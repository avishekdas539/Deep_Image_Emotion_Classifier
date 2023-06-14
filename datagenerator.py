import os
import cv2
import time

happy_path = "Data/happy"
sad_path = "Data/sad"
angry_path = "Data/angry"


if not os.path.exists("Data"):
    os.mkdir("Data")
    print("Data folder created.")
else:
    print("Data folder present.")



if os.path.exists(happy_path):
    os.mkdir(happy_path)
    print("happy folder created.")
else:
    print("happy folder present.")



if os.path.exists(sad_path):
    os.mkdir(sad_path)
    print("sad folder created.")
else:
    print("sad folder present.")




if os.path.exists(angry_path):
    os.mkdir(angry_path)
    print("angry folder created.")
else:
    print("angry folder present.")


number_of_sample_required = int(input("Enter number of sample required per category: "))

cam = cv2.VideoCapture(0)


for path, emo in [[happy_path, "Happy"], [angry_path, "Angry"], [sad_path, "Sad"]]:
    count = 0
    print(f"Please show {emo} face. Caputuring will start in 5 sec.")
    time.sleep(5)
    while True:
        _, frame = cam.read()
        frame = cv2.flip(frame, 1)
        # converted = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        filename = os.path.join(path, f"{count}.jpg")
        count+=1
        print(filename)
        cv2.imwrite(filename, frame)
        cv2.imshow("Angry", frame)
        cv2.waitKey(500)
        if count==number_of_sample_required:
            break