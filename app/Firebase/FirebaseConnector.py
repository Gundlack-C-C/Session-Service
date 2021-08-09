import firebase_admin
from firebase_admin import credentials
import os
from werkzeug.exceptions import ServiceUnavailable
from firebase_admin import firestore
from datetime import datetime
from datetime import timezone

class FirebaseConnector():
    app = None
    db = None

    def __init__(self):
        try:
            path_cred = os.getenv('FIREBASE_CREDENTIALS')
            assert os.path.isfile(
                path_cred), f"Invalid Credential Path! [{path_cred}]"

            cred = credentials.Certificate(path_cred)
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
                'array': firestore.ArrayUnion([status]),
                'changed': firestore.SERVER_TIMESTAMP
            })
        else:
            self.db.collection('session_status').document(id).set({
                'array': firestore.ArrayUnion([status]),
                'changed': firestore.SERVER_TIMESTAMP,
                'created': firestore.SERVER_TIMESTAMP
            })
