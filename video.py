from __future__ import unicode_literals
import youtube_dl, cv2
import os
from PIL import Image
from imagehash import phash
import random


curdir = os.getcwd() + '/'
dldir = 'dl/'

ydl_opts = {
	'format': 'best',
	'outtmpl': dldir + "%(id)s"
}

ydl = youtube_dl.YoutubeDL(ydl_opts)

def youtube_download(video_id, filename=dldir + "%(id)s.%(ext)s"):
	if not get_youtube_video(video_id):
		ydl = youtube_dl.YoutubeDL(ydl_opts)
		ydl.download(['https://www.youtube.com/watch?v=' + video_id])

'''
Returns a cv2 VideoCapture object,
or None if the file doesn't exist.
'''
def get_youtube_video(video_id):
	if video_id in os.listdir(curdir + dldir):
		return cv2.VideoCapture(curdir + dldir + video_id)

# one frame per sampling rate
sampling_rate = 24

num_threads = 4

def hash_list(video):
	length = int(video.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
	ret = True
	i = 0

	phash_list = []
	while ret:
		video.set(cv2.cv.CV_CAP_PROP_POS_FRAMES,(i*sampling_rate + random.randint(0,sampling_rate)))
		ret,cv2_img = video.read()
		if not ret:
			break
		pil_im = Image.fromarray(cv2_img)
		phash_list.append(phash(pil_im))
		i+=1

	return phash_list

# Returns the minimum (best match) difference between all overlaps of the two hash lists.
def correlate_hash_list(a,b):
	if len(a) < len(b):
		a, b = b, a
	result = []
	for i in range(len(a)-len(b)+1):
		total = 0
		for j in range(len(b)):
			total += a[j+i] - b[j]
		result.append(total/float(len(b)))
	return min((val, idx) for (idx, val) in enumerate(result))

# test_id = 'NEx-qyZAmqs'
# same_id = 'NEx-qyZAmqs'
# different_id = 'KomzHoutxBY'


# video = get_youtube_video(test_id)
# same = get_youtube_video(same_id)
# different = get_youtube_video(different_id)

# vh = hash_list(video)
# sh = hash_list(same)
# dh = hash_list(different)