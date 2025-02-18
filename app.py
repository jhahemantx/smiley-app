# app.py
from flask import Flask, render_template, Response
import cv2
import mediapipe as mp
import os

app = Flask(__name__)

# Initialize MediaPipe FaceMesh
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
camera = cv2.VideoCapture(0)

# Ensure static folder exists
os.makedirs('static', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

def generate_frames():
    while True:
        success, img = camera.read()
        if not success:
            break
        
        # Flip image horizontally for selfie view
        img = cv2.flip(img, 1)
        
        # Convert to RGB for MediaPipe
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_img)
        
        if output.multi_face_landmarks:
            landmarks = output.multi_face_landmarks[0].landmark
            h, w, _ = img.shape
            
            # Get mouth landmarks
            x1 = int(landmarks[43].x * w)  # Left corner of mouth
            y1 = int(landmarks[43].y * h)
            x2 = int(landmarks[287].x * w)  # Right corner of mouth
            y2 = int(landmarks[287].y * h)
            
            # Calculate mouth width
            distance = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
            
            # Draw rectangle around mouth (for visualization)
            
            
            # If smiling, save the image
            if distance > 80:
                cv2.imwrite("static/selfie.jpg", img)
                # Draw text to indicate smile detected
                cv2.putText(img, "Smile Detected!", (50, 50), 
                          cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Convert frame to bytes for streaming
        ret, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                   mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug=True)