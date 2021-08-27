import os
import logging
from Exception.RabbitMQException import RabbitMQException

REQUIRED_VAR = [
    "RABBITMQ_EXCHANGE_NAME", 
    "RABBITMQ_SKLEARN_QUEUE_INPUT", 
    "RABBITMQ_TRANSFORMERS_QUEUE_INPUT", 
    "RABBITMQ_STATUS_QUEUE_INPUT"
]

EXCHANGE_NAME = os.getenv("RABBITMQ_EXCHANGE_NAME")
ROUTING = {
    'sklearn': {
        'QUEUE_NAME':  os.getenv("RABBITMQ_SKLEARN_QUEUE_INPUT")
    },
    'transformers': {
        'QUEUE_NAME':  os.getenv("RABBITMQ_TRANSFORMERS_QUEUE_INPUT")
    },
    'status': {
        'QUEUE_NAME': os.getenv("RABBITMQ_STATUS_QUEUE_INPUT")
    }
}

def AssertRabbitmqEnvironmentComplete():
    complete = True
    for VAR in REQUIRED_VAR:
        try:
            assert os.getenv(VAR) != None, f"Missing Environment Variable: ['{VAR}']"
        except Exception as e:
            complete = False
            logging.error(e)

    if not complete:
        raise RabbitMQException("Missing Environment Variables!")
