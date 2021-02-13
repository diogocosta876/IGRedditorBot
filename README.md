# RedditorInfluencerBOT

This is a side project created by [diogocosta876](https://github.com/diogocosta876)

The python bot allows the user to cycle through a given subreddit's hot posts, it **displays a post's image and title onto a GUI** while enabling the user to **post them on instagram** or **save the image** locally.

The project's Key Elements:
* **Image resizing and display** onto the **GUI**
* **Image Saving**
* **Image cropping** for Instagram's post requirements
* **File management**
* Usage of **3rd party wrapper APIs**
* Development of a **Responsive User Interface**, using buttons to allow for **user input** (tkinter)

The post cycling works by chaching all the post URLs and Titles. When the "Next Post" button is pressed, the script fetches the post image, resizes it, crops it and the GUI's Image and Text frames are updated 
It uses **Praw** (Python Reddit API Wrapper) and **InstaBot** (Instagram API Wrapper) to fetch posts and submit them.


**NOTE:**
The **InstaBot** library is currently facing issues because of Instagram accelerating the deprecation of instagram API Platform, image posting my take anywhere up to 5 minutes or it might not work at all. As such the Posting function will not work as intended until a fix is found.

# Requirements
tkinter
praw
PIL
requests
io
os
instabotBot
shutil
