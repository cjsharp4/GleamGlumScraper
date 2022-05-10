# GleamGlumScraper

This scraper was built to create a real-world dataset of ‘ee’ and ‘uh’ words. This dataset of video clips must include clear facial movements of the person that said the word. 

--Generating the YouTube Links--

The scraper relies on another program called random_youtube.py (in the LinkGeneration folder) to generate a list of pseudo-random YouTube links for it to analyze. Our scraper needed to analyze randoms links so that there was no bias in the selection of videos we were collecting data from.

Using YouTube Data API v3, it was possible to make search queries that return the link to the top result of that query. Doing a search on YouTube with a 3 character string comprised of random numbers and letters seems to be the best way to get a ‘random’ video on YouTube. Through Python’s random module, we generated 200 strings of random numbers and letters using the seed 1 for the first 100 links and seed 3 for the last 100 links. Some example search queries: 'HCH' would return a video of a Mexican news segment (~12,000 views), 'OU8' would return a video showing off a corporate office (~500 views), and a query of 'OA9' would return a food vlog (~40,000 views). Until Google provides an official API to get random videos on YouTube, this is the best and most recommended way to accomplish this task.

--Building the Scraper--

The design of the video scraper can be broken down into 5 processes/steps:
1.	Download the video and search the transcript of the video for target words.
2.	Create sub clips of sentences where a target word is found.
3.	Use the OpenCV facial classifier to determine if the sub clip has a face present in the video for more than 80% of the frames.
4.	Save the sub clip and move it to the proper folder if a face is found to be present.
5.	Delete all clips that do not have a face present and full-length video.

After each video is analyzed, any accepted sub clips are placed into a folder based on which phoneme was in the target word found and then into another folder based on the title of the video. The file name of each sub clip would follow the format: '(PHONEME)-(WORD)-TITLE_CLIP#.mp4'. Here is an example of this format: '(EE)-(me)_ Minimal Every Day Carry EDC_clip76.mp4'.

Several open source Python packages were utilized to build this scraper. 

 -Pytube provided an easy method to download an mp4 file for each video link. 

 -The youtube-transcript-api package was used to get the transcripts of each video. In addition to giving the transcript of a video, this package also included the   timestamp and duration for each sentence spoken in the video. 

 -Moviepy was used to create sub clips based on the timestamps provided by the youtube-transcript-api and the full length video file provided by pytube. 

 -The OpenCV package was used to work with their frontal-face classifier in order to detect if 80% of the frames in a video contained a face in it or not. This requirement of 80% seemed to work very well in tests, as the classifier does not always detect a face for the entire length of a video clip (even when the face is present).    

Internally, some of these packages required the 'requests' module in order to make HTTP requests to YouTube.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

--How to run the script--

Note: Depending on how you initially installed python onto your computer, any commands that use the keywords 'pip' and 'python' may need to be replaced with 'pip3' and 'python3'.

1) Press the green 'code' button on the main Github page for this project and download the project ZIP.
2) Extract the files and drag them onto your main Desktop screen for ease of access later.
3) Open a command prompt (windows) or terminal (mac) on your computer. 
4) Use command ``cd`` to navigate to the folder containing the scraper.
5) Install all packages by using the command ``pip install -r requirements.txt``
6) If step 3 does not work, individually install required packages using command ``pip install name-of-package``
7) Make sure that you have folders: 'EE_Videos' and 'UH_Videos' in the same folder as the python script
8) Run command ``python videoScraper.py`` to run the script. 

Here is a picture of a windows user navigating to the project folder located on their Desktop directory and running the script:

![Capture2](https://user-images.githubusercontent.com/65328908/167336669-508644f6-9289-4c76-9fa9-411a58fc2879.PNG)

--What to do if pytube is not currently working--

If pytube seems to be causing the script to crash, Use the command ``pip install --upgrade pytube`` to see if there are any new updates to pytube.

The current version of pytube works as of 5/8/2022, but may stop working in the future for several weeks at a time. If pytube is causing the script to crash, go to: https://github.com/pytube/pytube/issues and see if other people are getting the same error message as you. Often times, the fix for the problem will require you to edit a line of code in 'cipher.py' based on provided solutions listed in the issue ticket on Github. The pytube folder on your computer will probably be located in a similar spot as the picture below:

![Capture3](https://user-images.githubusercontent.com/65328908/167337589-e508b408-a60d-4e40-8dcf-6c770e936cd6.png)

Open up cipher.py using a text editor and do the modifications listed in the Github ticket. Save the file after changing the correct lines of code. 

The program should now work again.


--Improvements--

There is a chance that the transcript of a video (especially when it was auto-generated) may have some inaccuracies where some words may be different from what was actually said in the video. In this case, the clip may not contain the target word. I have found that this does not happen very often, so it is not a big issue.

One issue that may occur in some clips is in the case that someone is saying the target word offscreen and another person's face is detected. 
 
Optimize clip length/frame so only target word is in the clip (harder)
