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
