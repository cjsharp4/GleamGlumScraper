from youtube_transcript_api import YouTubeTranscriptApi #pip install youtube_transcript_api
import requests #pip install requests
from pytube import YouTube #pip install pytube
from moviepy.editor import * #pip install moviepy
import cv2 #pip install opencv-python
import os 
import pathlib #pip install pathlib
from csv import reader

# open file in read mode
with open('trending_links.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    video_id_list = []
    video_link_list = []
    for row in csv_reader:
        #iterate through first row 
        for i in range(0,len(row)):
        	#check if row is empty 
        	if row[i]:
        		#get video link 
        		video_link_list.append(row[i])
        		#get video id
        		video_id_list.append(row[i].split("v=",1)[1]) 


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

#video_link = 'https://www.youtube.com/watch?v=7iONU9LxeV8'  
#root = YouTubeTranscriptApi.get_transcript('7iONU9LxeV8') 

#for key in root:
#	print(key['text'])
	
#list of words that we are looking to find in the video
ee_uh_words = ['bleem','bleen','breap','dreach','dreek','dreen','fleach','fleem','freach',
'freen','freap','gleech','gleek','gleap','greech','yeach','keach','cleem','crene','pleech',
'plene','pleap','preep','scheach','screek','screep','sleech','smeach','smeek','smeem','smeen',
'smeap','sneme','sneen','spleach','spleek','spleem','spleep','spreach','spreek','spream','spreap',
'streech','threech','treach','threne','treen','zeech','zeek','zeem','blum','blun','brup','druch',
'druck','drun','fluch','flum','fruch','frun','frup','gluch','gluck','glup','gruch','yuch','kuch',
'clum','crun','pluch','plun','plup','prup','schuch','scruck','scrup','sluch','smuch','smuck',
'smum','smun','smup','snum','snun','spluch','spluck','splum','splup','spruch','spruck','sprum',
'sprup','struch','thruch','truch','thrun','trun','zuch','zuck','zum','Wean','Mead','Clique','Peek',
'Keyed','Seep','Sleet','Cream','Wheeze','Creaks','Peat','Deem','Scene','Steed','Heel','Chic','Street',
'Dream','Bleed','Seek','Teaks','Grief','Theme','Neat','Meme','Reef','Deal','Deke','Cheek','Peer','Meat',
'Sheik','Beak','Sneak','Peep','Leaks','Deed','Teak','Keys','Heat','Sheave','Meek','Sheet','Sheen','Seem',
'Been','Speed','Peen','Leash','League','Deel','Bees','Bean','Beam','Seam','Leeks','Stream','Leave',
'Peace','Keep','Seen','Gleam','Kneel','Scream','Trees','Leak','Beat','Beef','Streak','Peak','Meal','Fiend',
'Leek','Teach','Fees','Geek','Tweeze','Least','Beast','Heal','Teen','Ream','Scheme','Keel','Bead',
'Dean','Beet','Wheat','Teared','Meet','Bud','Buck','Bum','Bun','Butt','Bust','Buff','Buzz','Blood',
'Chuck','Shuck','Cluck','Crux','Crumb','Done','Dud','Dumb','Duck','Drum','Fuzz','Fund','Guck','Glum',
'Gruff','Hut','Cup','Cud','Cuss','Lug','Luck','Lush','Lust','Love','Luck','Lux','Mud','Mutt','Muck','Mum',
'Nut','Pus','Puck','Putt','Pun','Pup','Rum','Rough','Scum','Scrum','Sum','Suck','Sup','Some','Sun','Shove',
'Shun','Shut','Shuck','Slut','Snuck','Spud','Stud','Struck','Strum','Strut','Touch','Tuck','Tux','Ton',
'Thumb','Truss','Twas','Won','What','Was']


for link in range(0,len(video_link_list)):

	video_link = video_link_list[link]  
	
	try:
		root = YouTubeTranscriptApi.get_transcript(video_id_list[link])
	except:
		root = "fail"

	if(root != "fail"):
		word_found = False
		which_word = "###"
		clip_number = 1
		for child in root:	
			transcript_section = child['text'].split()

			#begin downloading and clipping a video if a word from the list is found in the video's transcript
			if(any(word in transcript_section for word in ee_uh_words)):
				
				print("target word found")

				#get which word was said in the clip
				for word in ee_uh_words:
					if(word in transcript_section):
						which_word = word
						

				#for the first instance of a word being found, download the current video
				if(word_found == False):
					yt = YouTube(video_link)
					video_title = yt.title
					video_title = "".join( x for x in video_title if (x.isalnum() or x in "._- ")) #remove illegal characters from filename
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
		except:
			print("video did not contain any of the target words")
			video_filename = None
		else:
			if(os.path.isfile(removeFile)):
				os.remove(removeFile)
			
		
