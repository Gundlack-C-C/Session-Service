from concurrent.futures import ThreadPoolExecutor
import RabbitMQ.SessionReceiver as SessionReceiver
import logging
import os
import sys
import argparse

def session_callback_sklearn(ch, method, properties, body):
    logging.info(" [x] Sklearn Received %r" % body.decode())
    logging.info(" [x] Done")

def session_callback_transformers(ch, method, properties, body):
    logging.info(" [x] Transformers Received %r" % body.decode())
    logging.info(" [x] Done")

if __name__ == '__main__':

    LOG = "./.log/session-service-receiver.log"

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

    logging.info(f"Starting Receiver with [{args}]")

    try:
        #Start Receiver for all queues
        with ThreadPoolExecutor() as executor:
            f_receiver_sklearn = executor.submit(SessionReceiver.connect, 'transformers', session_callback_transformers)
            f_receiver_sklearn = executor.submit(SessionReceiver.connect, 'sklearn', session_callback_sklearn)

    except Exception as e:
        logging.error(e)

  