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

The current version of pytube does not work. The file in 'Modified Packages' need to be swapped with the file of the same name in the pytube folder on your desktop. The pytube folder on your computer will probably be located in a similar spot as the picture below:

![Capture1](https://user-images.githubusercontent.com/65328908/167334203-5110cc25-5782-4315-bac7-6d812e2f133a.PNG)



--Improvements--

One issue that may occur in some clips is in the case that someone is saying the target word offscreen and another person's face is detected. 
 
Optimize clip length/frame so only target word is in the clip (harder)
