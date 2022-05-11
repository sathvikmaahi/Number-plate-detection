import cv2
import numpy as np
import easyocr

numberplate_cascade = cv2.CascadeClassifier(r"F:\MY PROJECTS\NUMBER PLATE DETECTION\haarcascades\haarcascade_russian_plate_number.xml")

cap = cv2.VideoCapture(r'F:\MY PROJECTS\NUMBER PLATE DETECTION\video.mp4')

cap.set(3,480)
cap.set(4,360)

if (cap.isOpened() == False):
    print('Error Reading video')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    car_plates = numberplate_cascade.detectMultiScale(gray, scaleFactor=1.2,
                                                   minNeighbors=5)

    for (x, y, w, h) in car_plates:
        cv2.rectangle(frame, (x, y), (x + w, y + h),(255, 0, 0),2)
        plate = frame[y: y + h, x:x + w]


    if ret == True:
        cv2.imshow('Video', frame)
        cv2.imshow('roi',plate)
        reader = easyocr.Reader(['en'])
        results = reader.readtext(plate, paragraph="False")
        text = ''
        for result in results:
            text += result[1] + ''
        print(text)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break

    else:
        break



cap.release()
cv2.destroyAllWindows()