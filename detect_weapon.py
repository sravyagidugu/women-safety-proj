from ultralytics import YOLO
import cv2

# Load YOLOv8 model
model = YOLO('models/yolov8n.pt')  # Pre-trained model

def detect_weapon(image_path):
    results = model(image_path)

    # Show detected objects correctly
    for result in results:
        result.show()  # ✅ Correct way to display results

        for box in result.boxes:
            cls = result.names[int(box.cls)]  # Get class name
            if cls in ["knife", "gun"]:  # Modify as needed
                print(f"⚠️ Weapon detected: {cls}")
                return True

    return False

# Example Usage
print(detect_weapon("army.jpg"))
