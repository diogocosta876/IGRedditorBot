<img align="left" padding-top="30" width="40" height="40" src="https://raw.githubusercontent.com/diogocosta876/IGRedditorBot/main/logo.png">

# RedditorInfluencerBOT

This is a side project created by [diogocosta876](https://github.com/diogocosta876)

The python bot allows the user to cycle through a given subreddit's hot posts, it **displays a post's image and title onto a GUI** while enabling the user to **post the image and title (as caption) on instagram** or **save the image** locally.

The project's Key Elements:
* **Image resizing and display** onto the **GUI**
* **Image Saving**
* **Image cropping** for Instagram's post requirements
* **File management**
* Usage of **3rd party wrapper APIs**
* Development of a **Responsive User Interface**, using buttons to allow for **user input**

The post cycling works by chaching all the post URLs and Titles. When the "Next Post" button is pressed, the script fetches the post image, resizes it, crops it and the GUI's image and text frames are updated 
It uses **Praw** (Python Reddit API Wrapper) and **InstaBot** (Instagram API Wrapper) to fetch posts and submit them.

[cult-img]:     https://external-preview.redd.it/iDdntscPf-nfWKqzHRGFmhVxZm4hZgaKe5oyFws-yzA.png?auto=webp&s=38648ef0dc2c3fce76d5e1d8639234d8da0152b2
## Warning:
The **InstaBot** library is currently facing issues because of Instagram accelerating the deprecation of instagram API Platform, image posting my take anywhere up to 5 minutes or it might not work at all. As such the IG posting function will not work as intended until a fix is found.

## Requirements
tkinter
praw
PIL
requests
io
os
instabotBot
shutil
