import os

EXCHANGE_NAME = os.getenv("RABBITMQ_EXCHANGE_NAME")
ROUTING = {
    'sklearn': {
        'QUEUE_NAME':  os.getenv("RABBITMQ_QUEUE_SKLEARN_INPUT")
    },
    'transformers': {
        'QUEUE_NAME':  os.getenv("RABBITMQ_QUEUE_TRANSFORMERS_INPUT")
    },
    'status': {
        'QUEUE_NAME': os.getenv("RABBITMQ_QUEUE_STATUS_INPUT")
    }
}
