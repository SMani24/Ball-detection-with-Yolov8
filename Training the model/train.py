from ultralytics import YOLO

model = YOLO("yolov8m.pt")

model.train(task="detect", epochs=100, data="custom_data.yaml", imgsz=640)