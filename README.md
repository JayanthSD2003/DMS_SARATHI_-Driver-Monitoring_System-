# SARATHI - DMS - Driver Monitoring System 
SARATHI (Safety Assisted Responsive Automated Technology for Highway Independance)
## Using Python

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)                 

[![Python 3.12.5](https://img.shields.io/badge/python-3.12.5-blue.svg)](https://www.python.org/downloads/release/python-3125/) 
[![NumPy](https://img.shields.io/badge/numpy-1.26.1-blue)](https://pypi.org/project/numpy/)
[![Pygame](https://img.shields.io/badge/pygame-2.5.2-blue)](https://pypi.org/project/pygame/)
[![Imutils](https://img.shields.io/badge/imutils-0.5.1-blue)](https://pypi.org/project/imutils/)
[![OpenCV-Python](https://img.shields.io/badge/opencv--python-latest-blue)](https://pypi.org/project/opencv-python/)
[![SciPy](https://img.shields.io/badge/scipy-1.11.3-blue)](https://pypi.org/project/scipy/)
[![Dlib](https://img.shields.io/badge/dlib-19.24.2-blue)](https://pypi.org/project/dlib/)
[![OpenCV-Python Specific Version](https://img.shields.io/badge/opencv--python-4.8.1.78-blue)](https://pypi.org/project/opencv-python/4.8.1.78/)
[![Pyttsx3](https://img.shields.io/badge/pyttsx3-2.90-blue)](https://pypi.org/project/pyttsx3/)

[![VS Code](https://img.shields.io/badge/Made%20with-VS%20Code-0078d7.svg?logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
[![Made with Anaconda Navigator](https://img.shields.io/badge/Made%20with-Anaconda%20Navigator-green.svg)](https://docs.anaconda.com/anaconda/navigator/)
[![Powered by ChatGPT](https://img.shields.io/badge/Powered_by-ChatGPT-00A884.svg)](https://openai.com/chatgpt)


# Project Description:

## Technical Description

The SARATHI (Safety Assisted Responsive Automated Technology for Highway Independance) - Driver Monitoring System (DMS) leverages computer vision and machine learning to detect driver drowsiness in real-time using webcam video feeds. The system is constructed using several key technologies:

### Libraries and Modules:
- **OpenCV**: Utilized for video capture and image processing, including converting frames to grayscale and detecting faces.
- **dlib**: Employed for facial landmark detection, which pinpoints specific regions of the face, such as the eyes.
- **pygame**: Used to play an alert sound when drowsiness is detected.
- **pyttsx3**: A text-to-speech library that verbally alerts the driver to wake up.
- **SciPy**: Assists in calculating distances between facial landmarks to determine the eye aspect ratio (EAR).

### Eye Aspect Ratio (EAR):
The EAR is computed by detecting the coordinates of the eyes and calculating the distances between specific points. The formula is:

![EAR Formula](https://github.com/JayanthSD2003/DMS_SARATHI_-Driver-Monitoring_System-/blob/443c73525ccf421f63bfc9504dc062efe8ef1efd/EAR%20Formula.png)

where A and B are the vertical distances and C is the horizontal distance.

### Drowsiness Detection Logic:
- The system captures video frames continuously and flips them for correct orientation.
- Faces are detected within each frame using a combination of Haar cascades and dlib's face detector.
- Once faces are located, the eye aspect ratios for both eyes are calculated.
- If the EAR falls below a pre-defined threshold for a specified number of consecutive frames, the system triggers an audio alert via pygame and a verbal warning using pyttsx3.

### Program Flow:
1. **Initialization**: Libraries and the webcam are initialized, and configurations like speech rate for TTS are set.
2. **Main Loop**: The system reads frames, processes them to detect faces and eyes, and computes the EAR.
3. **Alert Mechanism**: If the EAR is below the threshold long enough, an audio alert and a verbal warning are triggered.
4. **Clean-Up**: Releases the video capture and closes all OpenCV windows when the program ends.

NOTE: Download the shape_predictor_68_face_landmarks.dat file from the following link:
  https://github.com/italojs/facial-landmarks-recognition/blob/master/shape_predictor_68_face_landmarks.dat

## Non-Technical Description

The Driver Monitoring System is designed to help drivers stay awake and alert while on the road. Here's how it works:

### Keeping an Eye on You
The system uses a webcam to watch the driver’s face in real-time. It looks for signs that the driver might be getting sleepy.

### Detecting Drowsiness
- **Seeing Your Eyes**: It can tell when your eyes are open or closed by measuring how open your eyes are.
- **Warning You**: If your eyes are closed for too long, indicating you might be falling asleep, it plays an alert sound and says "Wake up!" to grab your attention.

### Using Smart Technology
- **Video and Sound**: It combines video technology to watch your face and sound technology to alert you.
- **Continuous Monitoring**: It keeps checking your face and eyes as you drive to make sure you’re alert.

### Alert System
The system not only plays a sound to wake you up if you’re drowsy but also uses a voice alert saying "Wake up!" to ensure you don’t miss the warning.

This system is built using various technologies like computer vision for face and eye detection, sound alerts to wake you up, and a text-to-speech engine to provide voice warnings. It’s all about keeping drivers safe by ensuring they stay awake and alert while driving.

# Screenshots

## Testing, Development & Training

1. Test Image Eye:

  ![Test Image Eye](https://github.com/JayanthSD2003/DMS_SARATHI_-Driver-Monitoring_System-/blob/ee9de3bb8e5edd7062c137eb12d3c003dca2be68/Screenshots%20and%20Output%20Demo/Test%20image%20eye.png)

2. Test Webcam Eye:

  ![Test Webcam Eye](https://github.com/JayanthSD2003/DMS_SARATHI_-Driver-Monitoring_System-/blob/ee9de3bb8e5edd7062c137eb12d3c003dca2be68/Screenshots%20and%20Output%20Demo/Test%20webcam%20eye.png)

## Final Demo

1. Eye and Face Detect:

  ![Eye and face detect](https://github.com/JayanthSD2003/DMS_SARATHI_-Driver-Monitoring_System-/blob/ee9de3bb8e5edd7062c137eb12d3c003dca2be68/Screenshots%20and%20Output%20Demo/Eye%20and%20face%20detect.png)

2. Final Demo clip (click this image to download the demo video):

  [![Final Demo clip](https://github.com/JayanthSD2003/DMS_SARATHI_-Driver-Monitoring_System-/blob/097c3661322e480a4f9aeb3616dc5b57b15a362b/Screenshots%20and%20Output%20Demo/Eye%20and%20face%20detect.png)](https://github.com/JayanthSD2003/DMS_SARATHI_-Driver-Monitoring_System-/blob/097c3661322e480a4f9aeb3616dc5b57b15a362b/Screenshots%20and%20Output%20Demo/Screen%20Recording%202024-10-29%20180329.mp4)

