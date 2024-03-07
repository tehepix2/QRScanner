print("Importing libraries...")
import cv2
from time import sleep
import os

camera_id = 0
delay = 1
window_name = 'Scanner'

print("Starting detector...")
qcd = cv2.QRCodeDetector()
print("Starting Camera...")
cap = cv2.VideoCapture(camera_id)

print("Opening text file...")
A = open("data.txt", "a")
B = os.startfile('data.txt')

while True:
    ret, frame = cap.read()

    if ret:
        ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)
        if ret_qr:
            for s, p in zip(decoded_info, points):
                if s:
                    f = open("data.txt", "a")
                    
                    for obj in s:
                        f.write(str(obj).lstrip("[").rstrip("]"))
                    
                    f.write("\n")
                    os.system(f"taskkill /f /im notepad.exe")
                    os.startfile("data.txt")
                    f.close()
                    color = (0, 255, 0)
                    sleep(1)
                else:
                    color = (0, 0, 255)
                frame = cv2.polylines(frame, [p.astype(int)], True, color, 8)
        cv2.imshow(window_name, frame)
        
        

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break
    
print("End of program")
os.system(f"taskkill /f /im notepad.exe")
A.close()
os.remove('data.txt')
cv2.destroyWindow(window_name)
