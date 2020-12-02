from tkinter import *
import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pyjokes
import subprocess
import time

window = Tk()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate",180)


def read_text(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_usr():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        read_text("Good Morning!")
        print("Good Morning!")

    elif hour>=12 and hour<18:
        read_text("Good Afternoon!") 
        print("Good Afternoon!")   

    else:
        read_text("Good Evening!")  
        print("Good Evening!")     

def my_order():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("-Listening-")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("-Recognizing-")    
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:   
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('emaid', 'pass')
    server.sendmail('harshtanwar25@gmail.com', to, content)
    server.close()    
           
def start():
   
    wish_usr()
    
    read_text("How may i help you ")    
    print("How may i help you ") 

    while True:

        query = my_order().lower()

        # opens some other python programs       
       
        if 'calculate' in query: 
            os.system("Python calc.py")

        elif 'bmi' in query:
            os.system("Python bmicalculator.py")     

        # opens game of your choice
        elif 'game' in query:
            read_text("Which game do you want to play?")
            
            game_choice=my_order().lower()
            
            if 'guessing' in game_choice:
                read_text("Starting running game")
                os.system("Python guessinggame.py") 

            elif 'running' in game_choice:
                read_text("Starting running game")
                codePath = "F:\\My Game\Luffyrunner.exe" 
                os.startfile(codePath)

            elif 'tic tac' in game_choice:
                read_text("Starting tic-tac-toe")
                os.system("Python tictactoe.py")

            else:
                read_text("This game was not found in your system")

        elif 'coronavirus stats' in query:
            os.system("Python coronanotifier.py")  
        
        # opens websites on browser

        elif 'wikipedia' in query:
            read_text('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            read_text("According to Wikipedia")
            print(results)
            read_text(results)
            read_text("Anything else sir? ")  

        elif 'open youtube' in query:
            read_text("Opening Youtube")
            print("Opening Youtube")
            webbrowser.open("youtube.com")
            time.sleep(5)	
            read_text("Anything else sir? ")
            print("Anything else sir? ")

        elif 'open google' in query:
            read_text("Opening Google")
            webbrowser.open("google.com")
            time.sleep(5)	
            read_text("Anything else sir? ")
            print("Anything else sir? ")

        elif 'open facebook' in query:
            read_text("Opening facebook")
            webbrowser.open("facebook.com")  
            time.sleep(5)	 
            read_text("Anything else sir? ")
            print("Anything else sir? ")

        elif 'open github' in query:
            read_text("Opening github")
            webbrowser.open("github.com")
            time.sleep(5)	   
            read_text("Anything else sir? ")
            print("Anything else sir? ")
            

        elif 'anime' in query:
            read_text("Opening AnimeUltima")
            webbrowser.open("https://www1.animeultima.to/")
            time.sleep(5)	 
            read_text("Anything else sir? ")
            print("Anything else sir? ")
            

        elif 'search'  in query:
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)
            time.sleep(5)	
            read_text("Anything else sir? ")
            print("Anything else sir? ")    
        
        # plays music    

        elif 'music' in query:
            music_dir = 'D:\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            read_text("Anything else sir? ")
            print("Anything else sir? ")

        # tells time
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            read_text(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")
            read_text("Anything else sir? ")
            print("Anything else sir? ")

        # tells a joke

        elif 'joke' in query:
            read_text(pyjokes.get_joke())  
            print(pyjokes.get_joke()) 
            print("Anything else sir? ") 

        # sends email to me

        elif 'email to harsh' in query:
    
            try:
                read_text("What should I say?")
                content = my_order()
                print(content)
                to = "harshtanwar25@gmail.com"    
                sendEmail(to, content)
                read_text("Email has been sent!")
                print("Email has been sent!")
                read_text("Anything else sir? ")
                print("Anything else sir? ")
            except Exception as e:
                print(e)
                read_text("Sorry Mister Harsh. I am not able to send this email")    
  
        # runs files from my pc

        elif 'code' in query:
            codePath = "E:\\Microsoft VS Code\Code.exe"
            os.startfile(codePath)
            read_text("Anything else sir? ")
            print("Anything else sir? ")
        
        elif 'running game' in query:
            codePath = "F:\\My Game\Luffyrunner.exe" 
            os.startfile(codePath) 
            read_text("Anything else sir? ")
            print("Anything else sir? ")

        elif 'discord' in query:
            codePath = "C:\\Users\harsh\AppData\Local\Discord\App-0.0.308\Discord.exe" 
            os.startfile(codePath) 
            read_text("Anything else sir? ")
            print("Anything else sir? ")

        elif 'chrome' in query:
            codePath = "C:\\Program Files\Google\Chrome\Application\chrome.exe" 
            os.startfile(codePath) 
            read_text("Anything else sir? ") 
            print("Anything else sir? ")       

        #  System restart/signout/power off with confirmation

        elif 'restart' in query:
            read_text("Do you want to proceed? ")
            print("Do you want to proceed? ")
            confirmation=my_order()
            if confirmation=='yes':
                read_text("Restarting your pc")
                print("Restarting your pc")
                subprocess.call(["shutdown", "/r"])
            else:
                read_text("Anything else sir? ") 
                print("Anything else sir? ")   
 
        elif 'sign out' in query:
            read_text("Do you want to proceed? ")
            print("Do you want to proceed? ")
            confirmation=my_order()
            if confirmation=='yes':
                read_text("Signing out")
                print("Signing out")
                time.sleep(5)
                subprocess.call(["shutdown", "/l"])
            else:
                read_text("Anything else sir? ")  
                print("Anything else sir? ")   

        elif 'shutdown system' in query:
            read_text("Do you want to proceed? ")
            print("Do you want to proceed? ")
            confirmation=my_order()
            if confirmation=='yes':
                read_text("Shutting down your pc")
                print("Shutting down your pc")
                subprocess.call('shutdown / p /f')
            else:    
                read_text("Anything else sir? ") 
                print("Anything else sir? ")      
        
        # closes the program

        elif 'shutdown' in query:
            read_text("Shutting down....")
            print("Shutting down....")
            quit()

def update(layout):

    window.after(100, update, layout)


window.title('LUFFYBOT')

label = Label(window, width = 50, height = 30)
label.pack()
window.after(0, update, 0)

btn0 = Button(text = 'WISH ME',width = 25, command = wish_usr, bg = '#2ECC71')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(text = 'START',width = 25,command = start, bg = '#2ECC71')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text = 'EXIT',width = 25, command = window.destroy, bg = '#2ECC71')
btn2.config(font=("Courier", 12))
btn2.pack()

window.mainloop()