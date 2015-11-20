from video import youtube_download, get_youtube_video, hash_list

def hash_id(video_id, filename=None):
	if filename:
		youtube_download(video_id, filename)
	else:
		youtube_download(video_id)
	video = get_youtube_video(video_id)
	return hash_list(video)

