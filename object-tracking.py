import cv2

print(cv2.__version__)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
print("Opened:", cap.isOpened())

cap.release()
import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Perform object tracking
    results = model.track(
        source=frame,
        persist=True,
        verbose=False
    )

    # Draw bounding boxes and tracking IDs
    annotated_frame = results[0].plot()

    # Show the frame
    cv2.imshow("YOLOv8 Object Tracking", annotated_frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()