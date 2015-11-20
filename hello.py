import urllib, urlparse
from json import dumps
from flask import Flask
from flask import jsonify
from flask import request
from flask import abort
from flask import make_response

# application = Flask(__name__)

# if __name__ == '__main__':
#     application.run(debug=True)

import os
# from flask import Flask

app = Flask(__name__)

@app.route('/upload', methods=['GET'])
def make_video_data():

    youtube = request.args.get('youtube', '')
    facebook = request.args.get('facebook', '')
    if facebook != '':
        try:
            facebook = urlparse.parse_qs(facebook).values()[0][0]
        except:
            facebook = ''
    print(youtube)
    print(facebook)

    # hash the video

    # upload to Block Chain
    return params

@app.route('/')
def hello():
    return 'Hello World!'

