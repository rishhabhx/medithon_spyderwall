import cv2
import numpy as np
from tensorflow.keras.preprocessing import image
from keras.models import Sequential, model_from_json


# Step 1: Load model architecture from JSON file

from keras.saving import register_keras_serializable

@register_keras_serializable()
class Sequential(Sequential):
    pass

with open('Facial Expression Recognition.json', 'r') as json_file:
    model_json = json_file.read()

model = model_from_json(model_json, custom_objects={'Sequential': Sequential})


# Load weights
model.load_weights('fer.h5')


face_haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(0)

while True:
    ret, test_img = cap.read()  # captures frame and returns boolean value and captured image
    if not ret:
        continue
    gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

    faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)

    for (x, y, w, h) in faces_detected:
        cv2.rectangle(test_img, (x, y), (x + w, y + h), (255, 0, 0), thickness=7)
        roi_gray = gray_img[y:y + w, x:x + h]  # cropping region of interest i.e. face area from image
        roi_gray = cv2.resize(roi_gray, (48, 48))
        img_pixels = image.img_to_array(roi_gray)
        img_pixels = np.expand_dims(img_pixels, axis=0)
        img_pixels /= 255

        predictions = model.predict(img_pixels)

        # find max indexed array
        max_index = np.argmax(predictions[0])

        emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
        predicted_emotion = emotions[max_index]

        # Map emotions to pain levels
        pain_levels = {
            'angry': 'High Pain',
            'disgust': 'High Pain',
            'fear': 'Mild Pain',
            'sad': 'Mild Pain',
            'neutral': 'Low Pain',
            'happy': 'No Pain',
            'surprise': 'No Pain'
        }
        predicted_pain_level = pain_levels[predicted_emotion]
        print(predicted_pain_level)
        cv2.putText(test_img, predicted_pain_level, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    resized_img = cv2.resize(test_img, (1300, 800))
    cv2.imshow('Pain Level Estimation', resized_img)

    if cv2.waitKey(10) == ord('q'):  # wait until 'q' key is pressed
        break

cap.release()
cv2.destroyAllWindows()