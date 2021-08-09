#!/bin/sh

echo "##### Input ######"
printf "Container Environment: [%s]\n" "$ENVIRONMENT"
printf "Application name : [%s]\n" "$APPLICATION_NAME"
printf "Listen Port : [%s]\n" "$PORT"
printf "Log level : [%s]\n" "$LOG_LEVEL"
echo "##################"
echo ""

if [ $ENVIRONMENT = "PROD" ]; then
    echo "Start production server"
    SCRIPT_NAME=/"$APPLICATION_NAME" gunicorn -w 2 -b 0.0.0.0:"$PORT" --log-level "$LOG_LEVEL" server:app
elif [ $ENVIRONMENT = "SESSION-STATUS-SERVICE" ]; then
    echo "Start Session Status Service"
    python3 ./session-status-service-app.py --production
elif [ $ENVIRONMENT = "SESSION-SERVICE" ]; then
    echo "Start Session Status Service"
    python3 ./server.py --production
else
    echo "Start Server"
    python3 ./server.py --production
fi