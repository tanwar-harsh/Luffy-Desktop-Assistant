import pyttsx3 
import operator
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

r = sr.Recognizer()
mic= sr.Microphone(device_index=1)
with mic as source:
    speak("what you want to calculate, example: 3 plus 3")
    print("what you want to calculate, example: 3 plus 3")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
query=r.recognize_google(audio)

print(query)
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

speak("is equal to")
speak(calculation(*(query.split())))
print("is equal to",calculation(*(query.split())))