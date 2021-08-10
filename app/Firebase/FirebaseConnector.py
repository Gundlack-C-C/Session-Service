import os
from werkzeug.exceptions import ServiceUnavailable
from datetime import datetime, timezone
import firebase_admin
from firebase_admin import credentials, firestore
import json
from Exception.IncorrectInputException import IncorrectInputException

class FirebaseConnector():
    app = None
    db = None

    def __init__(self):
        cred_json = None
        try:
            cred_str = os.getenv('FIREBASE_CREDENTIALS', None)
            assert cred_str != None, 'Missing Environment Variable "FIREBASE_CREDENTIALS"'

            try:
                cred_json = json.loads(cred_str)
            except Exception as e:
                raise IncorrectInputException('Invalid Environment Variable "FIREBASE_CREDENTIALS"! JSON format expected! ' + str(e))

            cred = credentials.Certificate(cred_json)
            self.app = firebase_admin.initialize_app(cred)

            self.db = firestore.client(self.app)
        except Exception as e:
            raise ServiceUnavailable(
                f"Unable to connect to firebase! Cause: {str(e)}") from e

    def update_status(self, id, status):
        status = {**status, **{"T": datetime.now(timezone.utc).isoformat()}}
        doc_ref = self.db.collection('session_status').document(id).get()
        if doc_ref.exists:
            self.db.collection('session_status').document(id).update({
                'status': firestore.ArrayUnion([status]),
                'changed': firestore.SERVER_TIMESTAMP
            })
        else:
            self.db.collection('session_status').document(id).set({
                'status': firestore.ArrayUnion([status]),
                'changed': firestore.SERVER_TIMESTAMP,
                'created': firestore.SERVER_TIMESTAMP
            })
