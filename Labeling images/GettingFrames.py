# In the name of God
# SMani24
import cv2
import os

for vidPath in os.listdir("./Video"): # Get all directories in "Video" folder
    typ = vidPath.split(".")[-1] # Get file extenstion
    
    if(typ != "mp4"):#Make sure it's a .mp4 file
        continue
    video = cv2.VideoCapture("./Video/" + vidPath)
    success, image = video.read()
    count = 0
    print(success)
    while success:
        # Save frame as an image
        cv2.imwrite(f"./images/{vidPath}_frame_{count}.jpg", image)
        
        # Read the next frame
        success, image = video.read()
        
        # Increment frame counter
        count += 1
    video.release()
