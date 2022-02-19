# GleamGlumScraper

Some Quick Notes:

-I've been using macOS but I spent time making sure it works on Windows. 
On Windows if you try and scrape the same video it will give you an error since Windows won't replace files that have the same name.

-The current version of pytube (12.0.0) is working as of 2/18/2022 without any modifications to the package's source code. 

-One issue that may occur in some clips is in the case that someone is saying the target word offscreen and another person's face is detected. 


Improvements:

-File Organization: Videos currently contain the target word in their filename and are put into a folder with all the clips from the same video.
The actual vowel sound ("ee" or "uh") is not currently included in the filename. 

-Require coords of facial detection box to be a certain size so that face is big enough to see in the video

-Optimize clip length/frame so only target word is in the clip (harder)

-Use Selenium WebDriver to automate search for Youtube video links that are likely to contain the target words (hardest)
