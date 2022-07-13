from deepface import DeepFace
import cv2
import time

def live_emotion_analysis():
    # define a video capture object
    vid = cv2.VideoCapture(0)

    counter = 0

    while(True):
        res = None

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
            print("face emotion analysis complete! exiting now")
            time.sleep(5)
            # print(res['dominant_emotion']) 
            # Draw rectangles around faces
            # print(res)
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


    return res