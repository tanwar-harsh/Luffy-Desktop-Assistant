import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def my_order():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("-Listening-")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("-Recognizing-")    
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:   
        print("Say that again please...")  
        return "None"
    return query    

print ("BMI Calculator")
speak("Bmi Calculator")

speak("tell me your height in centimeters")
print("tell me your height in centimeters")

height= my_order()

height_in_m= int(height)/100

speak("tell me your weight")
print("tell me your weight")

weight= my_order()

bmi=int(weight)/(height_in_m)**2

print("Your BMI is ",bmi)

if bmi<18.5:
    print("You are Under weight")
    speak("You are Under weight!")
elif 18.5<bmi<25:
    print("You are Noraml weight")
    speak("You are Noraml weight!")
elif 25<bmi<30:
    print("You are Over weight")
    speak("You are Over weight!")
elif 30<bmi:
    print("You are obese")
    speak("You are obese!")
else:
    print("An Error occured due to wrong input format")
    print("try giving integer values only")
    speak("Error Occured")