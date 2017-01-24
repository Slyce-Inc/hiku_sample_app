#!flask/bin/python2.7

"""
.. :module: run.py
   :platform: Linux
   :synopsis: demo heroku app to accept webhook data and send it out over a Pusher channel
   :copyright: 2016, hiku labs, inc. All rights reserved.
.. moduleauthor: Rob Katcher <rob@hiku.us> (Dec 27, 2016)
"""

import os
from flask import Flask
from flask import request
from flask import send_from_directory
import requests
import pusher
import json


app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the hiku sample app!"

@app.route("/beep", methods = ['POST'])
def showLastBeep():
    payload = request.data
    print payload
    payload = json.loads(payload)
    data = payload['data']

    print data

    if data['eventDesc'] == 'PRODUCT_ENTRY':
        # this is a scan/speak from hiku
        msg = 'New item from hiku: ' + data['name']
    elif data['eventDesc'] == 'DEVICE_REGISTERED':
        # this is a new hiku that was setup
        msg = 'New hiku registered: ' + data['serialNumber']
    else:
        msg = data['eventDesc']

    # broadcast data to pusher
    PUSHER_APP_ID = os.environ['PUSHER_APP_ID']
    PUSHER_KEY = os.environ['PUSHER_KEY']
    PUSHER_SECRET = os.environ['PUSHER_SECRET']

    testPusher = pusher.Pusher(app_id=PUSHER_APP_ID, key=PUSHER_KEY, secret=PUSHER_SECRET)
    testPusher['MyPusherChannel'].trigger('newDataReady', msg)

    return data['name']

@app.route('/showBeep')
def showBeep():
    return send_from_directory('docs', 'showBeep.htm')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

