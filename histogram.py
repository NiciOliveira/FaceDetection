# Importing all necessary libraries
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
# Read the video from specified path
cam = cv2.VideoCapture("C:\\Users\\itaic\\Documents\\Graduação\\2019_2\\COMPUTAÇÃO GRAFICA\\TP1\\videoplayback.mp4")
 
try:
     
    # creating a folder named data
    if not os.path.exists('Hist'):
        os.makedirs('Hist')
 
# if not created then raise error
except OSError:
    print ('Error: Criação do diretorio Hist')
 
# frame
currentframe = 0
currentHist = 0
 
while(True):
     
    # reading from frame
    ret,frame = cam.read()
 
    if ret:
       
        file_name = './Hist/hist' + str(currentHist)+ 'frame' + str(currentframe) + '.jpg'
        print ('Criando imagem...' + file_name)
        # writing the extracted images
        cv2.imwrite(file_name, frame)


        mask = np.zeros(frame.shape[:2], np.uint8)
        mask[100:300, 100:400] = 255
        masked_img = cv2.bitwise_and(frame,frame,mask = mask)
        
        hist_full = cv2.calcHist([frame],[0],None,[256],[0,256])
        hist_mask = cv2.calcHist([frame],[0],mask,[256],[0,256])
        
        plt.subplot(221), plt.imshow(frame, 'gray')
        plt.subplot(222), plt.imshow(mask,'gray')
        plt.subplot(223), plt.imshow(masked_img, 'gray')
        plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
        plt.xlim([0,256])
        
        plt.savefig(file_name)
        
        currentframe += 1
        currentHist += 1
    else:
        break
 
# Release all space and windows once done
cam.release()
cv2.destroyAllWindows() 