import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model

# Paths
model_input = '/Users/harrymoss/Library/CloudStorage/OneDrive-Personal/AI Content/Emedia AI Projects/End Slide Cutter/TEST STAGE/testInput'
model_output = '/Users/harrymoss/Library/CloudStorage/OneDrive-Personal/AI Content/Emedia AI Projects/End Slide Cutter/TEST STAGE/testOutput'
model_path = '/Users/harrymoss/Library/CloudStorage/OneDrive-Personal/AI Content/Emedia AI Projects/End Slide Cutter/best_model.h5'

# Ensure directories exist
os.makedirs(model_input, exist_ok=True)
os.makedirs(model_output, exist_ok=True)

# Load your pre-trained model
model = load_model(model_path)

def preprocess_frame(frame_path):
    frame = cv2.imread(frame_path)
    if frame is None:
        print(f"Warning: Could not load image {frame_path}")
        return None  # Return None if the image couldn't be loaded
    frame = cv2.resize(frame, (128, 128))  # Resize the frame
    frame = frame / 255.0  # Normalize pixel values
    return np.expand_dims(frame, axis=0)  # Add batch dimension


def classify_and_move_frames(input_dir, output_dir, model):
    for frame_file in os.listdir(input_dir):
        frame_path = os.path.join(input_dir, frame_file)
        frame = preprocess_frame(frame_path)
        if frame is None:  # Skip processing if the image couldn't be loaded
            continue
        prediction = model.predict(frame)
        
        # Assuming your model outputs a binary prediction
        if prediction[0] > 0.5:  # Threshold can be adjusted
            # Move frame to model_output if detected as endslide
            os.rename(frame_path, os.path.join(output_dir, frame_file))

# Assuming the preprocess and extraction part is done and frames are ready in model_input
classify_and_move_frames(model_input, model_output, model)

print("Frame classification and processing complete.")
