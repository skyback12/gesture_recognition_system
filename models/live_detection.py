import cv2
from hand_gesture_model import create_cnn_model
import numpy as np

# Load the trained model
model = create_cnn_model((64, 64, 1))  # Replace with your input shape
model.load_weights('models/model_cnn.h5')

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Pre-process frame (grayscale, resize)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized_frame = cv2.resize(gray_frame, (64, 64))
    input_frame = np.expand_dims(resized_frame, axis=(0, -1))

    # Predict gesture
    prediction = model.predict(input_frame)
    gesture_class = np.argmax(prediction)

    # Display results
    cv2.putText(frame, f'Gesture: {gesture_class}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Gesture Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
