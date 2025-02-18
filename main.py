import cv2
import mediapipe as mp
import pyautogui
import winsound

x1, x2, y1, y2 = 0, 0, 0, 0
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks = True)
camera = cv2.VideoCapture(0)


while True:
    _, img = camera.read()
    # cv2.imshow("auto-selfie", img)
    img = cv2.flip(img, 1)
    fh, fw, _ = img.shape

    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_img)
    landmark_points = output.multi_face_landmarks

    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks):
            x = landmark.x * fw
            y = landmark.y * fh
            if id == 43:
                x1, y1 = x, y
            if id == 287:
                x2, y2 = x, y
     
        dist = int (( (x2-x1)**2 + (y2-y1)**2 )**0.5)
        print(dist)
        if dist>80:
            cv2.imwrite("selfie.png", img)
            cv2.waitKey(100)

    cv2.imshow("auto-selfie", img)

    key = cv2.waitKey(100)
    if key == 27:
        break

camera.release()
cv2.destroyAllWindows()