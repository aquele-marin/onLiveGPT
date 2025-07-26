from dotenv import load_dotenv
from core.audio.listener import wake_word_detected
from core.audio.recorder import record_audio
from core.services.transcriber import transcribe
from core.services.responder import ask_chatgpt
from core.views.speaker import speak_response
from core.views.display import print_response


def run():
    while True:
        if wake_word_detected():
            filename = record_audio()
            user_input = transcribe(filename)
            response = ask_chatgpt(user_input)
            speak_response(response)
            print_response(response)

if __name__ == "__main__":
    load_dotenv()
    run()