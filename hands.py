import cv2
import mediapipe as mp
import numpy as np
from helpers.overlay import overlayImage
from helpers.gesture import check_gesture

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


#Reading an image
img1 = cv2.imread('images/img.jpeg')
img1 = cv2.resize(img1, (300, 300))
img1_pos = (0,0)

#pointers
index_pointer = np.zeros((30, 30, 3), np.uint8)
thumb_pointer = np.zeros((30, 30, 3), np.uint8)
thumb_pointer[0:30,0:30] = (0, 0, 255) # Green in BGR format

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

    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        # mp_drawing.draw_landmarks(
        #     image,
        #     hand_landmarks,
        #     mp_hands.HAND_CONNECTIONS,
        #     mp_drawing_styles.get_default_hand_landmarks_style(),
        #     mp_drawing_styles.get_default_hand_connections_style())

        #Index Finger Coordinates
        index_x = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width)
        index_y = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height)

        #Thumb Finger Coordinates
        thumb_x = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * image_width)
        thumb_y = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * image_height)
        
        #Displaying index pointer
        try:
          image = overlayImage(index_pointer, image, (index_x-15, index_y-15))
        except Exception as e:
          pass

        #Displaying thumb pointer
        try:
          image = overlayImage(thumb_pointer, image, (thumb_x-15, thumb_y-15))
        except Exception as e:
          pass

        #Checking if gesture meets logic
        image, img1_pos = check_gesture(image, image_width, image_height, (index_x, index_y), (thumb_x, thumb_y), img1, img1_pos)

    

    #overlaying image
    dst = overlayImage(img1, image, img1_pos)

    # Flip the image horizontally for a selfie-view display.
    flipped_image = cv2.flip(dst, 1)

    cv2.imshow('MediaPipe Hands', flipped_image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()