import cv2
import mediapipe as mp
import keyboard as kb
import imutils
import playsound as p  
import time as t
import soundkey as s
l=[]
WINDOW_NAME="window" 
FRAME_WIDTH  = 1280
FRAME_HEIGHT =  920
i=1
 
THUMB_TIP = 4
INDEX_FINGER_TIP = 8
MIDDLE_FINGER_TIP = 12
RING_FINGER_TIP = 16
Z_THRESHOLD_PRESS = 1
m=['A','B','C','D','E','F','G','H','I','J','K','L']
VK = {
    'A': { 'x':50+30, 'y':200, 'w':80, 'h':300 },
    'B': { 'x':150+30, 'y':200, 'w':80, 'h':300 },
    'C': { 'x':250+30, 'y':200, 'w':80, 'h':300 },
    'D': { 'x':350+30, 'y':200, 'w':80, 'h':300 },
    'E': { 'x':450+30, 'y':200, 'w':80, 'h':300 },
    'F': { 'x':550+30, 'y':200, 'w':80, 'h':300 },
    'G': { 'x':650+30, 'y':200, 'w':80, 'h':300 },
    'H': { 'x':750+30, 'y':200, 'w':80, 'h':300 },
    'I': { 'x':850+30, 'y':200, 'w':80, 'h':300 },
    'J': { 'x':950+30, 'y':200, 'w':80, 'h':300 },
    'K': { 'x':1050+30, 'y':200, 'w':80, 'h':300 },
    'L': { 'x':1150+30, 'y':200, 'w':80, 'h':300 }
} 
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
def draw(img, x, y, z,):
    global a
    for k in VK:
        if ((VK[k]['x'] < x < VK[k]['x']+VK[k]['w']) and (VK[k]['y'] < y < VK[k]['y']+VK[k]['h']) and (z <= Z_THRESHOLD_PRESS)): 
            cv2.rectangle(img, (VK[k]['x'], VK[k]['y']), (VK[k]['x']+VK[k]['w'], VK[k]['y']+VK[k]['h']), (255,255,255), -1) 
            cv2.putText(img, f"{k}", (VK[k]['x']+20,VK[k]['y']+70),cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,0), 5, cv2.LINE_AA)
            for i in m:
                if k==i:
                    a=i
                    s.sound(a)
        else:
            cv2.rectangle(img, (VK[k]['x'], VK[k]['y']), (VK[k]['x']+VK[k]['w'], VK[k]['y']+VK[k]['h']), (0,255,0), 1) 
            cv2.putText(img, f"{k}", (VK[k]['x']+20,VK[k]['y']+70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,0), 4, cv2.LINE_AA)
 
def GODH():
    global a
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        img=imutils.resize(img,width=1350)
        img = cv2.flip(img, 1)
        if i==1:
            cv2.putText(img,"HI,GODWIN...",(910,100),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),2)
            cv2.putText(img,"WANT TO PLAY KEYBOARD",(200,80),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),2)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
 
        x = 0
        y = 0
        z = 0
        
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS) 
                try:
                    index_finger_tip = handLms.landmark[INDEX_FINGER_TIP]
                    x = int(index_finger_tip.x * FRAME_WIDTH)
                    y = int(index_finger_tip.y * FRAME_HEIGHT)
                    z = int(index_finger_tip.z * FRAME_WIDTH)
                    if (z <= Z_THRESHOLD_PRESS):
                        color = (0,0,255) 
                    else:
                        color = (255,255,255)
                    cv2.putText(img,"G", (x,y), cv2.FONT_HERSHEY_SIMPLEX,1,color, 1)
                except IndexError:
                    index_finger_tip = None
 
        draw(img, x, y, z)
 
        cv2.imshow("Godwin", img)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            cv2.destroyAllWindows()
            print(a)
            break

if __name__ == "__main__":
    GODH()
 
