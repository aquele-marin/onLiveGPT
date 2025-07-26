import speech_recognition as sr
import os
from dotenv import load_dotenv

load_dotenv()

WAKE_WORD = os.getenv('WAKE_WORD', 'hey assistant').lower()

def wake_word_detected():
    recognizer = sr.Recognizer()
    # for i, mic_name in enumerate(sr.Microphone.list_microphone_names()):
    #     print(f"Microphone {i}: {mic_name}")

    with sr.Microphone(device_index=12) as source:
        print("Listening for wake word...")
        audio = recognizer.listen(source)
        try:
            phrase = recognizer.recognize_google(audio)
            print(f"Recognized phrase: {phrase}")
            return WAKE_WORD in phrase.lower()
        except sr.UnknownValueError:
            return False
