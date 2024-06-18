# Importing required libraries
import numpy as np
import cv2

# Define trackbar callback functions:
# the control panel youll see on the right once the cod has run


def onTrack1(val):
    global hueLow
    hueLow = val
    # print('Hue Low',hueLow)


def onTrack2(val):
    global hueHigh
    hueHigh = val
    # print('Hue High',hueHigh)


def onTrack3(val):
    global satLow
    satLow = val
    # print('Sat Low',satLow)


def onTrack4(val):
    global satHigh
    satHigh = val
    # print('Sat High',satHigh)


def onTrack5(val):
    global valLow
    valLow = val
    # print('Val Low',valLow)


def onTrack6(val):
    global valHigh
    valHigh = val
    # print('Val High',valHigh)


# Create a window for trackbars:
width = 640
height = 360


cv2.namedWindow("myTracker", cv2.WINDOW_AUTOSIZE)
cv2.moveWindow("myTracker", int(width), 0)
"""
    cv2.namedWindow('myTracker'): 
    you are instructing OpenCV to create a window with the specified title.
    #### cv2.moveWindow('myTracker', width, 0):
    instructing OpenCV to move the "myTracker" window to the specified position on the screen.
    The width parameter determines the horizontal position,
    and 0 determines the vertical position,
    0 indicates that the window should be moved to the top of the screen.
"""

# Initialize the lower and upper bounds of HSV values:
hueLow = 0
hueHigh = 179
satLow = 0
satHigh = 255
valLow = 0
valHigh = 255

# Create trackbars for adjusting the HSV values
cv2.createTrackbar("Hue Low", "myTracker", 0, 179, onTrack1)
cv2.createTrackbar("Hue High", "myTracker", 179, 179, onTrack2)
cv2.createTrackbar("Sat Low", "myTracker", 0, 255, onTrack3)
cv2.createTrackbar("Sat High", "myTracker", 255, 255, onTrack4)
cv2.createTrackbar("Val Low", "myTracker", 0, 255, onTrack5)
cv2.createTrackbar("Val High", "myTracker", 255, 255, onTrack6)

"""
    #### cv2.createTrackbar('Hue Low','myTracker',0,179,onTrack1): 

 This line creates a trackbar named 'Hue Low' within the 'myTracker' window. The parameters are as follows:

   **Hue Low** : 
    The name or label of the trackbar.
    
   **myTracker** :
    The name of the window in which the trackbar should appear.
    
   **0**: 
    The initial value of the trackbar.
    
   **179**: 
    The maximum value of the trackbar.
    
   **onTrack1**: 
    The callback function that will be called when the trackbar value changes.
"""


while True:
    frame = cv2.imread("./2-1.jpg")
    frame = cv2.resize(frame, (width, height))
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerBound = np.array([hueLow, satLow, valLow])
    upperBound = np.array([hueHigh, satHigh, valHigh])
    myMask = cv2.inRange(frameHSV, lowerBound, upperBound)
    # myMask=cv2.bitwise_not(myMask)
    myObject = cv2.bitwise_and(frame, frame, mask=myMask)
    cv2.imshow("My Object", myObject)
    cv2.moveWindow("My Object", 0, int(height))
    cv2.imshow("My Mask", myMask)
    cv2.moveWindow("My Mask", int(width), height)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
