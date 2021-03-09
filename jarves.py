import pyttsx3 #pip install pyttsx3
# import speech_recognition as sr #pip install speechRecognition
import datetime
import subprocess
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import requests ,json
from time import ctime
import time
import pyjokes
# import time
# ?import random
#-------------------------------------------------
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
#-------------------------------------------------
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#-------------------------------------------------
def wishMe(): 
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello, i am jarvis . Please tell me how may I help you")       
#-------------------------------------------------
# def takeCommand():
#     # #It takes microphone input from the user and returns string output
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)
#     #     # viveksharma06
#     try:
#         print("Recognizing..")
#         query = r.recognize_google(audio,language="en-US")
#         print(f"user said:{query}.\n")
#     except Exception as e:
#         # print(e)  
#         print("Please check Internet Connection")  
#         speak("Please check Internet connection ") 
#         return "None"
#     return query

def takeCommand():
    query = input("Write something here:")
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
    # wishMe()
    while True:
    # if 1:
        query = takeCommand()
        
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            print(f'Searching Wikipedia of {query}...')
            speak(f'Searching Wikipedia of {query}...')
            results = wikipedia.summary(query, sentences=4)
            print("According to Wikipedia: ",results)
            speak("According to Wikipedia")
            speak(results)
        # 

        elif 'search'  in query:
            query = query.replace("search", " ")
            url = "https://www.google.com.tr/search?q={}".format(query)    
            print(f"Searching for{query} form Google..")
            speak(f"Searching for{query} form Google..")
            webbrowser.open(url)
        
        elif 'play' in query:
            query = query.replace('play','')
            url  = 'https://www.youtube.com.tr/search?q={}'.format(query)
            webbrowser.open(url)
            speak('done!')
            print('Done!')
        
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
        elif "stop working" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)    
        
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
#("------------------------------------------------------------------------------------------------------")
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
                        url = "http://newsapi.org/v2/everything?q=tesla&from=2021-01-03&sortBy=publishedAt&apiKey=599f339605364caf9c199b7352312c9e"
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
            
        elif 'youtube' in query:
            url = 'https://www.youtube.com/'
            webbrowser.open(url)
            speak("opening youtube")
            print("Opening Youtube")
        
        elif "i love you" in query:
            speak("It's hard to understand")
        
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/" + location)
            speak("Hold on, I will show you where " + query[2] + " is.")
   
        # elif "write a note" in query:
        #     speak("What should i write, sir")
        #     note = takeCommand()
        #     file = open('jarvis.txt', 'w')
        #     file.write(note)
        #     speak("Your note has been written suecssfully..")
         
        # elif "show note" in query:
        #     speak("Showing Notes")
        #     file = open("jarvis.txt", "r") 
        #     print(file.read())
        #     speak(file.read(6))
        
        elif "weather" in query:
            api_key = "db0fcdaaf43c13337b1cb28c84078ff8"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"

            speak("Enter City Name")
            city_name = input("Enter city name : ") 

            complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
            response = requests.get(complete_url) 

            x = response.json() 

            if x["cod"] != "404": 
                y = x["main"]
 
                current_temperature = y["temp"] 
                current_pressure = y["pressure"] 
                current_humidiy = y["humidity"] 
                # currenet_visiblity = y['visibility']

                z = x["weather"] 

                # store the value corresponding 
                # to the "description" key at 
                # the 0th index of z 
                weather_description = z[0]["description"] 

                # print following values 
                print(f"Weather in {city_name}")
                speak(f"Weather in {city_name}")
                
                print(" Temperature  = " +
                                str((current_temperature)-273.15) +
                    "\n Atmospheric pressure (in hPa unit) = " +
                                str(current_pressure) +
                    "\n Humidity (in percentage) = " +
                                str(current_humidiy)+"%" +
                    "\n Description = " +
                                str(weather_description)) 
                speak(" Temperature is" +
                                str((current_temperature)-273.15)+
                    "\n Atmospheric Pressure is" +
                                str(current_pressure) +
                    "\n Humidity is  " +
                                str(current_humidiy)+"percentage"+
                    "\n Description is " +
                                str(weather_description)) 

            else: 
                print(" City Not Found ") 


        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

        elif 'whatsapp' in query:
            url = 'https://web.whatsapp.com/'
            webbrowser.open(url)
            speak("done!")
            
            print("Done!")    

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
            
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
            
            if num3 == '+':
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
        elif "time" in query:
            print(ctime())
            speak(f"Sir, the time is {ctime()}")
        elif 'google' in query:
            url = 'https://www.google.com/'
            webbrowser.open(url)
            speak("Opening google")
            print("Opening google")

        elif 'facebook' in query:
            url = 'https://www.facebook.com/'
            webbrowser.open(url)
            speak("Opening Facebook")
            print("Opening Facebook") 

        elif 'instagram' in query:
            url = 'https://www.instagram.com/'
            speak("Opening Instagram")
            print("Opening Instagram")
            webbrowser.open(url)
    
        elif "are you mad" in query:
            speak("No way")
        

        elif "discord" in query:
            url = "https://discord.com/"
            webbrowser.open(url)
            speak("Opening Discord..")
            print("Opening Discord..")            
                        
        elif 'open mail' in query:
            url = 'https://mail.google.com/'
            webbrowser.open(url)
            speak("Opening Mail")
            print("Opening Mail")   

        elif 'music' in query:
            try:
                music_dir = 'C:\\Users\\Vivek Sharma\\Music'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))
            except Exception as e:
                print(e)

        
        elif 'pinterest' in query:
            url = 'https://in.pinterest.com/'
            webbrowser.open(url)
            speak("Opening Pinterest")
            print("Opening Pinterest") 

        elif 'who are you' in query:    
            print("sir, i am jarvis your personal assistant")
            speak("sir, i am jarvis your personal assistant") 

        elif 'open code' in query:
            codePath = "C:\\Program Files\\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'hello' in query or 'hey' in query:
            speak('hello sir ')

        elif "who made you" in query or "created you" in query: 
            speak("I have been created by Codester.")

        elif 'how are you' in query:
            speak("I am fine sir what about you sir")
            print("I am fine sir!.What about you sir?")
            
            
        elif 'hey jarvis' in query :
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
                speak("Sorry. I am not able to send this email") 
                        
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
                speak("Sorry. I am not able to send this email")

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
                speak("Sorry. I am not able to send this email") 

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
                speak("Sorry. I am not able to send this email")     
                
        
        elif "email to codexter" in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "vivekthecodester@gmail.com"
                sendEmail(to,content)
                print("Email has been sent!")
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email") 
                      