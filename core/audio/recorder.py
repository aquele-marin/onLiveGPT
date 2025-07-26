import sounddevice as sd
import scipy.io.wavfile as wav
import os
from dotenv import load_dotenv
load_dotenv()

RECORD_SECONDS = int(os.getenv('RECORD_SECONDS', 5))  # Default to 5 seconds if not set

print(sd.query_devices(12))
def record_audio(filename="output.wav", fs=48000):
    print("Recording...")
    audio = sd.rec(int(RECORD_SECONDS * fs), samplerate=fs, channels=1, dtype='int16', device=12)
    sd.wait()
    wav.write(filename, fs, audio)
    print("Recording complete.")
    return filename