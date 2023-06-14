import cv2
import numpy as np
import os
import tensorflow as tf


def decode_prediction(y_hat):
    maps = ['Angry', "Happy", "Sad"]
    maxs = np.argmax(y_hat, axis=1)
    decoded_emotions = []
    for m  in maxs:
        decoded_emotions.append(maps[m])
    decoded_emotions = np.array(decoded_emotions).reshape(-1,1)
    return decoded_emotions



cam = cv2.VideoCapture(0)
model = tf.keras.models.load_model("model.h5")
font = cv2.FONT_HERSHEY_SIMPLEX
  
# org
org = (50, 50)
  
# fontScale
fontScale = 1
   
# Blue color in BGR
color = (255, 0, 0)
  
# Line thickness of 2 px
thickness = 2

while 1:
    # os.system('cls')
    _, frame = cam.read()
    frame = cv2.flip(frame,1)
    resized = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # print(frame.tolist())
    resized = cv2.resize(resized, (256, 256))
    array = np.expand_dims(np.array(resized.tolist())/255,0)
    pred = decode_prediction(model.predict(array))[0][0]
    print(array, pred)
    cv2.putText(frame, pred, org, font, 
                   fontScale, color, thickness, cv2.LINE_AA)
    
    # cv2.imshow("Camera Capture", frame)
    cv2.waitKey(200)