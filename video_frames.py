import cv2
import math

imagesFolder = "C:\Users\Santino\Cmanai\SemanaiNKOTB\Images"
cap = cv2.VideoCapture("C:\Users\Santino\Cmanai\SemanaiNKOTB\Videos\Video.mp4")
frameRate = cap.get(5) #frame rate
while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % math.floor(frameRate) == 0):
        filename = imagesFolder + "\image_" +  str(int(frameId)) + ".jpg"
        cv2.imwrite(filename, frame)
cap.release()
print "Done!"