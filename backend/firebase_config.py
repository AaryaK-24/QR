import firebase_admin
from firebase_admin import credentials, firestore

# Load Firebase Admin SDK credentials
cred = credentials.Certificate("backend/firebase-admin.json")
firebase_admin.initialize_app(cred)

# Connect to Firestore
db = firestore.client()
