import os

EXCHANGE_NAME = "smartsearch"
ROUTING = {
    'sklearn': {
        'QUEUE_NAME_INPUT':  os.getenv("QUEUE_SKLEARN_INPUT")
    },
    'transformers': {
        'QUEUE_NAME_INPUT':  os.getenv("QUEUE_TRANSFORMERS_INPUT")
    }
}

