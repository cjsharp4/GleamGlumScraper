from youtube_transcript_api import YouTubeTranscriptApi #pip install youtube_transcript_api
import requests #pip install requests
from pytube import YouTube #pip install pytube
from moviepy.editor import * #pip install moviepy
import cv2 #pip install opencv-python
import os 
import pathlib #pip install pathlib


##TODO require coords to be certain size so that face is big enough to see in video
##TODO OPTIMIZE CLIP LENGTH SO ONLY TARGET WORD IS IN CLIP (HARDER TODO)
def faceDetect(clip_name):
	#Load the cascade  
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  #open face classifier from opencv github
  
	# To capture video from existing video.   
	cap = cv2.VideoCapture(clip_name)  

	faces_array = []
	count = 0

	while True:
		#read frame (img variable)
		_, img = cap.read()  
	

		#stop at end of frames in video
		if(img is None):
			break

		#Convert to grayscale  
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
  
		#Detect the faces  
		faces = face_cascade.detectMultiScale(gray, 1.1, 5)  #increase last two argument (scaleFactor and minNeighbors) for stricter classification

		faces_array.append(faces)
		count = count + 1

	#remove empty tuples or frames with no face detection
	faces_array = [t for t in faces_array if t != ()]
	print('frames with face: ' + str(len(faces_array)))
	print('total frames: ' + str(count))
	print(len(faces_array)/count)
	print('-----------------------')

	#Release VideoCapture object  
	cap.release()

	if( (len(faces_array)/count) > 0.80 ):
		return True
	
	return False


def saveClip(clip_name):
	cwd = os.getcwd()

	current_filepath = cwd + '/' + clip_name
	destination_folder = cwd + '/' + clip_name[:-10]
	destination_filepath = destination_folder + '/' + clip_name

	pathlib.Path(destination_folder).mkdir(parents=True, exist_ok=True)

	os.rename(current_filepath, destination_filepath)



"""
example video link:
https://www.youtube.com/watch?v=7iONU9LxeV8

this is the video id:
7iONU9LxeV8
"""

video_link = 'https://www.youtube.com/watch?v=7iONU9LxeV8'  
root = YouTubeTranscriptApi.get_transcript('7iONU9LxeV8') 

#for key in root:
#	print(key['text'])
	
ee_uh_words = ["glum" , "gleam"] #list of words that we are looking to find in the video

word_found = False
which_word = "###"
clip_number = 1
for child in root:	
	transcript_section = child['text'].split()

	#begin downloading and clipping a video if a word from the list is found in the video's transcript
	if(any(word in transcript_section for word in ee_uh_words)):
		
		#get which word was said in the clip
		for word in ee_uh_words:
			if(word in transcript_section):
				which_word = word

		#for the first instance of a word being found, download the current video
		if(word_found == False):
			yt = YouTube(video_link)
			video_title = yt.title
			video_filename = video_title + ".mp4"
			#yt.streams.first().download()
			download_video = yt.streams.filter(progressive = True, file_extension = "mp4").first().download(filename=video_filename)
			word_found = True

		#find the start and ending times of each transcript portion with a target word
		start = int(float(child['start']))
		end = int(float(child['duration'])) + start + 1
		clip = VideoFileClip(video_filename).subclip(start, end)

		#name file with video's title, the target word found, and number of clip within an individual video 
		clip_name = video_title + "_" + which_word + "_clip" + str(clip_number) + ".mp4"
		clip_number += 1

		#write file that will contain video and audio
		clip.write_videofile(clip_name, temp_audiofile='temp-audio.m4a', remove_temp=True, codec="libx264", audio_codec="aac")
		#print(unescape(child.text), int(float(child.attrib['start'])), "\n")

		clip.close()

		#if a face is detected for at least 80% of the video
		if(faceDetect(clip_name)):
			saveClip(clip_name)
		else:
			removeFile = os.getcwd() + '/' + clip_name
			if(os.path.isfile(removeFile)):
				os.remove(removeFile)



#remove full length downloaded video
try:
	removeFile = os.getcwd() + '/' + video_filename
	if(os.path.isfile(removeFile)):
		os.remove(removeFile)
except NameError:
	print("video did not contain any of the target words")
	video_filename = None