import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import os
import time
import subprocess
import webbrowser
import sklearn
#from ecapture import ecapture as ec
import wolframalpha
import json
import requests

print('Loading your AI personal assistant - Geralt')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")
        
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
        
        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")
            
        except Exception as e:
            speak("Pardon me, please say again")
            return "None"
        return statement
speak("Loading your AI personal assistant Geralt")
wishMe()


if __name__=='__main__':
    
    
    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue
        
        if "Good bye" in statement or "Ok bye" in statement or "Stop" in statement:
            speak('Your personal assistant Geralt is shutting down, Good bye')
            print('Your personal assistant Geralt is shutting down, Good bye')
            break
        
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia","")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
            
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)
            
            
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google is now open")
            time.sleep(5)
            
            
        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gamil.com")
            speak("GMail is now open")
            time.sleep(5) 
            
            
        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = takeCommand()
            complete_url = base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")
                
                
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            
            
            
        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Geralt your personal assistant. I am programmed to minor tasks like'
                  'opening youtube, google, gmail, stackoverflow, predict time, take a photo, search wikipedia, predict weather'
                  'in different cities, get top headline news from TOI and you can ask me computational or gegraphical questions too!')
        
            
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Piyush")
            print("I was built by Piyush")
            
            
        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")
            
            
        elif 'news' in statement:
            webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headline, Happy reading')
            time.sleep(7) 
            
            
        #elif "camera" in statement:
           # ec.capture(0, "robo camera", "img.jpg")
            
            
        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
            
            
        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
            
            
        elif "log off" in statement or "sign out" in statement:
            speak("Okay, your pc will log off in 10 seconds make sure to exit from all applications")
            subprocess.call(["shutdown", "/1"])
            
            
time.sleep(3)                
            
