import pyttsx3 
import operator
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

r = sr.Recognizer()
mic= sr.Microphone(device_index=1)
with mic as source:
    speak("Sir! what you want to calculate, example: 3 plus 3")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
query=r.recognize_google(audio)

speak(query)

def operators(op):
    return {
        '+' : operator.add,
        '-' : operator.sub,
        'x' : operator.mul,
        'divided' :operator.__truediv__,
        }[op]

def calculation(op1, oper, op2):
    op1,op2 = int(op1), int(op2)
    return operators(oper)(op1, op2)

print(calculation(*(query.split())))

speak("is equal to")
speak(calculation(*(query.split())))