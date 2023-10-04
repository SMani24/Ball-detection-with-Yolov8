import cv2
import supervision as sv
from ultralytics import YOLO

def main():
    frameCnt = int(input("Please enter the number of frames: "))
    sourceName = "1.mp4_frame_"
    step = 1
    filePath = "./Frames/" + sourceName
    model = YOLO("./yolov8_ping_pong.pt")
    for i in range(0, frameCnt, step):
        frame = cv2.imread(filePath + f"{i}.jpg")
        result = model(frame)[0]
        detections = sv.Detections.from_yolov8(result)
        frame = boxAnnotator.annotate(scene=frame, detections=detections)
        savePath = "./MarkedFrames/" + sourceName + f"{i}.jpg"
        cv2.imwrite(savePath, frame)
        
    model = YOLO("./yolov8_ping_pong.pt")
    model.predict(show=True, conf=0.5, source=filePath, conf=0.5, line_thickness=1)

if __name__ == "__main__":
    main()