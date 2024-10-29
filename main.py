import time
import cv2
import dlib
import pygame
import pyttsx3  # Import the text-to-speech engine
from imutils import face_utils
from scipy.spatial import distance

# Initialize Pygame and load music
pygame.mixer.init()
pygame.mixer.music.load(r'D:\Projects\SARATHI\SARATHI_DMS_Driver_Drowsiness\audio\alert.wav')  #add the alert.wav file

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Set the speech rate (speed)

# Thresholds for drowsiness detection
EYE_ASPECT_RATIO_THRESHOLD = 0.25  # Increased the threshold to be more sensitive
EYE_ASPECT_RATIO_CONSEC_FRAMES = 25  # Reduced the number of consecutive frames
COUNTER = 0
ALERT_PLAYING = False  # To check if TTS is already speaking

# Load face cascade
face_cascade = cv2.CascadeClassifier(r"D:\Projects\SARATHI\SARATHI_DMS_Driver_Drowsiness\haarcascades\haarcascade_frontalface_default.xml") #add the haarcascade_frontalface_default.xml file

# Function to calculate eye aspect ratio
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    return (A + B) / (2 * C)

# Load face detector and predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(r'D:\Projects\SARATHI\SARATHI_DMS_Driver_Drowsiness\shape_predictor_68_face_landmarks.dat') #add the shape_predictor_68_face_landmarks.dat file

# Facial landmarks for eyes
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS['left_eye']
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS['right_eye']

# Start webcam video capture
video_capture = cv2.VideoCapture(0)

# Allow time for the camera to initialize
time.sleep(2)

while True:
    ret, frame = video_capture.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray, 0)
    face_rectangle = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in face_rectangle:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    for face in faces:
        shape = predictor(gray, face)
        shape = face_utils.shape_to_np(shape)

        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]

        leftEyeAspectRatio = eye_aspect_ratio(leftEye)
        rightEyeAspectRatio = eye_aspect_ratio(rightEye)

        eyeAspectRatio = (leftEyeAspectRatio + rightEyeAspectRatio) / 2

        # Debug: Print the eye aspect ratio
        print(f"Eye Aspect Ratio: {eyeAspectRatio:.2f}")

        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

        if eyeAspectRatio < EYE_ASPECT_RATIO_THRESHOLD:
            COUNTER += 1
            print(f"Drowsiness counter: {COUNTER}")  # Debug: Print counter value
            if COUNTER >= EYE_ASPECT_RATIO_CONSEC_FRAMES:
                if not pygame.mixer.music.get_busy():  # Check if the music is not already playing
                    pygame.mixer.music.play(-1)
                if not ALERT_PLAYING:  # If TTS is not already speaking, speak
                    engine.say("Wake up!")
                    engine.runAndWait()
                    ALERT_PLAYING = True
                print("You're drowsy, wake up!!")
                cv2.putText(frame, "You're drowsy, wake up!!", (150, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 2)
        else:
            pygame.mixer.music.stop()
            COUNTER = 0
            ALERT_PLAYING = False  # Reset TTS status when eyes are open

    cv2.imshow('Video', frame)

    # Check for 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and destroy windows
video_capture.release()
cv2.destroyAllWindows()
