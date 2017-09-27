import cv2, math, os, inspect, time

PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
PATH = PATH.replace('\\', '/')
imgPATH = PATH + "/Images/"
vidPATH = PATH + "/Videos/"

capture = cv2.VideoCapture(0)

# Frame rate per second (FPS)
framesPerSecond = capture.get(0)

# Changeable variable according to desired time
INITIAL = int(time.time())

while capture.isOpened():

    # Current frame number
    delta = int(time.time()) - INITIAL

    if delta >= 60:
        INITIAL = int(time.time())

    ret, frame = capture.read()

    print (delta)

    if not ret:
        break

    if (delta % 1 == 0):

        filename = imgPATH + "image_" + str(delta) + ".jpg"
        cv2.imwrite(filename, frame)

capture.release()