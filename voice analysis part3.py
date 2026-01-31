import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import json
import pyttsx3
import datetime

# ---------------- LOAD VOSK MODEL ----------------
# Make sure the folder name is correct (e.g. "vosk-model-small-en-us-0.15")
model = Model("model")
recognizer = KaldiRecognizer(model, 16000)

# ---------------- AUDIO QUEUE ----------------
audio_queue = queue.Queue()

# ---------------- TEXT TO SPEECH ----------------
tts_engine = pyttsx3.init()
tts_engine.setProperty("rate", 150)

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# ---------------- AUDIO CALLBACK ----------------
def callback(indata, frames, time, status):
    if status:
        print(status)
    # RawInputStream already gives int16 bytes
    audio_queue.put(bytes(indata))

# ---------------- QUERY PROCESSING ----------------
def process_query(query):
    query = query.lower()

    if "time" in query:
        now = datetime.datetime.now().strftime("%H:%M")
        return f"The current time is {now}"

    elif "date" in query:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        return f"Today's date is {today}"

    else:
        return "I am sorry, I cannot understand that."

# ---------------- START ASSISTANT ----------------
print("🎤 Voice Assistant Started")
print("Say 'time', 'date' or 'exit'")
speak("Hello, I am ready to listen.")

# ---------------- MICROPHONE STREAM ----------------
with sd.RawInputStream(
    samplerate=16000,
    blocksize=8000,
    dtype="int16",
    channels=1,
    callback=callback
):
    while True:
        data = audio_queue.get()

        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text = result.get("text", "")

            if text:
                print("You said:", text)

                if text == "exit":
                    speak("Goodbye")
                    break

                response = process_query(text)
                print("Assistant:", response)
                speak(response)