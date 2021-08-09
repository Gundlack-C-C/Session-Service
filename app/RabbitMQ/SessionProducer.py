import pika
import os
import json
from Exception.IncorrectInputException import IncorrectInputException
import RabbitMQ.Configuration as Configuration

#IP = os.getenv('RABBITMQ_SERVICE_IP')
IP = os.getenv('RABBITMQ_SERVICE_IP')
PORT = os.getenv('RABBITMQ_SERVICE_PORT')
username = os.getenv('RABBITMQ_USERNAME')
password = os.getenv('RABBITMQ_PASSWORD')

def publisch_new_session(input, routing_key):
    creds = pika.PlainCredentials(username,password)
    parameters = pika.ConnectionParameters(IP,PORT, credentials=creds)

    if routing_key not in list(Configuration.ROUTING.keys()):
        raise IncorrectInputException(f'Routing key ["{routing_key}"] does not exist!')

    queue = Configuration.ROUTING[routing_key]['QUEUE_NAME_INPUT']

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_publish(exchange=Configuration.EXCHANGE_NAME, routing_key=routing_key, body=json.dumps(input))
    connection.close()
