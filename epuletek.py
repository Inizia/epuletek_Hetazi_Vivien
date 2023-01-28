from Epulet import Epulet

elupletek_lista = []
def fajlbeolvas():
    epuletek_fajl = open("epulet.txt", "r", encoding="utf-8")
    epuletek_fajl.readline()
    lista = epuletek_fajl.readlines()
    epuletek_fajl.close()

    print(lista)

    i = 0
    while i < len(lista):
        sor = lista[i].strip().split("$")
        print(sor)
        elupletek_lista.append(Epulet(sor))
        i += 1
    print((elupletek_lista[2]).getmagassag())


def epuletek_szama():
    return len(elupletek_lista)


def magas_epuletek():
    i = 0
    darab = 0
    while i < len(elupletek_lista):
        if (elupletek_lista[i].getmagassag()) * 3.280839895 > 555:
            darab += 1
        i += 1
    return darab


def legoregebb():
    i = 0
    oregek = 0
    while i < len(elupletek_lista):
        if (elupletek_lista[oregek].epult) > elupletek_lista[i].epult:
            oregek = i
        i += 1
    return elupletek_lista[oregek].orszag