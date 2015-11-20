import urllib, urlparse
from json import dumps
from flask import Flask
from flask import jsonify
from flask import request
from flask import abort
from flask import make_response
import os

app = Flask(__name__)

@app.route('/upload')
def make_video_data():
    youtube = request.args.get('youtube', '')
    facebook = request.args.get('facebook', '')
    print('facebook')
    print(youtube)
    print(facebook)
    return 'asdf'

@app.route('/')
def hello():
    return 'Hello World!'

# if __name__ == '__main__':
#     app.run(debug=True)