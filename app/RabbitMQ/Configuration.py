import os

EXCHANGE_NAME = os.getenv("RABBITMQ_EXCHANGE_NAME")
ROUTING = {
    'sklearn': {
        'QUEUE_NAME':  os.getenv("RABBITMQ_SKLEARN_QUEUE_INPUT")
    },
    'transformers': {
        'QUEUE_NAME':  os.getenv("RABBITMQ_TRANSFORMERS_QUEUE_INPUT")
    },
    'status': {
        'QUEUE_NAME': os.getenv("RABBITMQ_STATUS_QUEUE")
    }
}
