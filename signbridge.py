#THE CODE IS CURRENTLY WORK IN PROGRESS#
#####INCOMPLETE#####

import cv2
import mediapipe as mp

# Setup MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

# Start Webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    gesture_text = "Show a Sign"

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lm = handLms.landmark

            # Detect Open Palm (Hello Sign)
            fingers_open = 0
            if lm[8].y < lm[6].y: fingers_open += 1  # Index
            if lm[12].y < lm[10].y: fingers_open += 1  # Middle
            if lm[16].y < lm[14].y: fingers_open += 1  # Ring
            if lm[20].y < lm[18].y: fingers_open += 1  # Pinky

            if fingers_open >= 4:
                gesture_text = "Hello"
            else:
                gesture_text = "Sign not recognized"

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

    # Show gesture text
    cv2.putText(img, gesture_text, (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    cv2.imshow("SignBridge", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
