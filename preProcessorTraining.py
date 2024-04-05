import cv2
import numpy as np
import os
from sklearn.model_selection import train_test_split

# Parameters
end_slide_videos_dir = '/Users/harrymoss/Library/CloudStorage/OneDrive-Personal/AI Content/Emedia AI Projects/Instagram Graph API/sadhguruReels/ReelsEndSlide'
no_end_slide_videos_dir = '/Users/harrymoss/Library/CloudStorage/OneDrive-Personal/AI Content/Emedia AI Projects/Instagram Graph API/sadhguruReels/ReelsNoEndSlide'
output_directory = '/Users/harrymoss/Library/CloudStorage/OneDrive-Personal/AI Content/Emedia AI Projects/End Slide Cutter/totalSet'
target_width, target_height = 64, 64
last_n_seconds = 2  # Extract frames from the last N seconds of the video

# Ensure output directory exists
os.makedirs(output_directory, exist_ok=True)

# Function to extract and preprocess frames from a directory of videos
def extract_and_preprocess_frames_from_dir(videos_dir, output_subdir):
    output_dir = os.path.join(output_directory, output_subdir)
    os.makedirs(output_dir, exist_ok=True)
    
    for video_file in os.listdir(videos_dir):
        # Skip files with non-video extensions
        if not video_file.lower().endswith(('.mp4', '.avi', '.mov')):
            continue
        
        video_path = os.path.join(videos_dir, video_file)
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print(f"Warning: Could not open video file {video_path}")
            continue

        fps = cap.get(cv2.CAP_PROP_FPS)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        start_frame = max(0, total_frames - int(fps * last_n_seconds))
        
        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.resize(frame, (target_width, target_height))
            frame = frame / 255.0  # Normalize pixel values
            output_path = os.path.join(output_dir, f"{video_file}_frame_{int(cap.get(cv2.CAP_PROP_POS_MSEC) / 1000)}.jpg")
            cv2.imwrite(output_path, frame * 255)  # Convert back for saving
        cap.release()

# Process videos with and without end slides
extract_and_preprocess_frames_from_dir(end_slide_videos_dir, 'withEndSlide')
extract_and_preprocess_frames_from_dir(no_end_slide_videos_dir, 'withoutEndSlide')

print("Frame extraction and preprocessing complete.")
