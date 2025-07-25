from gender_classification.predict_gender import predict_gender
from weapon_detection.detect_weapon import detect_weapon
from distress_gesture.detect_gesture import detect_gesture
from alert_system.send_alert import send_email_alert

image_path = "OIP.jpg"

if predict_gender(image_path) == "Woman":
    if detect_weapon(image_path) or detect_gesture(image_path):
        send_email_alert("Women Safety Alert", "Threat detected!", "lokanadam@gmail.com")
