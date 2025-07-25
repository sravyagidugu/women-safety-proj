import os
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Set dataset path
train_dir = r"C:\Users\91830\Desktop\Women_Safety_Analytics\Women_Safety_Analytics\dataset\gender\train"
val_dir = r"C:\Users\91830\Desktop\Women_Safety_Analytics\Women_Safety_Analytics\dataset\gender\val"

# Create the model save directory if it doesn't exist
os.makedirs('models', exist_ok=True)

# Data Preprocessing
datagen = ImageDataGenerator(rescale=1./255)

# Load data
train_data = datagen.flow_from_directory(train_dir, target_size=(128, 128), batch_size=32, class_mode='binary')
val_data = datagen.flow_from_directory(val_dir, target_size=(128, 128), batch_size=32, class_mode='binary')

# Build CNN Model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the Model
model.fit(train_data, validation_data=val_data, epochs=10)

# Save Model
model.save('models/gender_model.h5')

print("Model saved successfully.")
