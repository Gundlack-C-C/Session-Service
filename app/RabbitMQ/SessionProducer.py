import pika
import os

#IP = os.getenv('RABBITMQ_SERVICE_IP')
IP = os.getenv('RABBITMQ_SERVICE_IP')
PORT = os.getenv('RABBITMQ_SERVICE_PORT')
username = os.getenv('RABBITMQ_USERNAME')
password = os.getenv('RABBITMQ_PASSWORD')

def publisch_new_session(input):
    creds = pika.PlainCredentials(username,password)
    parameters = pika.ConnectionParameters(IP,PORT, credentials=creds)
    
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
    print(" [x] Sent 'Hello World!'")
    connection.close()
