'''
Created on Mar 20, 2017

@author: wzy
'''
import config
from os import remove
from watson_developer_cloud.text_to_speech_v1 import TextToSpeechV1

def text2speech(fileName='', message=''):
    if fileName == '' :
        fileName = '/home/vcap/app/app/static/tmp/output.wav'
        print(fileName)
        
    if message == '' :
        message = 'Hello world!'
    
    try :
        remove(fileName)
    except :
        print('there is no file exist')
    # user watson api to transfer the text to speech
    text_to_speech = TextToSpeechV1(
        username=config.bluemix_username,
        password=config.bluemix_password,
        x_watson_learning_opt_out=True)  # Optional flag

    with open(fileName, 'wb') as audio_file:
        audio_file.write(text_to_speech.synthesize(message, accept='audio/wav', 
                                                   voice=config.bluemix_watsonvoice))
