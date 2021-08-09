from RabbitMQ.Listener import Listener
import RabbitMQ.Configuration as Configuration
from Firebase.FirebaseConnector import FirebaseConnector
import logging
import os
import sys
import argparse

fire_connector = None


def session_status_callback(ch, method, properties, body):
    logging.info(" [x] Session Status Received %r" % body.decode())
    status = {
        "id": "Test",
        "status": "Test",
        "msg": f"Message Received: {body.decode()}"
    }
    fire_connector.update_status("test", status)

    logging.info(" [x] Done")


if __name__ == '__main__':

    LOG = "./.log/session-status-service.log"
    try:
        # Setup Argument Parser
        parser = argparse.ArgumentParser(description='Argument Parser')
        parser.add_argument('--l', '--log', dest='LOGFILE', type=str, default=LOG,
                            help=f'path for logfile (default: {LOG})')
        parser.add_argument("--production", action='store_const',
                            help="set to production mode", const=True, default=False)

        args = parser.parse_args()
        # Check if production is set
        PRODUCTION = args.production
        os.environ['PRODUCTION'] = str(PRODUCTION)

        if not os.path.exists(os.path.abspath(os.path.dirname(args.LOGFILE))):
            os.makedirs(os.path.abspath(os.path.dirname(args.LOGFILE)))

        # Setup Logging
        logging.basicConfig(filename=args.LOGFILE, level=logging.INFO if PRODUCTION else logging.DEBUG,
                            format='%(asctime)s %(levelname)-8s %(message)s')
        logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

        logging.info(f"Starting Session Status Service with [{args}]")

        fire_connector = FirebaseConnector()
        logging.info("Connected to Firebase!")

        fire_connector.update_status("test",
                                     {"id": "test", "status": "test", "msg": "Session-Service Started"})

        routing_key = os.getenv('RABBITMQ_ROUTING_KEY')
        queue = Configuration.ROUTING[routing_key]['QUEUE_NAME']
        
        listener_sklearn = Listener(routing_key=routing_key)
        listener_sklearn.attachCallbackToQueue(queue, session_status_callback)
        listener_sklearn.run()

    except Exception as e:
        logging.error(e)
