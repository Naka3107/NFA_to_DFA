import cv2, math, os, inspect, time

PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
PATH = PATH.replace('\\', '/')
imgPATH = PATH + "/Images/"
vidPATH = PATH + "/Videos/"

capture = cv2.VideoCapture(0)

INTERVAL = 3

# Record from live video
def record(limit):

    # Changeable variable according to desired time
    INITIAL = int(time.time())

    while capture.isOpened():

        # Current frame number
        delta = int(time.time()) - INITIAL

        if delta >= limit:
            INITIAL = int(time.time())

        ret, frame = capture.read()

        print (delta)

        if not ret:
            break

        if (delta % INTERVAL == 0):

            filename = imgPATH + "image_" + str(delta) + ".jpg"
            cv2.imwrite(filename, frame)

    capture.release()