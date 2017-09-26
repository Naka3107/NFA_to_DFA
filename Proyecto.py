import detect_faces, info_analizer

def main():
    foto1 = "http://vignette2.wikia.nocookie.net/vikingstv/images/7/78/Katheryn_Winnick.png/revision/latest?cb=20130405200728"
    foto2 = "http://warp.la/wp-content/uploads/2017/06/the-killers-2-e1485012869982.jpg"
    jsonFoto1 = "{'url':'" + foto1 + "'}"
    jsonFoto2 = "{'url':'" + foto2 + "'}"

    infoPhoto1 = detect_faces.readFace(jsonFoto1)
    infoPhoto2 = detect_faces.readFace(jsonFoto2)

    info_analizer.compare(infoPhoto1, infoPhoto2)

main()