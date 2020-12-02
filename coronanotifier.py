import pyttsx3
import speech_recognition as sr
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier

engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:   
        print("Say that again please...")  
        return "None"
    return query

speak("Getting india's latest stats on corona virus")   
print("Getting india's latest stats on corona virus")   

header = {"User-Agent":"Chrome"}
req = Request("https://www.worldometers.info/coronavirus/country/india/", headers = header)
html = urlopen(req)
html.status
obj = bs(html,features="lxml")

new_cases = obj.find("li", {"class":"news_li"}).strong.text.split()[0]

print("New cases in India",new_cases)

new_deaths = list(obj.find("li", {"class":"news_li"}).strong.next_siblings)[1].text.split()[0]

print("Deaths in India",new_deaths)

speak(new_cases + " new cases and " + new_deaths + " new deaths were found ")


notifier = ToastNotifier()

speak("Just sent u a notification")
print("Just sent u a notification")

message  = "New Cases - "+ new_cases+"\nDeath - "+new_deaths

message

notifier.show_toast(title="COVID-19 Reporter", msg=message, duration=50)