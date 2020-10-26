#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici



# TODO: Définissez vos fonction ici
def compare_fichier(fichier1, fichier2):
    with open(fichier1, "r") as f, open(fichier2, "r") as p:
        c = f.read(1)
        k = p.read(1)
        while c != '' and k != '':
            if c != k:
                position = f.tell()
                print("la difference est à la position {position} entre {​​​​​c}​​​​​ et {​​​​​k}​​​​​")
                break
            c = f.read(1)
            k = p.read(1)

def nombre(fname):
    with open(fname, 'r') as f:
        donnees = f.read()
    liste_nombre = sorted([int(elem) for elem in donnees.split() if elem.isdigit()])
    print(liste_nombre)


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    compare_fichier("exemple.txt", "exemple2.txt")
    nombre("exemple.txt")
    pass
