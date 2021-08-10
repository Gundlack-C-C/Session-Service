import logging
import uuid
from werkzeug.exceptions import ServiceUnavailable, BadRequest
from RabbitMQ.Sender import sendMessage
from Exception.IncorrectInputException import IncorrectInputException


def validateInput(input):
    try:
        assert input.get('text', False) != False, '"text" missing!'
        assert input.get('param', False) != False, '"param" missing!'
        assert input['param'], '"param" empty!'
    except Exception as e:
        raise IncorrectInputException('Missing Field! ' + str(e)) from e


class SessionServer():
    def start_session(self, input, mode, _id=None):
        try: 
            validateInput(input)
        except Exception as e:
            raise BadRequest("Invalid Input! " + str(e)) from e

        _id = _id if _id else uuid.uuid4().hex
        try:
            sendMessage({"id": _id, "input": input}, routing_key=mode)

            sendMessage({"id": _id, "state": "NEW",
                         "msg": "New session commited to queue."}, routing_key='status')
        except Exception as e:
            logging.error(e)
            raise ServiceUnavailable(
                f'RabbitMQ Service not available! Reason: {str(e)}') from e

        return _id
