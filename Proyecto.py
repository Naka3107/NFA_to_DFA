#coding: UTF-8
import detect_faces, info_analizer, list_faces, os, inspect, webbrowser, cognitive_face, time
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

        foto1 = PATH + "a1.jpg"
        foto2 = PATH + "a2.jpg"

        showImg1 = Image.open(foto1, 'r')
        showImg1.show()
        showImg2 = Image.open(foto2, 'r')
        showImg2.show()

        jsonFoto1 = foto1
        jsonFoto2 = foto2

        print jsonFoto1

    infoPhoto1 = detect_faces.readFace(jsonFoto1, isURL)
    infoPhoto2 = detect_faces.readFace(jsonFoto2, isURL)

    print infoPhoto1

    jsonList1 = {"name": "sample_list_1"}
    jsonList2 = {"name": "sample_list_2"}

    print "WOLOLOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
    print (int)(time.time() * 10)
    listId = (int)(time.time() * 10)
    # strId = (str) listId

    list1 = list_faces.createList()


    # print (list1)

    #print (infoPhoto2)
    #print (infoPhoto1)

    #cognitive_face.face_list.add_face(foto1,'{"faceListId":"pollo"}')

    #print("CARA:\n")
    #print(cognitive_face.face_list.get('{"faceListId":"pollo"}'))

    #cognitive_face.face.find_similars(infoPhoto1[0]['faceId']);
    #info_analizer.compare(infoPhoto1, infoPhoto2)

main()