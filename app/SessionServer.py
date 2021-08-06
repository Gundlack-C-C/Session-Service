import logging
import uuid
from werkzeug.exceptions import NotImplemented
logger = logging.getLogger("SessionServer")


class SessionServer():
    def get_total_active(self):
        raise NotImplemented("")

    def start_session(self, input, _id=None):
        _id = _id if _id else uuid.uuid4().hex
        logging.info("Add Session to Queue")
        return _id
