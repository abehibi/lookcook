import cv2

img = cv2.imread("lookcook-main/index_img_01.jpg")


if img is None:
    print("画像が読み込めません。ファイル名や場所を確認してください。")
    exit()

cv2.imshow("Neko no Gazo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

from ultralytics import YOLO

# YOLOv8モデルをロード
model = YOLO('yolov8.pt')  # モデルを指定（自分のモデルを使ってください）

# ONNX形式でエクスポート
model.export(format='onnx')
