from app import app
from flask import request
from flask import make_response
from app.controller import watsonAPI
import time
from os.path import dirname
from flask.templating import render_template

@app.route('/')
def index():
    return 'Hello, Flask!'

@app.route('/text2speech')
def text2speech():
    return render_template('text2speech.html')

@app.route('/dotext2speech', methods=['POST', 'GET'])
def doText2Speech():
    if request.method == 'GET':
        message = request.args.get('message')
    path = dirname(__file__)
    path = path[0:len(path) - 4]   
    fileName = 'static/tmp/' + str(time.time()) + 'message.wav'
    watsonAPI.text2speech(fileName = path + fileName, message=message)
    response = make_response(fileName)
    return response 