import  cvzone
import cv2

from cvzone.HandTrackingModule import HandDetector
hand_detector = HandDetector(maxHands=2,detectionCon=0.9,minTrackCon=0.9)
fpsReader = cvzone.FPS()
cap = cv2.VideoCapture(0)
while True:
    ret , img = cap.read()
    fps, image = fpsReader.update(img,pos=(30,80),color=(255,0,255),scale=3,thickness = 3)
    lms,image  = hand_detector.findHands(image)
    cv2.imshow("Image",image)
    cv2.waitKey(1)










