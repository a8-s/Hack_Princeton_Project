#!/usr/bin/env python
from flask import Flask, request, make_response, render_template, redirect, json
from flask import url_for, abort, session
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app


app = Flask(__name__, template_folder='./templates/')


cred = credentials.Certificate("../serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


# make sure user is unicode string (u'mystring')
def setUnlock(user, challenge, setBool):
    doc_ref = db.collection(u'users').document(user).collection(u'challenges').document(challenge)
    doc_ref.set({
        u'Unlock': setBool
    })

setUnlock(u'david', 'youtube', True)

@app.route('/')
def index():

    html = render_template('index.html')
    response = make_response(html)

    return response


if __name__ == '__main__':
    app.run()