
import cv2
from matplotlib import image
from numpy import result_type

from Gesture_Controller import Controller


gest_name = handmajor.get_gesture()
Controller.handle_controls(gest_name,handmajor.hand_result)
                    
for hand_landmarks in result_type.multi_hand_landmarks:
                 mp_drawing.draw_landmarks(image, hand_landmarks,mp_hands.HAND_CONNECTIONS)
else:
                    Controller.prev_hand = None
cv2.imshow('Gesture Controller', image)