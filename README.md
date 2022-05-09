# GleamGlumScraper

--Some Quick Notes--

I have fixed previous bugs when running the script on windows.

--How to run the script--

Note: Depending on how you initially installed python onto your computer, any commands that use the keywords 'pip' and 'python' may need to be replaced with 'pip3' and 'python3'.

1) Press the green 'code' button on the main Github page for this project and download the project ZIP.
2) Extract the files and drag them onto your main Desktop screen for ease of access later.
3) Open a command prompt (windows) or terminal (mac) on your computer. 
4) Use command 'cd' to navigate to the folder containing the scraper.
5) Install all packages by using the command: 'pip install -r requirements.txt'
6) If step 3 does not work, individually install required packages using command 'pip install name-of-package'
7) Make sure that you have folders: 'EE_Videos' and 'UH_Videos' in the same folder as the python script
8) Run command 'python videoScraper.py' to run the script. 

Here is a picture of a windows user navigating to the project folder located on their Desktop directory and running the script:

![Capture2](https://user-images.githubusercontent.com/65328908/167336669-508644f6-9289-4c76-9fa9-411a58fc2879.PNG)

--What to do if pytube is not currently working--

If pytube seems to be causing the script to crash, Use the command: ``pip install --upgrade pytube`` to see if there are any new updates to pytube.

The current version of pytube works as of 5/8/2022, but may stop working in the future for several weeks at a time. If pytube is causing the script to crash, go to: https://github.com/pytube/pytube/issues and see if other people are getting the same error message as you. Often times, the fix for the problem will require you to edit a line of code in 'cipher.py' based on provided solutions listed in the issue ticket on Github. The pytube folder on your computer will probably be located in a similar spot as the picture below:

![Capture3](https://user-images.githubusercontent.com/65328908/167337589-e508b408-a60d-4e40-8dcf-6c770e936cd6.png)

Open up cipher.py using a text editor and do the modifications listed in the Github ticket. Save the file after changing the correct lines of code. 

The program should now work again.


--Improvements--

One issue that may occur in some clips is in the case that someone is saying the target word offscreen and another person's face is detected. 
 
Optimize clip length/frame so only target word is in the clip (harder)
