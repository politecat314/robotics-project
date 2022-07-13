from text_to_speech import text_to_speech
from speech_to_text import speech_to_text
from pygame import mixer
import time
print("Importing required libraries. Please wait")
from facial_emotion_analysis import face
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os
print("Libraries import complete")

# os.system('clear') # linux
os.system('cls')

def play_audio(audio_filename):
    mixer.init()
    mixer.music.load(f"audio-files/{audio_filename}")
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)




motivational_quotes = ["Never let your memories be greater than your dreams.",
                        "Change the changeable, accept the unchangeable, and remove yourself from the unacceptable.",
                        "There is always risk, so learn to manage risk instead of avoiding it.",
                        "Act the way you want to be and soon you'll be the way you act.",
                        "Listen to the secret sound, the real sound, which is inside you.",
                        "A pessimist sees the difficulty in every opportunity; an optimist sees the opportunity in every difficulty.",
                        "Always seek out the seed of triumph in every adversity."]



# text to speech
# text_to_speech.convert("Facial emotion analysis completed", 
#                         filename="facial_emotion_analysis_completed.mp3")

# text_to_speech.convert("We have analysed your answer. Next, we will analyse your face using the camera", 
#                         filename="face_analysis.mp3")


# play_audio("hello.mp3") # robot introduces itself
# print("How you are feeling today?")
# play_audio("how_are_you.mp3") # first question robot asks

# speech to text
# sentence = speech_to_text.speak()
sentence = "I want to kill myself today"
print()
print("Your answer:", sentence)

sid = SentimentIntensityAnalyzer()
ss = sid.polarity_scores(sentence)
sentiment_score = ( (ss['compound'] + 1) / 2 ) * 100

print()
print()
print("We have analysed your answer. Next, we will analyse your face using the camera")
# play_audio("face_analysis.mp3")

face_result = face.live_emotion_analysis()
print("Facial emotion analysis completed")
# play_audio("facial_emotion_analysis_completed.mp3")

emotion = face_result['dominant_emotion']
emotion_score = face_result['emotion'][emotion]

final_score = 0

if emotion == 'angry' or emotion == 'sad':
    final_score = sentiment_score - emotion_score
elif emotion == 'happy':
    final_score = sentiment_score + emotion_score

print("sentiment_score", sentiment_score, "%")
print("emotion_score", emotion_score, "% chance that you are", emotion)
print("Based on these 2 things, your current level of happiness is", round(final_score/2), "%")

## TODO choose motivational quotes

# speech_to_text.speak()


