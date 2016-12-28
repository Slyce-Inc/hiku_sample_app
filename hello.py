#!flask/bin/python2.7
import os
from flask import Flask
from flask import request
from flask import send_from_directory
import requests
import pusher
from flask import render_template, request, flash,redirect


app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to the hiku sample app!"

@app.route("/beep", methods = ['POST'])
def showLastBeep():
    name = request.form.get('name', 'no data to show')
    token = request.form.get('token', '1234')


    # broadcast the name data to pusher
    PUSHER_APP_ID = "53386"
    PUSHER_KEY = "735d7f3f26bde43a7a72"
    PUSHER_SECRET = "02a27e77a29a104ba596"

    data = {'name': name, 'ean': '00018823'}

    testPusher = pusher.Pusher(app_id=PUSHER_APP_ID, key=PUSHER_KEY, secret=PUSHER_SECRET)
    testPusher[token].trigger('newDataReady', data)

    return name

@app.route('/showBeep')
def showBeep():
    return send_from_directory('docs', 'showBeep.htm')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

