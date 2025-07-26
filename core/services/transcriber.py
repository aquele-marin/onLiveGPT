import whisper

model = whisper.load_model("base")

def transcribe(filename):
    print(f"Transcribing... {filename}")
    result = model.transcribe(filename)
    print("Transcribed text:", result['text'])
    return result['text']
