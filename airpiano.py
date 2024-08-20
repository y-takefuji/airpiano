# original:https://github.com/pdhruv93/computer-vision/tree/main/fingers-count
# original is modified by takefuji
import mediapipe as mp
import cv2
import math
import numpy as np
import os,sys

Hands = mp.solutions.hands
Draw = mp.solutions.drawing_utils

class HandDetector:
    def __init__(self, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.hands = Hands.Hands(max_num_hands=max_num_hands, min_detection_confidence=min_detection_confidence,
                                   min_tracking_confidence=min_tracking_confidence)
    def findHandLandMarks(self, image, handNumber=0, draw=False):
        originalImage = image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # mediapipe needs RGB
        results = self.hands.process(image)
        landMarkList = []
        if results.multi_handedness:
            label = results.multi_handedness[handNumber].classification[0].label  # label gives if hand is left or right
            #account for inversion in cam
            if label == "Left":
                label = "Right"
            elif label == "Right":
                label = "Left"
        if results.multi_hand_landmarks:  # returns None if hand is not found
            hand = results.multi_hand_landmarks[handNumber] #results.multi_hand_landmarks returns landMarks for all the hands

            for id, landMark in enumerate(hand.landmark):
                # landMark holds x,y,z ratios of single landmark
                imgH, imgW, imgC = originalImage.shape  # height, width, channel for image
                xPos, yPos = int(landMark.x * imgW), int(landMark.y * imgH)
                landMarkList.append([id, xPos, yPos, label])
            if draw:
                Draw.draw_landmarks(originalImage, hand, Hands.HAND_CONNECTIONS)
        return landMarkList

handDetector = HandDetector(min_detection_confidence=0.7)
import musicalbeeps as mb
p=mb.Player(volume=0.5, mute_output=False)
from time import sleep

def main():
 if len(sys.argv)==2:
  cam=cv2.VideoCapture(sys.argv[1])
 else: cam = cv2.VideoCapture(0)
 while True:
    status, image = cam.read()
    image =cv2.flip(image,1)
    handLandmarks = handDetector.findHandLandMarks(image=image, draw=True)
    count=0
    thumb=0
    index=0
    middle=0
    ring=0
    little=0
    oct=0
    if(len(handLandmarks) != 0):

        if handLandmarks[4][1]+30 < handLandmarks[5][1]:     #Thumb
            count = count
        else:      
            thumb=1
            oct=1
        if handLandmarks[4][1]+70 < handLandmarks[5][1]:     #Thumb
            count = count+1
        else:      
            thumb=thumb+1
        if handLandmarks[8][2]+30 < handLandmarks[6][2]:     #Index
            count = count+1
        else:       
            index=1
        if handLandmarks[12][2]+30 < handLandmarks[10][2]:   #Middle
            count = count+1
        else:       
            middle=1
        if handLandmarks[16][2]+30 < handLandmarks[14][2]:   #Ring
            count = count+1
        else:       
            ring=1
        if handLandmarks[20][2]+30 < handLandmarks[18][2]:   #Little
            count = count+1
        else:       
            little=1
    cv2.putText(image, str(count), (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 0, 0), 25)
    cv2.imshow("result", image)
    cv2.moveWindow("result",10,10)
    cv2.setWindowProperty("result", cv2.WND_PROP_TOPMOST, 1)
    if cv2.waitKey(1) == ord('q'):
     cam.release()
     cv2.destroyWindow("result")
     break
    if count==4 and thumb==2: 
     p.play_note("A5",0.3)
     sleep(0.20)
    elif count==4 and thumb==1: 
     p.play_note("C5",0.3)
     sleep(0.20)
    elif count==4 and index==1: 
     p.play_note("D5",0.3)
     sleep(0.20)
    elif count==3 and index==1 and oct==1: 
     p.play_note("B5",0.3)
     sleep(0.20)
    elif count==4 and middle==1: 
     p.play_note("E5",0.3)
     sleep(0.20)
    elif count==3 and middle==1 and oct==1: 
     p.play_note("C6",0.3)
     sleep(0.20)
    elif count==4 and ring==1: 
     p.play_note("F5",0.3)
     sleep(0.20)
    elif count==3 and ring==1 and oct==1: 
     p.play_note("D6",0.3)
     sleep(0.20)
    elif count==4 and little==1: 
     p.play_note("G5",0.3)
     sleep(0.20)
    elif count==3 and little==1 and oct==1: 
     p.play_note("E6",0.3)
     sleep(0.20)

if __name__ == '__main__':
 main()
 os._exit(0) 

