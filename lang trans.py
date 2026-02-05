import speech_recognition as sr
import pyttsx3
from googletrans import Translator

engine = pyttsx3.init()
engine.setProperty("rate", 150)

translator = Translator()

languages = {
    "1": "hi",
    "2": "ta",
    "3": "te",
    "4": "bn",
    "5": "mr",
    "6": "gu",
    "7": "ml",
    "8": "pa"
}
def speak(text):
    engine.say(text)
    engine.runAndWait()
def listen():
    r=sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("listening")
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("you said",text)
        return text
    except sr.UnknownValueError:
        print("error")
        return""
    except sr.RequestError as e:
        print("error of api",e)
        return""
print("\nchose a lang to trans")
print("1.hindi 2.telugu 3.tamil 4.bengali")
print("5.marathi 6.gujrati 7.malyalam 8.punjabi")
choice=input("enter choice(!-8)")
Lang= languages.get(choice)
if not Lang:
    print("invalid")
    exit()
text=listen()
if text:
    translated = translator.translate(text, dest=Lang)
    print("Translated Text:", translated.text)
    speak(translated.text)