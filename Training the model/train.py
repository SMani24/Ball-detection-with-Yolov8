from multiprocessing import freeze_support
from ultralytics import YOLO

if __name__ == "__main__":
    freeze_support()
    model = YOLO("yolov8n.pt")

    model.train(task="detect", epochs=200, data="custom_data.yaml", imgsz=640)