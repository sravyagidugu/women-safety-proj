import tensorflow as tf
import cv2
import numpy as np

# Load trained model
model = tf.keras.models.load_model('gender_classification/gender_model.h5')

def predict_gender(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (128, 128))
    image = np.expand_dims(image, axis=0) / 255.0

    prediction = model.predict(image)
    return "men" if prediction[0][0] > 0.5 else "Woman"

# Example Usage
print(predict_gender("OIP.jpg"))
