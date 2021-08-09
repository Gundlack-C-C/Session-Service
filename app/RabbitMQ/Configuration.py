import os

EXCHANGE_NAME = os.getenv("RABBITMQ_EXCHANGE_NAME")
ROUTING = {
    'sklearn': {
        'QUEUE_NAME':  os.getenv("QUEUE_SKLEARN_INPUT")
    },
    'transformers': {
        'QUEUE_NAME':  os.getenv("QUEUE_TRANSFORMERS_INPUT")
    },
    'status': {
        'QUEUE_NAME': os.getenv("QUEUE_STATUS_INPUT")
    }
}
