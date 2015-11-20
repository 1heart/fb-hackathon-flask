from video import youtube_download, get_youtube_video, hash_list
import db
def hash_id(video_id, filename=None):
	if filename:
		youtube_download(video_id, filename)
	else:
		youtube_download(video_id)
	video = get_youtube_video(video_id)
	return hash_list(video)

def get_url(id_or_key):
	if len(id_or_key) <= 12:
		# youtube
		return 'https://www.youtube.com/watch?v=' + id_or_key
	else:
		# facebook
		return id_or_key

def get_hash_list(id_or_key):
	for (key, value) in db.database.iteritems():
		if value == get_url(id_or_key):
			return key
	# not going to work for facebook
	return hash_list(get_youtube_video(id_or_key))