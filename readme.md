# Auto Selfie Flask App

This is a Flask-based web application that uses OpenCV and MediaPipe to detect smiles and automatically take selfies. 

## Preview
<!--![IMG_20250218_111715](https://github.com/user-attachments/assets/d4d66fb7-8f1a-4ded-a745-8dafd0e6d714)-->
![vdo](https://github.com/user-attachments/assets/4351980a-cab4-4518-b70e-e95ea2b56e7f)


## Features
- Real-time webcam feed using OpenCV.
- Face detection with MediaPipe FaceMesh.
- Automatic selfie capture when a smile is detected.
- Flask web interface to view the video feed and selfies.

## Requirements
Make sure you have the following installed:

- Python 3.x
- Flask
- OpenCV
- MediaPipe

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/jhahemantx/smiley-app.git
   cd auto-selfie-flask
   ```

2. Install the dependencies:
   ```bash
   pip install flask opencv-python mediapipe
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Open a browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## File Structure
```
/auto-selfie-flask
│── static/
│   ├── selfie.jpg  # Stores captured selfie
│   ├── style.css  
│── templates/
│   ├── index.html  # Web interface
│── app.py          # Main Flask application
│── main.py          # Initial OpenCV code
│── README.md       # Project documentation
```

## How It Works
1. The app starts a webcam feed using OpenCV.
2. MediaPipe detects facial landmarks and calculates mouth width.
3. If a smile is detected (mouth width exceeds a threshold), a selfie is captured.



