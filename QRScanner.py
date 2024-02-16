import time
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import os

def decoder(image):
    gray_img = cv2.cvtColor(image,0)
    qrCode = decode(gray_img)

    for obj in qrCode:
        points = obj.polygon
        (x,y,w,h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

        raw_qrData = obj.data.decode("utf-8").strip()
        qrData = ' '.join(raw_qrData.split())
       
        f = open("data.txt", "a")
        f.write(qrData + "\n")
        f.close()

        time.sleep(2)

cap = cv2.VideoCapture(1)
while True:
    ret, frame = cap.read()
    decoder(frame)
    cv2.imshow('Image', frame)
    code = cv2.waitKey(10)
    if code == ord('q'):
        break

os.remove('data.txt')