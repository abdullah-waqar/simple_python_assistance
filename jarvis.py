# READ LINE 69 , 100 , 146 , 148 , 161

from tkinter.constants import S
from plyer import notification
from pytube import YouTube
import pyautogui

import time


import datetime

# opening for jokes

import pyjokes
import pytube
# use to get the microphone input
import speech_recognition as sr

# importing for wikipedia text

import wikipedia

# importing for opening web browsers

import webbrowser

# importing for speaking text

import pyttsx3

# importing for plying music
import os

import random

from googlesearch import search

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# this will wish me (good morning or good evening or good afternoon)
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if (hour >= 0 and hour < 12):
        speak("Good morning")
    elif (hour >= 12 and hour <= 15):
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("I am your personal assistant. how can i help you?")


def jokes():
    joke = pyjokes.get_joke()
    print(joke)
    speak(f"Joke related to programing language: {joke}")
    speak("haha")

def drinkig_water():
    notification.notify(
        title="Drinking water",
        message="The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
        #Set this according to your path
        app_icon = "C:\PythonProjects\DrinkWaterNotificationApp\water.ico",
        timeout = 4,
    )

def takeCommand():
    # it will take microphone input and return string as a output

    r = sr.Recognizer()

    print("Listening........")

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.energy_threshold = 2000
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio , language='en-in')
        print("user said: " , query)
    except Exception as e:
        print("Something went worng please try again!")
        print("Please try again!")
        return "None"
    return query


speak("please enter your password")

password = pyautogui.password(title="Password" , text="Enter your password" , mask="*")
# Set this accoding to your path
with open("C:\\PythonProjects\\Jarvis\\password.txt" , 'r') as f:
    checking = f.read()
track = 0
if password != checking:
    wishMe()
    drinkig_water()
    speak("Hey bro don't forget to drink water")
    while(True):
        track += 1
        print(f"value: {track}")
        query =  takeCommand().lower()
        value = 10
        print(f"value: {track}")
        if track == value:
            drinkig_water()
            track = 0

        if "wikipedia" in query:
            speak("Searching on wikipedia...")
            query = query.replace("wikipedia" , "")
            print(f"query is:  {query}")
            result = wikipedia.summary(query , sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif("open youtube" in query):
            webbrowser.open("youtube.com")
        elif("open google" in query):
            webbrowser.open("google.com")
        elif("open ek hunter channel on youtube" in query or "open my channel" in query or "ek hunter" in query):
            webbrowser.open("https://www.youtube.com/channel/UCT0agxs7mWavl8NXbMy6Pxw")
        elif("open blogger" in query):
            webbrowser.open("https://www.blogger.com/blog/posts/797105350213107316")
        elif("open stackoverflow" in query):
            webbrowser.open("stackoverflow.com")
        elif("open python documents" in query):
            webbrowser.open("https://docs.python.org/3/")
        elif("who are you" in query):
            speak("I am personal assistant of abdullah waqar lodhi")
        elif("who is your crush" in query or "who is your love" in query):
            speak("You are going very personal bro")
        elif("joke" in query or "jokes" in query):
            jokes()
        elif("play song" in query or "play songs" in query or "play music" in query or "music" in query):
                # music directory , set this according to your path
                music_directory = 'C:\\Users\\EK HunterZ\\Music\\New folder'
                # makeing list of all the songs in music directory using os module (os.listdir)
                songs = os.listdir(music_directory)
                a = len(songs)
                random_number = random.randint(0 , a-1)
                print("length of song is: " , a)
                # stating and opening song
                os.startfile(os.path.join(music_directory , songs[random_number]))
        elif "the time" in query:
            storing_time = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"the time is {storing_time}")
        elif "what is your name" in query:
            speak("My name is personal assistant of abdullah waqar lodhi")
            
            # SET THESES TO YOUR PATH
        elif "open visual studio code" in query:
            path_of_file = "C:\\Users\\EK HunterZ\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            # now i am opening the file using os module
            os.startfile(path_of_file)
        elif "open pycharm" in query:
            path_of_file = "C:\\Program Files\\JetBrains\\PyCharm 2020.3.1\\bin\\pycharm64.exe"
            os.startfile(path_of_file)
        elif "open intellij" in query or "open java code editor" in query:
            path_of_file = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2020.1.2\\bin\\idea64.exe"
            os.startfile(path_of_file)
        elif "open chrome" in query or "open any browser" in query:
            path_of_file = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path_of_file)
        elif "open this pc" in query:
            path_of_file = "C:\\Users\\EK HunterZ\\Desktop"
            os.startfile(path_of_file)
        elif "quit" in query or "exit" in query:
            speak("ok i am going bye take care")
            exit()
        elif "screenshot" in query:
            speak("taking screen shot")
            screenshot = pyautogui.screenshot("yourScreenshot.png")
        
            path = None
            speak("Please enter a path where i should safe your screenshot")
            try:
                path = pyautogui.prompt(title="user input" , text="Enter your name" ,
                default="C:\\PythonProjects\\yourscreenshot.png")
                screenshot.save(str(path))
                speak("Opening your screen shot")
                os.startfile(str(path))
            except Exception as e:
                speak("Some thing went wrong")
                speak("May be your path is not correct.please try again")
        elif "download youtube video" in query or "how to download youtube video" in query:
            speak("please enter a url of youtube video")
            try:
                url = pyautogui.prompt(title="Download youtube video",
                text="Enter the url of youtue video",default="https://youtu.be/rOZaxdPYP7U")
                video = YouTube(url)
                title = video.title
                speak(str(title))
                speak("Enter the quality of video in pixels")
                quality = pyautogui.prompt(title="Video quality" , text="Enter the video quality",default="480p")
                video = video.streams.get_by_resolution(str(quality))
                speak("Downloading video")
                SAVE_PATH = "E:/"
                video.download(SAVE_PATH)

            except Exception as e:
                print("Some thing went wrong")
                print("May be your entered url is not correct you can try again!")
                print(e)
        elif "open cmd" in query:
            path = "C:\\Windows\\system32\\cmd.exe"
            os.startfile(path)
        else:
            for i in search(query , num=1 , stop=1):       
                webbrowser.open(str(i))
else:
    speak("You are not my boss go to the hell")






