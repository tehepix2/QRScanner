print("Importing libraries...")
import time
import os
import signal
import cv2
import numpy as np
from pyzbar.pyzbar import decode

print("Opening text file...")
A = open("data.txt", "a")
B = os.startfile('data.txt')

def decoder(image):
    gray_img = cv2.cvtColor(image,0)
    qrCode = decode(gray_img)

    for obj in qrCode:
        points = obj.polygon
        (x,y,w,h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

        raw_qrData = obj.data.decode("utf-8").split()
        f = open("data.txt", "a")
        print("Writing to file...")
        for x in raw_qrData:
            try:
                int(x)
                f.write(x + " ")
            except:
                f.write(f'"{x}"' + " ")
        
        f.write("\n")
        os.system(f"taskkill /f /im notepad.exe")
        os.system("notepad.exe")
        f.close()

        time.sleep(1)






print("Activating camera...")
cap = cv2.VideoCapture(0)
print("Camera active")
while True:
    
    ret, frame = cap.read()
    decoder(frame)
    cv2.imshow('Image', frame)
    code = cv2.waitKey(10)
    if code == ord('q'):
        break
print("End of program")
os.system(f"taskkill /f /im notepad.exe")
A.close()
os.remove('data.txt')
