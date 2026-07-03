# YOLO_Vision_System

# 🚀 VisionDetect AI - Object Detection using YOLO

## 📌 Project Overview

VisionDetect AI is a real-time object detection project developed using the YOLO (You Only Look Once) deep learning model and OpenCV. The system detects multiple objects in images and videos by drawing bounding boxes around detected objects along with their class names and confidence scores.

This project demonstrates how YOLO can be used for fast and accurate object detection in computer vision applications.

---

## ✨ Features

- Real-time object detection using YOLO
- Detects multiple objects simultaneously
- Displays object labels and confidence scores
- Supports image and video detection
- Uses OpenCV for visualization
- Fast and accurate inference

---

## 🛠️ Technologies Used

- Python
- YOLO (Ultralytics)
- OpenCV
- NumPy

---

## 📂 Project Structure

```
VisionDetect-AI/
│── Images/
│── Videos/
│── utils/
│   └── coco.txt
│── output/
│── yolo_check.py
│── yolov8_n_opencv.py
│── yolov8n.pt
│── requirements.txt
│── README.md
```

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/VisionDetect-AI.git
```

Move into the project directory:

```bash
cd VisionDetect-AI
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

For image detection:

```bash
python yolo_check.py
```

For video detection:

```bash
python yolov8_n_opencv.py
```

---

## 📸 Sample Output

The detected output images and videos are saved automatically in the output folder.

Each detected object includes:

- Bounding Box
- Object Label
- Confidence Score

---

## 📁 Dataset

This project uses the COCO dataset class names stored in:

```
utils/coco.txt
```

---

## 📌 Applications

- Smart Surveillance
- Traffic Monitoring
- Autonomous Vehicles
- Security Systems
- Retail Analytics
- Robotics

---

## 👩‍💻 Author

**Ankita Shendge**

---

## ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.
