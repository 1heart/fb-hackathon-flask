import urllib2
import json
import imagehash
import video
import re
import hashTest
import requests


def grabData():
	db = json.loads(urllib2.urlopen("http://testware.cloudapp.net:3000/getAllData").read())['data']
	print(db)
	# db = [{'redirect': 'google.com', 'videoHash': u'a'*128}]

	hashToUrl = {}

	for elem in db:
		url = elem['srcurl']
		hashes = elem['videoHash']
		lst = tuple(imagehash.hex_to_hash(str(hashes[i:i+16])) for  i in range(0, len(hashes), 16))
		hashToUrl[lst] = url

	return hashToUrl

# input is a hash_list
def find_best_match(vid):
	min_diff = float("inf")
	min_video = None
	print(len(database.keys()))
	for item in database.keys():
		matchrate = video.correlate_hash_list(vid, item)
		corr = matchrate[0]
		print('here')
		if corr < 15 and corr < min_diff:
			min_diff = corr
			print('there')
			min_video = item
	if not min_video:
		print('nope')
		return min_video
	else:
		print(min_video)
		print('yep')
		return database[min_video]

def extract_video(url):
	search = re.match(r'.*youtube.com/watch\?v=(.*)$', url, re.M|re.I)
	if search:
		video_id = search.group(1)
		return hashTest.hash_id(video_id)


database = grabData()

def add_to_db(hash_list, url):
	database[tuple(hash_list)] = url
	serialized = ''.join([str(x) for x in hash_list])
	r = requests.post("http://testware.cloudapp.net:3000/putVideo",
		data = {"videoHashes":serialized, "url": url, "redirect": ''})
	return True

