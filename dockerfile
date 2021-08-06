FROM python:3.8-slim

ARG REQUIREMENTS=requirements.txt
COPY ${REQUIREMENTS} /tmp/
RUN pip install --upgrade pip
RUN pip install -r /tmp/${REQUIREMENTS}

WORKDIR /usr/src/app
COPY ./app .

COPY ./docker-entrypoint.sh .
RUN chmod +x ./docker-entrypoint.sh