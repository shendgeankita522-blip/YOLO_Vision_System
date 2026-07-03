# Install Ultralytics (Run once)
# pip install ultralytics

from ultralytics import YOLO
import ultralytics

# Check Ultralytics installation
ultralytics.checks()

# Load YOLO11 Nano model
# If not already downloaded, Ultralytics will download it automatically.
model = YOLO("yolo11n.pt")

# Perform object detection
results = model.predict(
    source=r"C:\Users\Dell\VS_CODE_PROJECT\Object Detection using yolo model\Images\1.jpg",
    conf=0.25,
    save=True,
    show=True,
    project=r"C:\Users\Dell\VS_CODE_PROJECT\Object Detection using yolo model",
    name="output",
    exist_ok=True
)

# Print where the output image is saved
print("\nPrediction completed successfully!")
print(f"Output folder: {results[0].save_dir}")

# Print the model location
print(f"Model loaded from: {model.ckpt_path}")