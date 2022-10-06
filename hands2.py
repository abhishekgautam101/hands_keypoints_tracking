import cv2
import mediapipe as mp
import numpy as np
from helpers.cursor import Cursor

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cursor_obj = Cursor((0,0))

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    image_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH )
    image_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT )
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
      # Flip the image horizontally.
    image = cv2.flip(image, 1)

    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())

        #Index Finger Coordinates
        index_x = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width)
        index_y = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height)

        #Thumb Finger Coordinates
        thumb_x = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * image_width)
        thumb_y = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * image_height)

        #Ring Finger Coordinates
        ring_x = int(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x * image_width)
        ring_y = int(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y * image_height)
        
        #Little Finger Coordinates
        little_x = int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x * image_width)
        little_y = int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y * image_height)

        #Checking if gesture meets logic
        cursor_obj.move_cursor((index_x, index_y), (thumb_x, thumb_y), (ring_x, ring_y), (little_x, little_y))

    cv2.imshow('Webcam', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()