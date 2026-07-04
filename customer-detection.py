import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")      # or best.pt

# Webcam
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(r"C:\Users\Dell\VS_CODE_PROJECT\Object Detection using yolo model\Videos\video_sample2.mp4")

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    annotated_frame = results[0].plot()

    cv2.imshow("YOLOv8 Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()