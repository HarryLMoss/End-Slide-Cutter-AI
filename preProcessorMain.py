import cv2
import numpy as np
import os
from collections import defaultdict

# Parameters
test_videos_dir = '/Users/harrymoss/Library/CloudStorage/OneDrive-Personal/AI Content/Emedia AI Projects/Instagram Graph API/sadhguruReels/Reels'
output_directory = '/Users/harrymoss/Library/CloudStorage/OneDrive-Personal/AI Content/Emedia AI Projects/End Slide Cutter/FINAL STAGE/modelInput'
processed_videos_log = '/Users/harrymoss/Library/CloudStorage/OneDrive-Personal/AI Content/Emedia AI Projects/End Slide Cutter/FINAL STAGE/processedVideos.txt'
target_width, target_height = 128, 128
start_offset_seconds = 6
end_offset_seconds = 2
frames_to_extract = 100

# Ensure output directory exists
os.makedirs(output_directory, exist_ok=True)

# Initialize or load the log of processed videos
if os.path.exists(processed_videos_log):
    with open(processed_videos_log, 'r') as file:
        processed_videos = set(file.read().splitlines())
else:
    processed_videos = set()

# Auto-populate the processed_videos set based on existing output files
existing_files = os.listdir(output_directory)
video_names_from_files = {file.split('_frame_')[0] for file in existing_files if '_frame_' in file}
processed_videos.update(video_names_from_files)

# Update the log file accordingly
with open(processed_videos_log, 'w') as file:
    for video_name in processed_videos:
        file.write(f"{video_name}\n")

def extract_specific_number_of_frames(video_path):
    # Frame extraction logic remains the same
    # Omitted for brevity

def extract_and_preprocess_frames_from_test_dir(videos_dir):
    for video_file in os.listdir(videos_dir):
        video_name = os.path.splitext(video_file)[0]
        if not video_file.lower().endswith(('.mp4', '.avi', '.mov')) or video_name in processed_videos:
            continue  # Skip non-video files or already processed videos
        
        video_path = os.path.join(videos_dir, video_file)
        if extract_specific_number_of_frames(video_path):
            print(f"Successfully extracted frames from {video_file}")
        else:
            print(f"Failed to extract frames from {video_file}")

# Process test videos
extract_and_preprocess_frames_from_test_dir(test_videos_dir)

print("Frame extraction and preprocessing for all videos complete.")
