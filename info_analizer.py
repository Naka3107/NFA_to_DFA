#coding: UTF-8
exclude = ['[', ']', '{', '}', ',', ' ', '\"', '']

# Converts a JSON string into a matrix where each list is a person with usable values
def jsonToList(json):
    list = json.split("\n")
    matrix = []

    pos = -1

    for i in list:
        word = ''
        for char in i:
            if char not in exclude:
                word += char
        if word == "faceAttributes:":
            newList = []
            matrix.append(newList)
            pos += 1
        elif word != '' and not (word.endswith(':')):
            matrix[pos].append(word)

    return matrix

# Compares both photos and throws a matching percentage
def compare(list1, list2):
    newList1 = jsonToList(list1)
    newList2 = jsonToList(list2)



    print newList1
    print newList2