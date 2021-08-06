#!/bin/sh

echo "docker-entrypoint.sh executing ..."

echo "Start RabbitMQ Session Listener"
python3 ./server.py

echo ""
echo "##################"
echo "Finished!"