import logging
import uuid
from werkzeug.exceptions import NotImplemented, ServiceUnavailable
from RabbitMQ.Sender import sendMessage


class SessionServer():
    def get_total_active(self):
        raise NotImplemented("")

    def start_session(self, input, mode, _id=None):
        _id = _id if _id else uuid.uuid4().hex
        try:
            sendMessage({"id": _id, "input": input}, routing_key=mode)

            sendMessage({"id": _id, "state": "NEW", "msg": "New session commited to queue."}, routing_key='status')
        except Exception as e:
            logging.error(e)
            raise ServiceUnavailable(
                f'RabbitMQ Service not available! Reason: {str(e)}') from e

        return _id
