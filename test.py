#!/usr/bin/env python
from flask import Flask, request, make_response, render_template, redirect, json
from flask import url_for, abort, session
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app

cred = credentials.Certificate("../serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# make sure user is unicode string (u'mystring')
def setUnlock(user, challenge, setBool):
    doc_ref = db.collection(u'users').document(user).collection(u'challenges').document(challenge)
    doc_ref.update({
        u'Unlock': setBool
    })
    print('set')


def main():
    setUnlock(u'david', 'netflix', False)


    
    # doc_ref = db.collection(u'sampleData').document(u'inspiration')
    # users_ref = db.collection(u'sampleData')
    # docs = users_ref.stream()

    # for doc in docs:
    #     print(f'{doc.id} => {doc.to_dict()}')





if __name__ == '__main__':
    main()