from itertools import *
import os, inspect

nodos = []
estados = "{"

def main():
    global nodos, estados
    PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    PATH = PATH.replace('\\', '/')
    PATH = PATH + "/Textos/"
    try:
        for file in os.listdir(PATH):
            if file.startswith("respuesta"):
                os.remove(PATH+file)
            elif file.endswith(".txt"):
                nfa=PATH+file
        for linea in open(nfa,'r').readlines():
            nodes = set([])
            symbols = set([])
            flag = True
            while flag:
                if linea[-1] == "}":
                    flag = False
                    linea = linea[:-1]
                linea = linea[1:]
                nodos = new_nodes(linea)
                for n in nodos:
                    symbols.add(n[0])
                    nodes.add(n[1])
                    nodes.add(n[2])
                for c in list(powerset(nodes)):
                    for sy in symbols:
                        if (len(c) >= 1):
                            estados += "(" + str(sy) + ",{"
                            for comb in c:
                                estados += comb
                            estados += "}," + str(new_transitions(c, sy)) + "),"
                estados += "}"
            f=open(PATH+'respuesta.txt','w')
            f.write(estados)
            print "El DFA se guardo con exito."
    except NameError:
        print "No se encontro el archivo"


def new_nodes(linea):
    nodos = []
    n = 0
    f = 0
    for i in range(len(linea)):
        if linea[i] == "(":
            n = i + 1
        elif linea[i] == ")":
            f = i
            lista = []
            case = linea[n:f]
            case = case.split(',')
            lista.append(case[0])
            lista.append(case[1])
            lista.append(case[2])
            nodos.append(lista)
    return nodos


def new_transitions(comb, sym):
    transciones = []
    global nodos
    if (len(comb) == 1):
        for n in nodos:
            if (n[0] == sym and n[1] == comb[0]):
                transciones.append(n[2])
                return transciones
        for c in comb:
            for n in nodos:
                if (n[0] == sym and c == n[1]):
                    if (not (n[2] in transciones)):
                        transciones.append(n[2])
    else:
        for c in comb:
            for n in nodos:
                if (n[0] == sym and c == n[1]):
                    if (not (n[2] in transciones)):
                        transciones.append(n[2])

    return transciones


def powerset(set):
    l = list(set)
    return chain.from_iterable(combinations(l, r) for r in range(len(l) + 1))

main()