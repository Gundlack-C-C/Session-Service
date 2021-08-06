FROM python:3.8-slim

ARG REQUIREMENTS=requirements.txt
COPY ${REQUIREMENTS} /tmp/
RUN pip install --upgrade pip
RUN pip install -r /tmp/${REQUIREMENTS}

COPY ./app /usr/src/app
WORKDIR /usr/src/app

COPY ./docker-entrypoint.sh /usr/src/app/dockerInit/
ENTRYPOINT ["/usr/src/app/dockerInit/docker-entrypoint.sh"]