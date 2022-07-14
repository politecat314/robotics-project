from text_to_speech import text_to_speech
from speech_to_text import speech_to_text
from pygame import mixer
import time
print("Importing required libraries. Please wait")
from facial_emotion_analysis import face
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import random
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


play_audio("hello.mp3") # robot introduces itself
print("How you are feeling today?")
play_audio("how_are_you.mp3") # first question robot asks

# speech to text
sentence = speech_to_text.speak()
print()
print("Your answer:", sentence)

sid = SentimentIntensityAnalyzer()
ss = sid.polarity_scores(sentence)
sentiment_score = ( (ss['compound'] + 1) / 2 ) * 100

print()
print()
print("We have analysed your answer. Next, we will analyse your face using the camera")
play_audio("face_analysis.mp3")

face_result = face.live_emotion_analysis()
print("Facial emotion analysis completed")
play_audio("facial_emotion_analysis_completed.mp3")

emotion = face_result['dominant_emotion']
emotion_score = face_result['emotion'][emotion]

final_score = 0

if emotion == 'angry' or emotion == 'sad':
    final_score = sentiment_score - 100 - emotion_score
    if final_score < 0:
        final_score = 0
elif emotion == 'happy':
    final_score = sentiment_score + emotion_score
else:
    final_score = sentiment_score
    final_score *= 2

final_percentage = round(final_score/2)

print("sentiment_score", sentiment_score, "%")
print("emotion_score", emotion_score, "% chance that you are", emotion)
print("Based on these 2 things, your current level of happiness is " + str(final_percentage) +  "%")

text_to_speech.convert(f"Based on your sentiment score and emotion score, we find that your happiness level is {str(final_percentage)} percent.", 
                        filename="final_result.mp3")
play_audio("final_result.mp3")

if final_percentage < 33.3: # feeling very depressed
    print("Since your happiness level is below 33.3 percent, we recommend seeking help from a therapist. Here is the number of a therapist: 0176")
    # text_to_speech.convert(f"Since your happiness level is below 33.3 percent, we recommend seeking help from a therapist. Here is the number of a therapist: 0176", 
    #                     filename="very_depressed.mp3")
    play_audio("very_depressed.mp3")

elif final_percentage < 66.6: # feeling moderate. Play a motivational quote
    quote = random.choice(motivational_quotes)
    print(f"Here is a motivational quote for you. {quote}")
    text_to_speech.convert(f"Here is a motivational quote for you. {quote}", 
                        filename="quote.mp3")
    play_audio("quote.mp3")
    
else: # feeling very happy today
    print(f"Congratulations! You seeem happy today. We hope you stay that way!")
    text_to_speech.convert(f"Congratulations! You seeem happy today. We hope you stay that way!", 
                        filename="happy.mp3")
    play_audio("happy.mp3")




# speech_to_text.speak()


