
import pika, os

IP = os.getenv('RABBITMQ_SERVICE_IP')
PORT = os.getenv('RABBITMQ_SERVICE_PORT')
username = os.getenv('RABBITMQ_USERNAME')
password = os.getenv('RABBITMQ_PASSWORD')
 
 
def connect(routing_key, callback):
   creds = pika.PlainCredentials(username,password)
   parameters = pika.ConnectionParameters(IP,PORT,credentials=creds)
 
   connection = pika.BlockingConnection(parameters)
   channel = connection.channel()
 
   channel.queue_declare(queue=routing_key)
  
   channel.basic_consume(queue=routing_key, on_message_callback=callback, auto_ack=True)
 
   print(' [*] Waiting for messages. To exit press CTRL+C')
   channel.start_consuming()