#!/usr/bin/env python
from flask import Flask, request, make_response, render_template, redirect, json
from flask import url_for, abort, session, jsonify
import firebase_admin
from flask_cors import CORS, cross_origin
from firebase_admin import credentials, firestore, initialize_app, db
import sys
from urllib.parse import urlparse


app = Flask(__name__, template_folder='./templates/', static_folder='./static/')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


databaseURL = 'https://hackptonfitnessapp-default-rtdb.firebaseio.com/'
cred = credentials.Certificate("../serviceAccountKey.json")
firebase_admin.initialize_app(cred, {'databaseURL':databaseURL})
# db = firestore.client()




# make sure user is unicode string (u'mystring')
# def setUnlock(user, challenge, setBool):
#     doc_ref = db.collection(u'users').document(user).collection(u'challenges').document(challenge)
#     doc_ref.set({
#         u'Unlock': setBool
#     })

# setUnlock(u'david', 'youtube', True)



@app.route('/')
def index():

    html = render_template('index.html')
    response = make_response(html)
    return response

@app.route('/profile')
def screen1():

    html = render_template('screen1.html')
    response = make_response(html)
    return response



@app.route('/challengeOne')
def screen2():

    html = render_template('screen2.html')
    response = make_response(html)
    return response

# @app.route('/css/<path:path>')
# def send_css(path):
#     return send_from_directory('templates', path)


@app.route('/challengeTwo')
def screen3():

    html = render_template('screen3.html')
    response = make_response(html)
    return response

@app.route('/recommendation')
def screen4():

    html = render_template('screen4.html')
    response = make_response(html)
    return response


@app.route('/_get_data/', methods=['POST'])
def _get_data():

    siteURL=None
    if request.method == "POST":

        siteURL=json.dumps(request.form['siteURL'])
        username=json.dumps(request.form['username'])

        username = username.replace('"', '')
        siteURL = siteURL.replace('"', '') # gets rid of quotation marks within string so urlparse can work
        hostName = urlparse(siteURL).netloc
        hostName = hostName.replace('www.', '') # gets rid of the www.


    # siteURL = siteURL.replace("http://www.","")

    print('This is the URL: ' + siteURL, file=sys.stdout)
    print('This is the hostName: ' + hostName, file=sys.stdout)
    print('This is the username: ' + username, file=sys.stdout)

    ref = db.reference('/users/' + username + "/challenges/" + hostName.replace('.com', ''))

    # doc_ref = db.collection(u'users').document(username).collection(u'challenges')
    values = ref.get()
    print(values, file=sys.stdout)

    challengeName = ''
    unlocked = True
    
    if(values['Unlock'] == "False"):
        unlocked = False
        challengeName = values['ChallengeName']
        print('Locked!', file=sys.stdout)

    return jsonify({'unlocked' : unlocked, 'title' : challengeName, 'hostName' : hostName})


if __name__ == '__main__':
    app.run()