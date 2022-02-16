

# RedditorInfluencerBOT :speech_balloon:

This is a side project created by [diogocosta876](https://github.com/diogocosta876)

The python bot allows the user to cycle through a given subreddit's hot posts, it **displays a post's image and title onto a GUI** while enabling the user to **post the image and title (as caption) on instagram** or **save the image** locally.

The project's Key Elements:
* **Image resizing and display** onto the **GUI**
* **Image Saving**
* **Image cropping** for Instagram's post requirements
* **File management**
* Usage of **3rd party wrapper APIs**
* Development of a **Responsive User Interface**, using buttons to allow for **user input**

The post cycling works by chaching all the post URLs and Titles. When the "Next Post" button is pressed the script fetches the post image, resizes it, crops it and updates the GUI's image and text frames.
It uses **Praw** (Python Reddit API Wrapper) and **InstaBot** (Instagram API Wrapper) to fetch posts and submit them.

## Warning:
The **InstaBot** library is currently facing issues because of Instagram accelerating the deprecation of instagram API Platform, image posting my take anywhere up to 5 minutes or it might not work at all. As such the IG posting function will not work as intended until a fix is found.

## Setting up the aplication
* Put your Reddit aplication and instagram account credentials on **credentialsEXAMPLE.py** (search for praw tutorials for getting the reddit aplication set up)
* Rename credentialsExample.py to **credentials.py**
* Install requirements as needed
* Run script.py

## Requirements
tkinter
praw
PIL
requests
io
os
instabotBot
shutil


## Demo:

![](https://github.com/diogocosta876/IGRedditorBot/blob/main/demo.gif?raw=true)
