#!/usr/bin/env python
from flask import Flask, request, make_response, render_template, redirect, json
from flask import url_for, abort, session, jsonify
import firebase_admin
from flask_cors import CORS, cross_origin
from firebase_admin import credentials, firestore, initialize_app
import sys
from urllib.parse import urlparse


app = Flask(__name__, template_folder='./templates/')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

cred = credentials.Certificate("../serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()




# make sure user is unicode string (u'mystring')
def setUnlock(user, challenge, setBool):
    doc_ref = db.collection(u'users').document(user).collection(u'challenges').document(challenge)
    doc_ref.set({
        u'Unlock': setBool
    })

# setUnlock(u'david', 'youtube', True)



@app.route('/')
def index():

    html = render_template('index.html')
    response = make_response(html)



    return response


@app.route('/_get_data/', methods=['POST'])
def _get_data():

    siteURL=None
    if request.method == "POST":

        siteURL=json.dumps(request.form['siteURL'])
        username=json.dumps(request.form['username'])

        siteURL = siteURL.replace('"', '') # gets rid of quotation marks within string so urlparse can work
        hostName = urlparse(siteURL).netloc
        hostName = hostName.replace('www.', '') # gets rid of the www.


    # siteURL = siteURL.replace("http://www.","")

    print('This is the URL: ' + siteURL, file=sys.stdout)
    print('This is the hostName: ' + hostName, file=sys.stdout)
    print('This is the username: ' + username, file=sys.stdout)


    #doc_ref = db.collection(u'users').document(username).collection(u'challenges').document(siteURL)
    # users_ref = db.collection(u'sampleData')
    # docs = users_ref.stream()

    # for doc in docs:
    #     print(f'{doc.id} => {doc.to_dict()}')

    myList = ['Element1', 'Element2', 'Element3']
    return jsonify({'data' : myList})


if __name__ == '__main__':
    app.run()