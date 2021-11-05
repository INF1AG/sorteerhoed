import firebase_admin
import uuid
from firebase_admin import credentials
from firebase_admin import firestore

def send_data(username, points):
	cred = credentials.Certificate("./creds.json")
	firebase_admin.initialize_app(cred, {
		'projectId': 'thndr-1ca0e'
	})

	db = firestore.client()
	ref = db.collection(u'thdnrsorteerhoed')
	document = ref.document(str(uuid.uuid4()))
	document.set({
		u'username': username,
		u'points': points
	})