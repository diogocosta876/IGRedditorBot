import tkinter as tk
import praw
from PIL import Image, ImageTk
import requests
from io import BytesIO
from instabot import Bot
import os
import shutil

def getPhoto(url):
    # GET PHOTO FROM POST URL AND CROP
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    width, height = img.size
    if height > width * 1.25:
        finalHeight = width * 1.25
        img = img.crop((0, (height - finalHeight) / 2, width, (height - finalHeight) / 2 + finalHeight))
    if width > height * 1.25:
        finalWidth = height * 1.25
        img = img.crop(((width - finalWidth) / 2, 0, (width - finalWidth) / 2 + finalWidth, 0))
    img.save("photoFull.png")

    # resize to fit frame
    basewidth = 400
    img = Image.open("photoFull.png")
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save("photo.png")


def ButtonPress():
    #GET NEXT POST.    CYCLES TROUGH THE URLS UNTIL ONE IS SUCCESSFULL, OR UNTIL THERE ARE NO MORE URLS TO CHECK

    global displayPostCount
    GOTPOST = False
    FINISHED = False
    while ((not GOTPOST) and (not FINISHED)):
        try:
            url= urlDict[displayPostCount]
            Posttitle= titleDict[displayPostCount]
            getPhoto(url)
            image1 = Image.open("photo.png")
            width, height = image1.size
            displayPhoto = ImageTk.PhotoImage(image1)
            label1.config(image=displayPhoto)
            label1.image = displayPhoto
            title.config(text=Posttitle, wraplength=width)
            displayPostCount += 1
            GOTPOST = True
        except:
            displayPostCount += 1
            if displayPostCount >= len(urlDict):
                print("No more Posts")
                FINISHED = True
            else:
                print("Post isn't compatible")

def SavePicture():
    global savecount
    NotSaved = True
    while NotSaved:
        if os.path.exists("downloaded" + str(savecount) + ".png"):
            savecount += 1
            continue
        shutil.copy("photoFull.png", "downloaded" + str(savecount) + ".png")
        print("saved at", savecount)
        savecount += 1
        NotSaved = False

def PostToInstagram():
    from credentials import IGuser, IGpassword
    window.destroy()
    #DESTROY COOKIES BECAUSE OF THE instabot API BUG
    if os.path.isdir("config"):
        shutil.rmtree("config")
        print("config removed")
    bot = Bot()
    bot.login(username=IGuser, password=IGpassword )
    bot.upload_photo('photoFull.png', caption=titleDict[displayPostCount])


### MAIN PROCESS ###

from credentials import credentialList
reddit = praw.Reddit(
    client_id = credentialList[0],
    client_secret = credentialList[1],
    username = credentialList[2],
    password = credentialList[3],
    user_agent = credentialList[4])

subreddit = reddit.subreddit("ProgrammerHumor")
hot_python = subreddit.hot(limit=50)

window = tk.Tk("RedditInfluencerBOT by diogocosta876 (https://github.com/diogocosta876)")

frame1 = tk.Frame(master=window, width=600, height=600, pady=20)
frame1.pack(fill=tk.BOTH, expand=True)

frame2 = tk.Frame(master=frame1, width=500, height=500, pady=20)
frame2.pack(expand=True)

frametitle = tk.Frame(master=frame1, pady=10)
frametitle.pack(expand=True)

frameSpacing = tk.Frame(master=frame1, width=100, height=20)
frameSpacing.pack(expand=True)
button = tk.Button(
    master=frame1,
    text="Next Image",
    height=3,
    width=30,
    command=ButtonPress
)
button.pack(side=tk.TOP)

button2 = tk.Button(
    master=frame1,
    text="Save Picture",
    height=3,
    width=30,
    command=SavePicture
)
button2.pack(side=tk.TOP)

button3 = tk.Button(
    master=frame1,
    text="Post To Instagram",
    height=3,
    width=30,
    command=PostToInstagram
)
button3.pack(side=tk.TOP)

i=1
urlDict = {}
titleDict = {}
for submission in hot_python:
    if not submission.stickied:
        print(submission.url)
        urlDict[i] = submission.url
        titleDict[i] = submission.title
        i+=1


# GET FIRST POST PRINTED
displayPostCount = 1
while True:
    try:
        getPhoto(urlDict[displayPostCount])
        image1 = Image.open("photo.png")
        displayPhoto = ImageTk.PhotoImage(image1)
        label1 = tk.Label(master=frame2, image=displayPhoto)
        label1.image = displayPhoto
        label1.pack()
        title = tk.Label(master=frametitle, text=titleDict[displayPostCount], font=("calibri", 26), padx = 20)
        title.pack()
        savecount = 0
        displayPostCount += 1
        # print(urlDict)
        # print(titleDict)
        window.mainloop()
        break
    except:
        print("post didnt work")
        displayPostCount +=1



