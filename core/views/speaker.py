import pyttsx3

def speak_response(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()