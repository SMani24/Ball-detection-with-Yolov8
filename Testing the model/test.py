import cv2
import argparse
import time
import os
import pandas as pd

from ultralytics import YOLO
import supervision as sv


def parseArguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="YOLOv8 live")
    parser.add_argument("--webcam-resolution", default=(1280, 720), nargs=2, type=int)
    args = parser.parse_args()
    return args

def main():
    for vidPath in os.listdir("./Video"): # Get all directories in "Video" folder
        results = pd.DataFrame(index=["Detected", "Not Detected"], columns=["Ball in frame", "Ball not in frame", "Half ball"]) 
        results["Ball in frame"]["Detected"] = 0
        results["Ball not in frame"]["Detected"] = 0
        results["Half ball"]["Detected"] = 0
        results["Ball in frame"]["Not Detected"] = 0
        results["Ball not in frame"]["Not Detected"] = 0
        results["Half ball"]["Not Detected"] = 0  
        video = cv2.VideoCapture("./Video/" + vidPath)
        success, frame = video.read()
        while success:
             
            model = YOLO("./yolov8_ping_pong.pt")

            boxAnnotator = sv.BoxAnnotator(
                thickness=2,
                text_thickness=2, 
                text_scale=1
            )
            result = model(frame)[0]
            detections = sv.Detections.from_yolov8(result)

            detectedFrame = boxAnnotator.annotate(scene=frame, detections=detections)


            # cv2.imshow("Og frame", frame)
            cv2.imshow("Detected", detectedFrame)

            while True:
                # print(frame.shape)
                a = cv2.waitKey(30)
                print(a)
                if (a == 113):
                    success = False
                    break
                if (a == 49):
                    results["Ball in frame"]["Detected"] += 1
                    break
                if (a == 50):
                    results["Ball not in frame"]["Detected"] += 1
                    break
                if (a == 51):
                    results["Half ball"]["Detected"] += 1
                    break
                if (a == 52):
                    results["Ball in frame"]["Not Detected"] += 1
                    break
                if (a == 53):
                    results["Ball not in frame"]["Not Detected"] += 1
                    break
                if (a == 54):
                    results["Half ball"]["Not Detected"] += 1
                    break
            success, frame = video.read()
        results.to_csv(vidPath + ".csv")
    

    

if __name__ == "__main__":
    main()