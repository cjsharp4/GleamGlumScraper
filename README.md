# GleamGlumScraper

--Some Quick Notes--

I have fixed previous bugs when running the script on windows.

--How to run the script--

*Note* 
Depending on how you initially installed python onto your computer, any commands that use the keywords 'pip' and 'python' may need to be replaced with 'pip3' and 'python3'.

1) Start by opening a command prompt (windows) or terminal (mac) on your computer.
2) Install all the packages listed in "requirements.txt' using command 'pip install name-of-package' 
3) Use command 'cd' to navigate to the folder containing the scraper.
4) Run command 'python videoScraper.py' to run the script.
5) Make sure that you have folders: 'EE_Videos' and 'UH_Videos' in the same folder as the python script. 

The current version of pytube does not work. The file in 'Modified Packages' need to be swapped with the file of the same name in the pytube folder on your desktop. The pytube folder on your computer will probably be located in a similar spot as the picture below:

![Capture1](https://user-images.githubusercontent.com/65328908/167334203-5110cc25-5782-4315-bac7-6d812e2f133a.PNG)



--Improvements--

One issue that may occur in some clips is in the case that someone is saying the target word offscreen and another person's face is detected. 
 
Optimize clip length/frame so only target word is in the clip (harder)
