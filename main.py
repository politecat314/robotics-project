from text_to_speech import text_to_speech
from speech_to_text import speech_to_text
from pygame import mixer
import time
from facial_emotion_analysis import face

# # text to speech
# text_to_speech.convert("hello world")

# # play audio
# mixer.init()
# mixer.music.load('audio-files/audio.mp3')
# mixer.music.play()
# while mixer.music.get_busy():  # wait for music to finish playing
#     time.sleep(1)


# speech_to_text.recognize("audio-files/preamble10.wav")

# speech_to_text.speak()


# face.live_emotion_detect()



# import the opencv library
import cv2
from deepface import DeepFace
  
# define a video capture object
vid = cv2.VideoCapture(0)

counter = 0

while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    ### added part start
    try:
        res = DeepFace.analyze(frame, actions=['emotion'])
        

        x = int(res['region']['x'])
        y = int(res['region']['y'])
        w = int(res['region']['w'] + x)
        h = int(res['region']['h'] + y)
        cv2.rectangle(frame, (x,y), (w,h), (0, 255, 0), 2)
        
        text = res['dominant_emotion']
        startY = y
        startX = x
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.putText(frame, text, (startX, y),
        cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

    except Exception as e: print(e)
    ### added part end

    # Display the resulting frame
    cv2.imshow('frame', frame)
    
    # custom if statement by aman
    if res is not None:
        counter += 1
    
    if counter == 20:
        time.sleep(5)
        print(res['dominant_emotion']) 
        # Draw rectangles around faces
        print(res)
        break
        # break


    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()