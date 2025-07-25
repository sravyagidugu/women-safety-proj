import cv2
import mediapipe as mp

# Initialize MediaPipe Hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

def detect_gesture(image_path):
    # Load image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return False
    
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    # Debugging Output
    if results.multi_hand_landmarks:
        print("Hand detected! Checking for distress gesture...")
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Show the processed image with landmarks
        cv2.imshow("Detected Hand", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        print("✅ Distress Gesture Detected")
        return True
    else:
        print("❌ No hand detected. Try a clearer image.")
        return False

# Test with an image
print(detect_gesture("OIP.jpg"))
