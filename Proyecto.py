#coding: UTF-8
import detect_faces, list_faces, video_frames, os, inspect, webbrowser, cognitive_face, time
from PIL import Image
from multiprocessing import Process

TOTAL_PHOTOS = 5

def function_1():

        PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        PATH = PATH.replace('\\', '/')
        PATH = PATH + "/Images/image_"

        basePhoto = ""

        photoNum = 0
        while True:
            comparablePhoto =  PATH + str(photoNum) + ".jpg"

            # showImg1 = Image.open(foto1, 'r')
            # showImg1.show()
            # showImg2 = Image.open(foto2, 'r')
            # showImg2.show()

            try:

                infoPhoto1 = detect_faces.readFace(comparablePhoto)
                # infoPhoto2 = detect_faces.readFace(foto2)

                print infoPhoto1
                # print infoPhoto2
                print "---------------------------------------------"

                id1 = infoPhoto1[0]['faceId']
                # id2 = infoPhoto2[0]['faceId']

                print id1
                # print id2

                print "YYYYYYYYYY"
                photoNum += 1

            except Exception as e:
                print "XXXXXXXXXX"
                print e.args

            if photoNum >= TOTAL_PHOTOS:
                photoNum = 0

            print photoNum


def function_2():
    video_frames.record(TOTAL_PHOTOS)

if __name__ == '__main__':
    p1 = Process(target = function_1())
    p1.start()
    p2 = Process(target = function_2())
    p2.start()