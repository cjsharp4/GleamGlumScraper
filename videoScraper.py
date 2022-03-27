from youtube_transcript_api import YouTubeTranscriptApi #pip install youtube_transcript_api
import requests #pip install requests
from pytube import YouTube #pip install pytube
from moviepy.editor import * #pip install moviepy
import cv2 #pip install opencv-python
import os 
import pathlib #pip install pathlib
from csv import reader
import time

start = time.time()

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


def saveClip(clip_name,folder_name,phoneme):
	cwd = os.getcwd()

	current_filepath = cwd + '/' + clip_name

    #gets directory for proper folder based on word's phoneme
	phoneme_folder = cwd + '/'
	if(phoneme == "(EE)"):
		phoneme_folder += "EE_Videos"
	else:
		phoneme_folder += "UH_Videos"

	destination_folder = phoneme_folder + '/' + folder_name
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
ee_uh_words = [['bleem','(EE)'],['bleen','(EE)'],['breap','(EE)'],['dreach','(EE)'],['dreek','(EE)'],['dreen','(EE)'],['fleach','(EE)'],['fleem','(EE)'],['freach','(EE)'],['freen','(EE)'],['freap','(EE)'],['gleech','(EE)'],['gleek','(EE)'],['gleap','(EE)'],['greech','(EE)'],['yeach','(EE)'],['keach','(EE)'],['cleem','(EE)'],['crene','(EE)'],['pleech','(EE)'],['plene','(EE)'],['pleap','(EE)'],['preep','(EE)'],['scheach','(EE)'],['screek','(EE)'],['screep','(EE)'],['sleech','(EE)'],['smeach','(EE)'],['smeek','(EE)'],['smeem','(EE)'],['smeen','(EE)'],['smeap','(EE)'],['sneme','(EE)'],['sneen','(EE)'],['spleach','(EE)'],['spleek','(EE)'],['spleem','(EE)'],['spleep','(EE)'],['spreach','(EE)'],['spreek','(EE)'],['spream','(EE)'],['spreap','(EE)'],['streech','(EE)'],['threech','(EE)'],['treach','(EE)'],['threne','(EE)'],['treen','(EE)'],['zeech','(EE)'],['zeek','(EE)'],['zeem','(EE)'],['blum','(UH)'],['blun','(UH)'],['brup','(UH)'],['druch','(UH)'],['druck','(UH)'],['drun','(UH)'],['fluch','(UH)'],['flum','(UH)'],['fruch','(UH)'],['frun','(UH)'],['frup','(UH)'],['gluch','(UH)'],['gluck','(UH)'],['glup','(UH)'],['gruch','(UH)'],['yuch','(UH)'],['kuch','(UH)'],['clum','(UH)'],['crun','(UH)'],['pluch','(UH)'],['plun','(UH)'],['plup','(UH)'],['prup','(UH)'],['schuch','(UH)'],['scruck','(UH)'],['scrup','(UH)'],['sluch','(UH)'],['smuch','(UH)'],['smuck','(UH)'],['smum','(UH)'],['smun','(UH)'],['smup','(UH)'],['snum','(UH)'],['snun','(UH)'],['spluch','(UH)'],['spluck','(UH)'],['splum','(UH)'],['splup','(UH)'],['spruch','(UH)'],['spruck','(UH)'],['sprum','(UH)'],['sprup','(UH)'],['struch','(UH)'],['thruch','(UH)'],['truch','(UH)'],['thrun','(UH)'],['trun','(UH)'],['zuch','(UH)'],['zuck','(UH)'],['zum','(UH)'],['Wean','(EE)'],['Mead','(EE)'],['Clique','(EE)'],['Peek','(EE)'],['Keyed','(EE)'],['Seep','(EE)'],['Sleet','(EE)'],['Cream','(EE)'],['Wheeze','(EE)'],['Creaks','(EE)'],['Peat','(EE)'],['Deem','(EE)'],['Scene','(EE)'],['Steed','(EE)'],['Heel','(EE)'],['Chic','(EE)'],['Street','(EE)'],['Dream','(EE)'],['Bleed','(EE)'],['Seek','(EE)'],['Teaks','(EE)'],['Grief','(EE)'],['Theme','(EE)'],['Neat','(EE)'],['Meme','(EE)'],['Reef','(EE)'],['Deal','(EE)'],['Deke','(EE)'],['Cheek','(EE)'],['Peer','(EE)'],['Meat','(EE)'],['Sheik','(EE)'],['Beak','(EE)'],['Sneak','(EE)'],['Peep','(EE)'],['Leaks','(EE)'],['Deed','(EE)'],['Teak','(EE)'],['Keys','(EE)'],['Heat','(EE)'],['Sheave','(EE)'],['Meek','(EE)'],['Sheet','(EE)'],['Sheen','(EE)'],['Seem','(EE)'],['Been','(EE)'],['Speed','(EE)'],['Peen','(EE)'],['Leash','(EE)'],['League','(EE)'],['Deel','(EE)'],['Bees','(EE)'],['Bean','(EE)'],['Beam','(EE)'],['Seam','(EE)'],['Leeks','(EE)'],['Stream','(EE)'],['Leave','(EE)'],['Peace','(EE)'],['Keep','(EE)'],['Seen','(EE)'],['Gleam','(EE)'],['Kneel','(EE)'],['Scream','(EE)'],['Trees','(EE)'],['Leak','(EE)'],['Beat','(EE)'],['Beef','(EE)'],['Streak','(EE)'],['Peak','(EE)'],['Meal','(EE)'],['Fiend','(EE)'],['Leek','(EE)'],['Teach','(EE)'],['Fees','(EE)'],['Geek','(EE)'],['Tweeze','(EE)'],['Least','(EE)'],['Beast','(EE)'],['Heal','(EE)'],['Teen','(EE)'],['Ream','(EE)'],['Scheme','(EE)'],['Keel','(EE)'],['Bead','(EE)'],['Dean','(EE)'],['Beet','(EE)'],['Wheat','(EE)'],['Teared','(EE)'],['Meet','(EE)'],['Bud','(UH)'],['Buck','(UH)'],['Bum','(UH)'],['Bun','(UH)'],['Butt','(UH)'],['Bust','(UH)'],['Buff','(UH)'],['Buzz','(UH)'],['Blood','(UH)'],['Chuck','(UH)'],['Shuck','(UH)'],['Cluck','(UH)'],['Crux','(UH)'],['Crumb','(UH)'],['Done','(UH)'],['Dud','(UH)'],['Dumb','(UH)'],['Duck','(UH)'],['Drum','(UH)'],['Fuzz','(UH)'],['Fund','(UH)'],['Guck','(UH)'],['Glum','(UH)'],['Gruff','(UH)'],['Hut','(UH)'],['Cup','(UH)'],['Cud','(UH)'],['Cuss','(UH)'],['Lug','(UH)'],['Luck','(UH)'],['Lush','(UH)'],['Lust','(UH)'],['Love','(UH)'],['Luck','(UH)'],['Lux','(UH)'],['Mud','(UH)'],['Mutt','(UH)'],['Muck','(UH)'],['Mum','(UH)'],['Nut','(UH)'],['Pus','(UH)'],['Puck','(UH)'],['Putt','(UH)'],['Pun','(UH)'],['Pup','(UH)'],['Rum','(UH)'],['Rough','(UH)'],['Scum','(UH)'],['Scrum','(UH)'],['Sum','(UH)'],['Suck','(UH)'],['Sup','(UH)'],['Some','(UH)'],['Sun','(UH)'],['Shove','(UH)'],['Shun','(UH)'],['Shut','(UH)'],['Shuck','(UH)'],['Slut','(UH)'],['Snuck','(UH)'],['Spud','(UH)'],['Stud','(UH)'],['Struck','(UH)'],['Strum','(UH)'],['Strut','(UH)'],['Touch','(UH)'],['Tuck','(UH)'],['Tux','(UH)'],['Ton','(UH)'],['Thumb','(UH)'],['Truss','(UH)'],['Twas','(UH)'],['Won','(UH)'],['What','(UH)'],['Was','(UH)']] 

