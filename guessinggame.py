import pyttsx3
import speech_recognition as sr
import math
import random

engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",150)

def read_text(audio):
    engine.say(audio)
    engine.runAndWait()
    
def my_order():
    
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

print("This is a Guessing game")

read_text("In this game you will have to guess a number in a range that will be defined by you. You will be given only 5 guesses")

print("Here you will have to find a random number in a range defined by you")
print("You will be given only 5 guesses")

read_text("So now let the game begin, Good Luck")

read_text("Now ! give the lower limit of your range")
print("Now ! give the lower limit of your range")

lower = my_order()

read_text("Now ! give the upper limit of your range")
print("Now ! give the upper limit of your range")

upper = my_order()

number_to_be_guessed = random.randint(int(lower), int(upper))

#print(number_to_be_guessed)

no_of_guesses=0

read_text("your guess")
print("your guess")

while no_of_guesses < 5:
    no_of_guesses += 1
    
    guess = my_order()
    
    if int(guess)>int(upper) or int(guess)<int(lower):
        print("\nYour number is \nout of range")
        read_text("your guess is out of range. try again")

    elif number_to_be_guessed > int(guess):
        print("\nyour guess is \nsmaller than number")
        read_text("your guess is smaller than the number. try again")
    
    elif number_to_be_guessed == int(guess):
        print("WINNER!")
        read_text("Yay! you have won the game. congratulations")
        print("\nCongratulations you guessed the number in your ",no_of_guesses," try")
        break
      
    elif number_to_be_guessed < int(guess):
        print("\nyour guess is \nlarger than number")
        read_text("your guess is larger than the number. try again")

    else:
        print("There was some problem")
        break
           
if no_of_guesses >= 5:
    print("\nThe Correct answer was ", number_to_be_guessed)
    read_text("the correct answer was")
    read_text(number_to_be_guessed)
    print("\nLets hope you do better next time")





    
 