import cv2
import argparse
import time

from ultralytics import YOLO
import supervision as sv

def calculateFPS(prevTime):
    currentTime = time.time()
    fps = 1 / (currentTime - prevTime)
    return fps, currentTime

def parseArguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="YOLOv8 live")
    parser.add_argument("--webcam-resolution", default=(1280, 720), nargs=2, type=int)
    args = parser.parse_args()
    return args

def main():
    args = parseArguments()
    frameWidth, frameHeight = args.webcam_resolution
    print(frameWidth, frameHeight)

    cap = cv2.VideoCapture(2)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frameWidth)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frameHeight)

    model = YOLO("./yolov8_ping_pong.pt")

    boxAnnotator = sv.BoxAnnotator(
        thickness=2,
        text_thickness=2, 
        text_scale=1
    )

    prevTime = time.time()
    while True:
        ret, frame = cap.read()

        result = model(frame)[0]
        detections = sv.Detections.from_yolov8(result)

        frame = boxAnnotator.annotate(scene=frame, detections=detections)

        # Calculate FPS
        fps, prevTime = calculateFPS(prevTime)

        # Draw FPS on the frame
        cv2.putText(frame, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("YOLOv8", frame)

        # print(frame.shape)
        if (cv2.waitKey(30) == 27):
            break

if __name__ == "__main__":
    main()