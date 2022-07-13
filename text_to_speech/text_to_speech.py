from gtts import gTTS

def convert(text, filename="audio.mp3", path="audio-files"):
    tts = gTTS(text)
    tts.save(f"{path}/{filename}")
    print("audio recording saved (debug)")
