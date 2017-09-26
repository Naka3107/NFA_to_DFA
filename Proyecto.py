#coding: UTF-8
import detect_faces, list_faces, os, inspect, webbrowser, cognitive_face, time
from PIL import Image

def main():
    isURL = False

    if isURL:
        # Change URL according to uses
        foto1 = "https://pbs.twimg.com/profile_images/902026418355290112/ZaPrOTYn_400x400.jpg"
        foto2 = "https://s-media-cache-ak0.pinimg.com/originals/bd/06/5f/bd065f6cd8635d4817e432d26d72bed7.jpg"

        webbrowser.open(foto1)
        webbrowser.open(foto2)

        jsonFoto1 = "{'url':'" + foto1 + "'}"
        jsonFoto2 = "{'url':'" + foto2 + "'}"
    else:
        PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        PATH = PATH.replace('\\', '/')
        PATH = PATH + "/Images/"

        foto1 = PATH + "b1.jpg"
        foto2 = PATH + "b2.jpg"

        showImg1 = Image.open(foto1, 'r')
        showImg1.show()
        showImg2 = Image.open(foto2, 'r')
        showImg2.show()

        jsonFoto1 = foto1
        jsonFoto2 = foto2

    infoPhoto1 = detect_faces.readFace(jsonFoto1, isURL)
    infoPhoto2 = detect_faces.readFace(jsonFoto2, isURL)

    id1 = infoPhoto1[0]['faceId']
    id2 = infoPhoto2[0]['faceId']

    print id1
    print id2

    # list1 = list_faces.run()

main()