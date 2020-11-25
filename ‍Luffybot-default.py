import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import operator

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Luffy():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  
        

    speak("I am your personal assistant. How may i help you ? Sir!")       

def takeCommand():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:   
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Luffybot25@gmail.com', '8383028152')
    server.sendmail('harshtanwar25@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    Luffy()
    while True:
   
        query = takeCommand().lower()

        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            speak("Anything else sir? ")

        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")
            speak("Anything else sir? ")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")
            speak("Anything else sir? ")

        elif 'open stackoverflow' in query:
            speak("Opening stackoverflow")
            webbrowser.open("stackoverflow.com")   
            speak("Anything else sir? ")


        elif 'play music' in query:
            music_dir = 'D:\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Anything else sir? ")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            speak("Anything else sir? ")

        elif 'open code' in query:
            codePath = "E:\Microsoft VS Code\Code.exe"
            os.startfile(codePath)
            speak("Anything else sir? ")

        elif 'email to harsh' in query:
    
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harshtanwar25@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
                speak("Anything else sir? ")
            except Exception as e:
                print(e)
                speak("Sorry Mister Harsh. I am not able to send this email")    

        elif 'shutdown' in query:
            speak("bye-bye! Master")
            quit()

        elif 'play jumping game' in query:
            codePath = "E:\Codes\C++\Trex game.exe" 
            os.startfile(codePath)   
            speak("Anything else sir? ")
          
        elif 'play running game' in query:
            codePath = "F:\My Game\Luffyrunner.exe" 
            os.startfile(codePath) 
            speak("Anything else sir? ")

        elif 'open anime' in query:
            speak("Opening AnimeHaven")
            webbrowser.open("https://animeheaven.ru") 
            speak("Anything else sir? ")

        
                 
