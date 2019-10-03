import cv2 
import os 
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['figure.figsize'] = (360, 360)
  
cam = cv2.VideoCapture("C:\\Users\\itaic\\Documents\\Graduação\\2019_2\\COMPUTAÇÃO GRAFICA\\TP1\\videoplayback.mp4") 
  
face_cascade = cv2.CascadeClassifier('modelo/haarcascade_frontalface_default.xml')
try: 
      

    if not os.path.exists('Pessoas'): 
        os.makedirs('Pessoas') 
  

except OSError: 
    print ('Error: Criação de diretorio Pessoas') 

# frame 
currentframe = 0
  
while(True):
    ret,frame = cam.read() 
  
    if ret: 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
        )
        current_face = 0
        for (x,y,w,h) in faces:
            cropped_face = frame[y:y+h, x:x+w]
            file_name = "Pessoas/frame" + str(currentframe) + "face" + str(current_face) + ".jpg"
            cv2.imwrite(file_name, cropped_face)
            current_face += 1
            print ('Criando imagem', file_name)
        currentframe += 1
        
    else: 
        break
  
cam.release()
cv2.destroyAllWindows()

