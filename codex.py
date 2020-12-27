# MODULES
import pyttsx3
import time
import speech_recognition as sr
import datetime as h
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import json
import requests

user = input("Enter Your name:")
user.capitalize()

#Starting
print("Starting.",end="")
time.sleep(1)
print(".",end="")
time.sleep(1)
print(".")

# Initialization
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


# Testing

def speak(audio):
    engine.say(audio,150)
    engine.runAndWait()

def wishme():
    hour = int(h.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak(f"Good morning {user}")
    elif hour>=12 and hour<18:
        speak(f"Good afternoon {user}")
    else:
          speak(f"Good Evening {user}")
    speak("Hey buddy how are you")
    
def command():
    # It take commands form the user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something..")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio,language="en-US")
        print(f"{user} said:{query}.\n")
        
    except Exception as e:
        print("Please Check 'Internet Connection'.." )
        speak("PLEASE CHECK INTERNET CONNECTION")
        return None
    return query

def sendMail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('vivekthecodester@gmail.com',"7024453050vicky")
    server.sendmail('vivekthecodester@gmail.com',to, content)
    server.close()
    
if __name__ == '__main__':
    webbrowser.register('chrome', None)
    webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    wishme()
    while True:
        query = command().lower()
        if "how are you" in query:
            speak(f"I am good and you {user}")
            print(f"I am Good and You {user}?")
        elif "who are you" in query:
            speak("I am codex Your personal assistant")
            print("I am codex.Your Personal Assistant!")
        elif "codex" in query:
            speak("yes i am here")
            
        elif "hello" in query:
            speak("hello sir")
            
        elif "google" in query:
            url = "www.google.com"
            webbrowser.open(url)
            
        elif "youtube" in query:
            url  = "www.youtube.com"
            webbrowser.open(url)
            
        elif "instagram" in query:
            url = "www.instagram.com"
            webbrowser.open(url)
            speak("Done sir!")
            
        elif "facebook" in query:
            url  = "www.facebook.com"
            webbrowser.open(url)
            speak("Done sir!")
            
        elif "pinterest" in query:
            url = "www.pinterest.com"
            webbrowser.open(url)
            speak("Done sir!")
            
        elif "whatsapp" in query:
        