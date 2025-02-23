# IoT-Based Surveillance Robot

## Overview
The **IoT-Based Surveillance Robot** is a web-controlled robot designed for real-time surveillance. It is powered by a Raspberry Pi 4B, utilizes a Pi Camera module for live streaming, and employs YOLOv5 for object detection and EasyOCR for text recognition, such as reading license plates. The robot can be controlled remotely via a web interface and stores captured images on Google Drive for further analysis.

## Screenshots

### Robot:
<img width="357" alt="image" src="https://github.com/user-attachments/assets/135208c2-b685-4ff5-93ca-57c12fb3ad83" />

<img width="344" alt="image" src="https://github.com/user-attachments/assets/36e2c345-cfb1-41e6-ba92-c9e4d7988c7b" />

<img width="348" alt="image" src="https://github.com/user-attachments/assets/09dc526a-46d2-426b-81fd-a303329dadb2" />

### Web Interface
<img width="472" alt="image" src="https://github.com/user-attachments/assets/2bbde185-31e3-43a8-93bc-29fafcc072a7" />

### Object Recognition

<img width="239" alt="image" src="https://github.com/user-attachments/assets/46ecd51e-f624-4c4c-a23d-301c358140e9" />

## Features
- **Live Video Streaming**: Streams real-time video to a web-based interface.
- **Remote Control**: Move the robot in any direction via the web UI.
- **Camera Movement**: Adjust the camera angle remotely.
- **Image Capture & Storage**: Captures images and stores them on Google Drive.
- **Object Detection**: Uses YOLOv5 for identifying objects in images.
- **License Plate Recognition**: Reads text from captured images using OCR.

## Hardware Requirements
- **Raspberry Pi 4B**
- **Pi Camera Module**
- **L298 Motor Driver**
- **DC Motors**
- **Servo Motor** (for camera movement)
- **Power Supply (9V Batteries & Power Bank)**

## Software Requirements
- **Python 3**
- **Flask** (for web server)
- **OpenCV** (for image processing)
- **YOLOv5** (for object detection)
- **EasyOCR / PyTesseract** (for text recognition)
- **Google Drive API** (for cloud storage)

## Usage
- Use the web UI buttons to move the robot forward, backward, left, or right.
- Adjust the camera angle via the interface.
- Click "Capture" to take an image and store it on Google Drive.
- Object detection and OCR processing can be triggered from the UI.

## Future Enhancements
- **Autonomous Navigation**: Implement AI-based path planning.
- **GPS Tracking**: Integrate GPS for remote tracking.
- **Sensor Integration**: Add temperature, pressure, and motion sensors.
- **Advanced AI Processing**: Improve YOLO model accuracy and introduce face recognition.

## Contributors
- **Jainil Patel** : https://github.com/Retr0-2211

