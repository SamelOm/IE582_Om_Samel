# YOLO (You Only Look Once) - Real-Time Object Detection

## Overview
YOLO (You Only Look Once) is a state-of-the-art real-time object detection system that processes images in a single pass, making it highly efficient and fast. It is widely used for applications such as surveillance, autonomous vehicles, and robotics.

## Key Benefits & Features

- **High Speed & Efficiency** – Processes images in real-time, making it ideal for live detection applications.
- **Single-Pass Detection** – Unlike traditional CNN-based models, YOLO detects objects in one go, improving speed and reducing computation.
- **High Accuracy** – Despite being fast, YOLO provides impressive accuracy in detecting multiple objects in a frame.
- **Flexibility** – Detects a wide range of objects in different environments with minimal modifications.
- **Optimized for Real-Time Applications** – Works well with webcams, drones, and embedded systems like Raspberry Pi and Jetson Nano.
- **Pre-trained & Custom Models** – Use pre-trained YOLO models (like YOLOv8) or train a custom model on specific datasets.


  ## Why Choose YOLOv11n?
- **Improved Efficiency** – YOLOv11n offers even faster inference times compared to previous versions, making it ideal for low-latency applications.
- **Higher Accuracy** – Enhanced model architecture leads to better precision in detecting small and occluded objects.
- **Lower Computational Cost** – Optimized neural network structure reduces GPU and CPU usage, making it suitable for edge devices.
- **Better Adaptability** – Fine-tuned algorithms enable seamless adaptation across diverse datasets and environments.
- **Enhanced Object Tracking** – Upgraded tracking mechanisms improve performance in real-time multi-object tracking scenarios.


 **Here are some performance metrics:**

![Screenshot 2025-02-12 at 11 36 06 AM](https://github.com/user-attachments/assets/847f7b23-5293-49ad-a3e6-c21f0c7e1a51)

![Screenshot 2025-02-12 at 11 34 14 AM](https://github.com/user-attachments/assets/e53bb1d2-ebbd-4204-af63-c876e2168c5b)

## Installation

To get started with YOLO, install the required dependencies:
```bash
pip install ultralytics opencv-python
```

## Usage
### Running YOLO for Real-Time Detection
```python
import cv2
import csv
from ultralytics import YOLO

# Load the trained YOLO model
model = YOLO("yolo11n.pt")  # Replace with your model path

# Open webcam
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Open CSV file for writing
with open("detections.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Class", "Confidence", "X_min", "Y_min", "X_max", "Y_max"])  # Header

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Run YOLO object detection
        results = model(frame)

        # Get detections from results
        for result in results:
            for box in result.boxes:
                x_min, y_min, x_max, y_max = box.xyxy[0].tolist()  # Bounding box
                confidence = box.conf[0].item()  # Confidence score
                class_id = int(box.cls[0].item())  # Class index
                class_name = model.names[class_id]  # Class name

                # Write detection to CSV
                writer.writerow([class_name, confidence, x_min, y_min, x_max, y_max])

        # Show the annotated frame
        annotated_frame = results[0].plot()
        cv2.imshow("YOLO Real-Time Object Detection", annotated_frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release camera and close windows
cap.release()
cv2.destroyAllWindows()

```

## Training a Custom YOLO Model
To train YOLO on a custom dataset, follow these steps:

```bash
yolo task=detect mode=train model=yolov8n.pt data=custom_dataset.yaml epochs=50
```

Or to train on a knownn data-set:
```bash
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

## To access the data generated by this code
a CSV file with the name "Detections.csv" will be generated which you can use to do analysis.

## Some Screenshots of the Setup while working:
 The Output:
![Screenshot 2025-02-12 at 12 13 56 PM](https://github.com/user-attachments/assets/42ee7937-72e6-4f0e-929d-627e6db7af41)

Data being generated:
![Screenshot 2025-02-12 at 12 14 13 PM](https://github.com/user-attachments/assets/6ba4a900-f249-4959-aead-49ecd8084795)

The data:
![Screenshot 2025-02-12 at 12 17 22 PM](https://github.com/user-attachments/assets/e1fd2ff7-bd7e-4820-9e42-ab9829a72c89)

## References
- [YOLO Documentation](https://docs.ultralytics.com/)
- [YOLO GitHub Repository](https://github.com/ultralytics/ultralytics)

## License
This project follows the open-source license provided by Ultralytics.

