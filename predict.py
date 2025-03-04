from ultralytics import YOLO
model = YOLO('yolov8x.pt')
model.predict(['hhh.png'], save=True)