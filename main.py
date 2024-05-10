import cv2
import numpy as np
from PoseEstimationModule import PoseEstimation as PoseEstimation
import time

cap = cv2.VideoCapture(0)
detector = PoseEstimation()
count = 0
dir = 0

while True:
    success,img = cap.read()
    # Resize the image
    img = cv2.resize(img, (1280, 720))
    img = detector.findPose(img,False)
    lmList = detector.findPosition(img,False)

    if len(lmList) != 0:#Right Arm
        angle = detector.findAngle(img, 12, 14, 16,pts = True, lines= True)
        per = np.interp(angle, (40, 180), (0, 100))
        print(per)
        
        # Check for the curls
        if per > 80:
            if dir == 0:
                count += 0.5
                dir = 1
        elif per < 25:
            if dir == 1:
                count += 0.5
                dir = 0

    cv2.putText(img, f'{int(per)}%', (30, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 3)
    cv2.putText(img, f'Count: {count}', (1000, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 3)
    cv2.rectangle(img,(50,100),(85,650),(255, 255, 0),2)
    cv2.rectangle(img,(55,110),(80,110+int(per*5.3)),(255,255,0),cv2.FILLED)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    #Exit when the video ends
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        break