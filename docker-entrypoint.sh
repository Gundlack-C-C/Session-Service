#!/bin/sh

echo "##### Input ######"
printf "Container Environment: [%s]\n" "$MODE"
printf "Application name : [%s]\n" "$APPLICATION_NAME"
printf "Listen Port : [%s]\n" "$PORT"
printf "Log level : [%s]\n" "$LOG_LEVEL"
echo "##################"
echo ""

if [ "$MODE" = "PROD" ]; then
    echo "Start production server"
    SCRIPT_NAME=/"$APPLICATION_NAME" gunicorn -w 2 -b 0.0.0.0:"$PORT" --log-level "$LOG_LEVEL" --access-logfile "-" server:app
elif [ "$MODE" = "SESSION-STATUS-SERVICE" ]; then
    echo "Start Session Status Service"
    python3 ./session-status-service-app.py --production
elif [ "$MODE" = "SESSION-SERVICE" ]; then
    echo "Start Session Status Service"
    python3 ./server.py --production
elif [ "$MODE" = "DEV" ]; then
    echo "Development Mode - Sleep to connect to container"
    /bin/sh -c "while sleep 1000; do :; done"
else
    echo "Start Server"
    python3 ./server.py
fi