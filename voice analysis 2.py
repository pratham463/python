import pyaudio
import numpy as np
import speech_recognition as sr
import matplotlib.pyplot as plt
RATE = 16000
CHUNK = 1024
def record(sec, msg):
    print(msg)
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK
    )
    frames = [
        stream.read(CHUNK, exception_on_overflow=False)
        for _ in range(int(RATE / CHUNK * sec))
    ]
    stream.close()
    p.terminate()
    return b"".join(frames)

def analyze(audio):
    s = np.frombuffer(audio, np.int16)
    return len(s) / RATE, np.mean(abs(s)), np.max(abs(s)), s

def speech_to_text(audio):
    try:
        r = sr.Recognizer()
        return r.recognize_google(sr.AudioData(audio, RATE, 2))
    except:
        return ""
def speech_to_text(audio):
    try:
        r = sr.Recognizer()
        return r.recognize_google(sr.AudioData(audio, RATE, 2))
    except:
        return "Could not transcribe"

def show(a1, a2):
    plt.plot(a1, label="Recording 1")
    plt.plot(a2, label="Recording 2")
    plt.legend()
    plt.show()
audio1 = record(3, "Speak normally...")
audio2 = record(3, "Speak louder/faster...")
d1, avg1, max1, s1 = analyze(audio1)
d2, avg2, max2, s2 = analyze(audio2)
print("\n--- RESULTS ---")
print("R1:", d1, avg1, max1)
print("R2:", d2, avg2, max2)
print("Text 1:", speech_to_text(audio1))
print("Text 2:", speech_to_text(audio2))
show(s1, s2)