EXCHANGE_NAME = "smartsearch"
ROUTING = {
    'sklearn': {
        'QUEUE_NAME':  "sklearn_queue_input"
    },
    'transformers': {
        'QUEUE_NAME':  "transformers_queue_input"
    },
    'status': {
        'QUEUE_NAME':  "session-status"
    }
}
