from ultralytics import YOLO

# YOLOv8の小さいモデルを読み込む（n = nano）
model = YOLO("yolov8n.pt")

# ONNX形式に変換して保存
model.export(format="onnx")
