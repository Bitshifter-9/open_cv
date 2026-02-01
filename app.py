import cv2

face_cascade = cv2.CascadeClassifier(
    "/Users/pranavkumar.bandaram/Desktop/ml_prime/open_cv_learn/haarcascade_frontalface_default.xml"
)
eye_cascade = cv2.CascadeClassifier(
    "/Users/pranavkumar.bandaram/Desktop/ml_prime/open_cv_learn/haarcascade_eye.xml"
)
smile_cascade = cv2.CascadeClassifier(
    "/Users/pranavkumar.bandaram/Desktop/ml_prime/open_cv_learn/haarcascade_smile.xml"
)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        # Draw face rectangle
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Eye detection
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
        if len(eyes) > 0:
            cv2.putText(frame, "Eye detected", (x, y - 30),
                        cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 0), 2)

        # Smile detection
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 20)
        if len(smiles) > 0:
            cv2.putText(frame, "Smile detected", (x, y - 10),
                        cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 0, 0), 2)

    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()q
cv2.destroyAllWindows()
