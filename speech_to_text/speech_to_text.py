import speech_recognition as sr

# initialize the recognizer
r = sr.Recognizer()

def recognize(audio_path):
    # open the file
    with sr.AudioFile(audio_path) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
        print(text, "(debug)")
    
    return text


def speak(time_to_speak=5):
    with sr.Microphone() as source:
        print("recording your voice")
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=time_to_speak)
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data)
        print(text)