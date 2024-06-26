# End Slide Cutter AI

****PLEASE NOTE: This project is still in progress, files are in the process of being uploaded as we speak. Please check other available projects on this [link.](https://github.com/HarryLMoss) Thank you for your patience.***

## Project Overview
This project focuses on developing a machine learning model capable of detecting and extracting end slides from video content. It utilizes TensorFlow and OpenCV for processing video frames and employs a pretrained VGG16 model for enhanced feature extraction. The goal is to accurately identify the transition to end slides in videos, enabling automated content editing and analysis.

## Features
- **Video Frame Extraction**: Processes videos to extract relevant frames for analysis, targeting specific time windows to optimise performance.
- **Deep Learning Model**: Leverages the VGG16 model for accurate end slide detection, trained on a custom dataset of video frames.
- **Efficiency Improvements**: Includes a system to avoid reprocessing videos, enhancing the usability of the system for iterative testing and development.
- **OpenAI**, for the GPT models that inspired aspects of our machine learning approach.
- **The JUCE Framework Team**, for their audio processing and GUI library, critical in developing our real-time music generation capabilities.
- **The Python Community**, for their extensive resources and forums, which were invaluable throughout the development process.
- **The C++ Community**, for their shared knowledge and resources on C++ programming, greatly assisting in the technical aspects of our project.
- **Ancient Scholars of Indian Classical Music**:

## Installation
Clone this repository to your local machine:
```bash
git clone https://github.com/harrylmoss/end-slide-detection.git
cd end-slide-detection
```
Ensure you have Python 3.x installed, and then install the required dependencies:

```bash
pip install -r requirements.txt
```
## Usage
First, preprocess the video content (ensuring to first change the directories to the correct location of video content in the python files beforehand) by running:

```bash
python preProcessorTraining.py
```

Now, in order to preprocess data before building the "_model".h file, run:

```bash
python preProcessorMain.py
```
To start processing videos and detecting end slides, run:

```bash
python modelRunning.py
```
Ensure your video files are placed in the designated testVideos directory as specified in the script parameters.

## Project Structure
modelRunning.py: The main script for processing videos, extracting frames, and running the detection model.
requirements.txt: Lists all the project dependencies for easy installation via pip.
best_model.h5: The pretrained TensorFlow model optimized for detecting end slides.

## Contributing
Contributions to improve the End Slide Detection System are welcome. Please follow these steps to contribute:

- Fork the repository.
- Create a new branch (git checkout -b feature-branch).
- Commit your changes (git commit -am 'Add some feature').
- Push to the branch (git push origin feature-branch).
- Create a new Pull Request.

## License
This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details.

## Acknowledgements
Special thanks to the TensorFlow and OpenCV communities for providing extensive documentation and resources that greatly assisted in this project's development.

## Contact
For any inquiries or collaboration requests, please contact me at harrymoss33@gmail.com.

Other AI/Digital Signal Processing projects can be found on my [GitHub Profile](https://github.com/HarryLMoss)

---

© 2024 Harry Moss. All Rights Reserved.
