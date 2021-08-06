#!/bin/sh

echo "docker-entrypoint.sh executing ..."

echo "Start Session-Service"
python3 /usr/src/app/server.py

echo ""
echo "##################"
echo "Finished!"