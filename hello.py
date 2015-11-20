import urllib, urlparse
from json import dumps
from flask import Flask
from flask import jsonify
from flask import request
from flask import abort
from flask import make_response
import os

app = Flask(__name__)

# curdir = os.getcwd() + '/'
# cv = '../cv/'
# os.chdir(cv)
import hashTest, video, db


@app.route('/upload')
def make_video_data():
    youtube = request.args.get('youtube', '')
    facebook = request.args.get('facebook', '')
    # print('facebook')
    # print(youtube)
    # print(facebook)
    if youtube:
    	handle_youtube(youtube)
    return jsonify({'youtube': 'success', 'facebook': 'success'})


def handle_youtube(video_id):
	video.youtube_download(video_id)
	curr_video = video.get_youtube_video(video_id)
	hash_list = hashTest.get_hash_list(video_id)
	db.add_to_db(hash_list, 'https://www.youtube.com/watch?v=' + video_id)
	return True


@app.route('/')
def hello():
    return 'Hello World!'

# if __name__ == '__main__':
#     app.run(debug=True)
# handle_youtube('j8D8YjgnGR4')
 # db.find_best_match(db.database.keys()[0])