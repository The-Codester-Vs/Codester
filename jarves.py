import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import json
import requests
# ?import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe(): 
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello, i am jarvis . Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        # viveksharma06

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)  
        print("Please check Internet Connection")  
        speak("Please check Internet connection ") 
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587 )
    server.ehlo()
    server.starttls()
    server.login('vivekthecodester@gmail.com', '7024453050vicky')
    server.sendmail('vivekthecodester@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    webbrowser.register('chrome',None)
    webbrowser.BackgroundBrowser('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            print("According to Wikipedia: ",results)
            speak("According to Wikipedia")
            speak(results)

        elif 'search'  in query:
            query = query.replace("search", " ")
            url = "https://www.google.com.tr/search?q={}".format(query)    
            webbrowser.open(url)
            speak("done!")
            print("Done!")
        
        elif 'play' in query:
            query = query.replace('play','')
            url  = 'https://www.youtube.com.tr/search?q={}'.format(query)
            webbrowser.open(url)
            speak('done!')
            print('Done!')
        
        elif 'news' in query:
            speak("News Mode")
            print("Types of news:\n1.Technology News\n2.Daily News\n3.Google News ")
            speak("choose one for technology news , two for daily news  and three for Google news")
            speak("Enter chosen number ")
            choice = int(input("Enter chosen number: "))
            i = 1
            if choice == 1:
                        print("Technology News..")
                        speak("Technology NEWS ")
                        speak("Lets begin..")
                        url = "http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=599f339605364caf9c199b7352312c9e"
                        news = requests.get(url).text
                        news_dict = json.loads(news)
                        arts = news_dict['articles']
                        for article in arts:
                            print(f"{i}.", article['title'])
                            speak(article['title'])
                            # print("------------------------------------------------------------------------------------------------------")
                            i = i + 1
                            if i == 6:
                                break
                            speak("Moving on to the next news. ")
            elif choice == 2:
                        print("Daily News..")
                        speak("Daily News")
                        speak("Lets begin..")
                        url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=599f339605364caf9c199b7352312c9e"
                        news = requests.get(url).text
                        news_dict = json.loads(news)
                        arts = news_dict['articles']
                        for article in arts:
                            print(f"{i}.", article['title'])
                            speak(article['title'])
                            # print("------------------------------------------------------------------------------------------------------")
                            i = i + 1
                            if i == 6:
                                break
                            speak("Moving on to the next news. ")
            elif choice == 3:
                        print("Google News..")
                        speak("Google News")
                        speak("Lets begin..")
                        url = "http://newsapi.org/v2/everything?q=apple&from=2020-11-02&to=2020-11-02&sortBy=popularity&apiKey=599f339605364caf9c199b7352312c9e"
                        news = requests.get(url).text
                        news_dict = json.loads(news)
                        arts = news_dict['articles']
                        for article in arts:
                            print(f"{i}.", article['title'])
                            speak(article['title'])
                            # print("------------------------------------------------------------------------------------------------------")
                            i = i + 1
                            if i == 6:
                                break
                            speak("Moving on to the next news. ")
                    
            print("Thanks for listening..")
            speak("Thanks for listening...")
            
        elif 'open youtube' in query:
            url = 'https://www.youtube.com/'
            webbrowser.open(url)
            speak("done!")
            print("Done!")

        elif 'open whatsapp' in query:
            url = 'https://web.whatsapp.com/'
            webbrowser.open(url)
            speak("done!")
            print("Done!")    

        elif 'manage my google account' in query:
            url = 'https://myaccount.google.com/?utm_source=account-marketing-page&utm_medium=go-to-account-button&pli=1&nlr=1'
            webbrowser.open(url)
            speak("done!")
            print("Done!")   

        elif 'calculator mode' in query:
            speak("calculator mode")
            speak("enter first number")
            print("Enter the first number:")
            num1=int(input())
            speak("Enter second number")
            print("Enter the second number:")
            num2 = int(input())
            speak("select your operators by symbols or type out to quit")
            num3=input("select the operators(+,-,/,*) and for exit() type out:\n")
            if num3 == '+' :
                speak("addition")
                add = num1+num2
                print(add)
                speak(f"your answer is {add}")
                print("|-------x------------------x--------------------x-----|")
                continue
            elif num3 =='-':
                speak("subtraction")
                sub = num1 - num2
                print(sub)
                speak(f"your answer is {sub}")
                print("|-------x------------------x--------------------x-----|")

                continue
            elif num3=='*':
                speak("multiplication")
                multi = num1*num2
                print(multi)
                speak(f"your answer is {multi}")
                print("|-------x------------------x--------------------x-----|")
                continue
            elif num3=='/':
                speak("divide")
                divide=num2/num1
                print(divide)
                speak(F"your answer is {divide}")
                print("|-------x------------------x--------------------x-----|")

                continue
            elif num3=='out':
                print("see you later")
                speak("see you later")
                continue
            else:
                print("try again")

        elif 'open google' in query:
            url = 'https://www.google.com/'
            webbrowser.open(url)
            speak("done!")
            print("Done!")

        elif 'open facebook' in query:
            url = 'https://www.facebook.com/'
            webbrowser.open(url)
            speak("done!")
            print("Done!") 

        elif 'open instagram' in query:
            url = 'https://www.instagram.com/'
            webbrowser.open(url)
            speak("done!")
            print("Done!")

        elif 'open mail' in query:
            url = 'https://mail.google.com/'
            webbrowser.open(url)
            speak("done!")
            print("Done!")   

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Vivek Sharma\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open pinterest' in query:
            url = 'https://in.pinterest.com/'
            webbrowser.open(url)
            speak("done!")
            print("Done!") 

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'who are you' in query:    
            print("sir, i am jarvis your personal assistant")
            speak("sir, i am jarvis your personal assistant") 

        elif 'open code' in query:
            codePath = "C:\\Program Files\\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'who made you' in query:
            speak("The team of programmers made me")

        elif 'how are you' in query:
            speak("I am fine ")
            
        elif 'hey jarvis' and "hi jarvis" in query:
            speak("yes sir i am here")

        elif 'exit' in query:
            speak("BYE BYE , sir")
            break

        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "viveksharma55236@gmail.com"    
                sendEmail(to, content)
                print("Email has been sent!")
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry White devil. I am not able to send this email") 

        elif 'email to sharad' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "patidarsharad3011@gmail.com"    
                sendEmail(to, content)
                print("Email has been sent!")
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry White devil. I am not able to send this email")    
                        
        elif 'email to samriddhi' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "samriddhijadhav12@gmail.com"    
                sendEmail(to, content)
                print("Email has been sent!")
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry White devil. I am not able to send this email")

        elif 'email to pranav' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "pranavsp1977@gmail.com"    
                sendEmail(to, content)
                print("Email has been sent!")
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry White devil. I am not able to send this email") 

        elif 'email to ricky' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "rickyjangid9000@gmail.com"    
                sendEmail(to, content)
                print("Email has been sent!")
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry White devil. I am not able to send this email")                      