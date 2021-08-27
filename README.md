# Session-Service


## Environment variable
### Execution
- MODE : Container Mode 
   -  PROD : GUnicorn REST API Server
   -  SESSION-STATUS-SERVICE : RabbitMQ Listener to handle Status Queue Events
   -  SESSION-SERVICE : Flask Server - REST API
   -  DEV : DEV Mode to connect via VSCode development environment
### FIREBASE
- FIREBASE_CREDENTIALS : Firebase Service Account Credential - JSON
### RABBITMQ
- RABBITMQ_SERVICE_IP : IP of the RabbitMQ cluster
- RABBITMQ_SERVICE_PORT : Port (default: 5672)
- RABBITMQ_USERNAME : RabbitMQ account username 
- RABBITMQ_PASSWORD=guest: RabbitMQ account username
- RABBITMQ_EXCHANGE_NAME: Name of the exchange
- RABBITMQ_TRANSFORMERS_QUEUE_INPUT: Name of the sklearn queue
- RABBITMQ_TRANSFORMERS_ROUTING_KEY: Routing key for transformers queue
- RABBITMQ_SKLEARN_QUEUE_INPUT: Name of the sklearn queue
- RABBITMQ_SKLEARN_ROUTING_KEY:  Routing key for sklearn queue
- RABBITMQ_STATUS_QUEUE_INPUT:  Name of the status queue
- RABBITMQ_STATUS_ROUTING_KEY :  Routing key for status queue