#get list of ee_uh_words without the phoneme as a tuple
ee_uh = [x[0] for x in ee_uh_words]


test_counter = 0

for link in range(0,len(video_link_list)):

	test_counter += 1

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
			if(any(word in transcript_section for word in ee_uh)):
				
				print("target word found")

				#get which word and phoneme was said in the clip
				phoneme = ""
				word_index = 0
				for word in ee_uh:
					if(word in transcript_section):
						phoneme = ee_uh_words[word_index][1]
						which_word = word
					word_index += 1

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
				clip_name = phoneme + "-(" + which_word + ")_" + video_title + "_clip" + str(clip_number) + ".mp4"
				clip_number += 1
				folder_name = video_title

				#write file that will contain video and audio
				clip.write_videofile(clip_name, temp_audiofile='temp-audio.m4a', remove_temp=True, codec="libx264", audio_codec="aac")
				#print(unescape(child.text), int(float(child.attrib['start'])), "\n")

				clip.close()

				#if a face is detected for at least 80% of the video
				if(faceDetect(clip_name)):
					saveClip(clip_name,folder_name,phoneme)
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

#Print number of links analyzed and total elapsed time of script
end = time.time()
print("Number of videos analyzed:")
print(test_counter)
print("Elapsed Time:")
print(end - start)