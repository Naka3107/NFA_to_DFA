def main():
    alphabet = []
    estados = []
    entrada = []
    f=open('prueba.txt','r')
    nfa=f.read()
    nfa=nfa[2:-2]
    h = nfa.split("),(")
    for i in h:
        entrada.append(i.split(","))
    for j in entrada:
        if (j[0] not in alphabet):
            alphabet.append(j[0])
        if (j[1] not in estados):
            estados.append(j[1])
        if (j[2] not in estados):
            estados.append(j[2])
    dfa = [None] * (2 ** (len(estados)) - 1)
    print entrada
    print h
    print dfa



##def generarDFA(nfa):

main()