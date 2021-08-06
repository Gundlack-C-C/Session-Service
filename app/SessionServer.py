import logging
import uuid
from werkzeug.exceptions import NotImplemented, ServiceUnavailable
from RabbitMQ import SessionProducer

class SessionServer():
    def get_total_active(self):
        raise NotImplemented("")

    def start_session(self, input, _id=None):
        _id = _id if _id else uuid.uuid4().hex

        try:
            SessionProducer.publisch_new_session({"id": _id, "input": input})
        except Exception as e:
            logging.error(e)
            raise ServiceUnavailable(f'RabbitMQ Service not available! Reason: {str(e)}') from e

        return _id
