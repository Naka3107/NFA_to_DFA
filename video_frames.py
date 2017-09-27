import cv2, os, inspect, time

PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
PATH = PATH.replace('\\', '/')
imgPATH = PATH + "/Images/"
vidPATH = PATH + "/Videos/"

capture = cv2.VideoCapture(0)


# Record from live video
def record(limit, interval):

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

        if (delta % interval == 0):

            filename = imgPATH + "image_" + str(delta / interval) + ".jpg"
            cv2.imwrite(filename, frame)

    capture.release()

# record(6, 3)