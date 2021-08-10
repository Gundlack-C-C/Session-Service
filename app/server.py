from SessionServer import SessionServer
from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os
import json
from werkzeug.exceptions import BadRequest
import logging
import argparse

logger = logging.getLogger("Session-Service.Server")

app = Flask(__name__)
CORS(app)

server = SessionServer()


@app.route('/session', methods=['POST'])
def Commit_Session():
    try:
        data = json.loads(request.data)
    except Exception as e:
        logging.error("Invalid Input")
        raise BadRequest(f"Invalid Input! JSON format required! {e}") from e

    if not 'input' in data:
        raise BadRequest("Missing field: 'input'")

    input = data.get('input', None)
    mode = data.get('target', 'sklearn')

    session_id = server.start_session(input, mode)

    return jsonify(session_id)


if __name__ == '__main__':

    LOG = "./.log/session-service.log"

    # Setup Argument Parser
    parser = argparse.ArgumentParser(description='Argument Parser')
    parser.add_argument('--l', '--log', dest='LOGFILE', type=str, default=LOG,
                        help=f'path for logfile (default: {LOG})')
    parser.add_argument("--production", action='store_const',
                        help="set to production mode", const=True, default=False)

    args = parser.parse_args()
    # Check if production is set
    PRODUCTION = args.production
    os.environ['PRODUCTION'] = str(PRODUCTION)

    if not os.path.exists(os.path.abspath(os.path.dirname(args.LOGFILE))):
        os.makedirs(os.path.abspath(os.path.dirname(args.LOGFILE)))

    # Setup Logging
    logging.basicConfig(filename=args.LOGFILE, level=logging.INFO if PRODUCTION else logging.DEBUG,
                        format='%(asctime)s %(levelname)-8s %(message)s')
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

    logging.info(f"Starting Server with [{args}]")

    try:
        # Start Server
        app.run(host="0.0.0.0", debug=False, port=5001)

    except Exception as e:
        logging.error(e)
