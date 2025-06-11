'''
Download the model from the following link:
https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task
'''
import cv2
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np
# STEP 1: Import the necessary modules.
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

MARGIN = 10  # pixels
FONT_SIZE = 1
FONT_THICKNESS = 1
HANDEDNESS_TEXT_COLOR = (88, 205, 54) # vibrant green

def draw_landmarks_on_image(rgb_image, detection_result):
  hand_landmarks_list = detection_result.hand_landmarks
  handedness_list = detection_result.handedness
  annotated_image = np.copy(rgb_image)

  # Loop through the detected hands to visualize.
  for idx in range(len(hand_landmarks_list)):
    hand_landmarks = hand_landmarks_list[idx]
    handedness = handedness_list[idx]

    # Draw the hand landmarks.
    hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
    hand_landmarks_proto.landmark.extend([
      landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in hand_landmarks
    ])
    solutions.drawing_utils.draw_landmarks(
      annotated_image,
      hand_landmarks_proto,
      solutions.hands.HAND_CONNECTIONS,
      solutions.drawing_styles.get_default_hand_landmarks_style(),
      solutions.drawing_styles.get_default_hand_connections_style())

    # Get the top left corner of the detected hand's bounding box.
    height, width, _ = annotated_image.shape
    x_coordinates = [landmark.x for landmark in hand_landmarks]
    y_coordinates = [landmark.y for landmark in hand_landmarks]
    text_x = int(min(x_coordinates) * width)
    text_y = int(min(y_coordinates) * height) - MARGIN

    # Draw handedness (left or right hand) on the image.
    cv2.putText(annotated_image, f"{handedness[0].category_name}",
                (text_x, text_y), cv2.FONT_HERSHEY_DUPLEX,
                FONT_SIZE, HANDEDNESS_TEXT_COLOR, FONT_THICKNESS, cv2.LINE_AA)

  return annotated_image

# STEP 2: Create an HandLandmarker object.
base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
options = vision.HandLandmarkerOptions(base_options=base_options,
                                       num_hands=1)
detector = vision.HandLandmarker.create_from_options(options)

drawn_points = []
drawing = False

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()


while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
    detection_result = detector.detect(image)

    # Convert the MediaPipe Image to NumPy
    annotated_image = draw_landmarks_on_image(image.numpy_view(), detection_result)

    # Create a canvas to draw on (black transparent layer)
    draw_canvas = np.zeros_like(annotated_image)

    for hand_idx, hand_landmarks in enumerate(detection_result.hand_landmarks):
        # Index fingertip = landmark 8
        index_finger_tip = hand_landmarks[8]
        index_x = int(index_finger_tip.x * annotated_image.shape[1])
        index_y = int(index_finger_tip.y * annotated_image.shape[0])

        # Thumb tip = landmark 4
        thumb_tip = hand_landmarks[4]
        thumb_x = int(thumb_tip.x * annotated_image.shape[1])
        thumb_y = int(thumb_tip.y * annotated_image.shape[0])

        # Compute distance between index and thumb
        distance = np.hypot(index_x - thumb_x, index_y - thumb_y)

        # If distance is small (pinching), enable drawing
        if distance < 40:
            drawing = True
            drawn_points.append((index_x, index_y))
        else:
            drawing = False
            # Optional: Add blank line to break stroke
            drawn_points.append(None)

    # Draw points on canvas
    for i in range(1, len(drawn_points)):
        if drawn_points[i - 1] is None or drawn_points[i] is None:
            continue
        cv2.line(draw_canvas, drawn_points[i - 1], drawn_points[i], (255, 0, 255), 4)

    # Overlay the drawing on top of the annotated image
    combined = cv2.addWeighted(annotated_image, 1, draw_canvas, 1, 0)

    cv2.imshow('result', combined)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
