# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:49:16 2020

@author: Elève
"""

# importation
from turtle import *


# ex 1
def puissance(x: float, n: int):
    if n == 0:
        return_val = 1
    else:
        return_val = x * puissance(x, n - 1)
    return return_val


def puissance_itt(x: float, n: int) -> float:
    return_val = x
    for i in range(n - 1):
        return_val *= x
    return return_val


"""la version récursive de puissance et plus compréhensible et se rapproche
d'un modèle mathématique concret. Cependant, la version récursive est
limité par l'espace d'empilement de python. A l'inverse la version
ittérative de puissance n'est quant à elle pas limité par python mais peut ne
pas faire apparaître de formule mathématique concrète.
"""


# ex 2
def mystere(n: int):
    if n<2:
        return_val = str(n)
    else:
        return_val = mystere(n // 2) + str(n % 2)
    return return_val

"""
mystère retourne l'équivalance de la valeur donnée en argument en binaire.
Le programme prend la valeur donnée en argument puis si celle si est inférieure
à 2 (soit 0 ou 1) alors cet valeur sera retournée sinon il s'agit de la
concaténation de mystere du quotient de la division euclydienne de la valeur
donnée en argument par 2 et du reste de la division euclidienne de la valeur
par 2. Ce systeme se répète jusqu'a n<2.
Cela marche car pour transposer en entier de la base 10 en base 2, on effectue
la division euclidienne du quotient précedent jusqu'à ce que le quoitient soit
inférieure strictement à 2 et on reprend tous les restes de bas en haut.
par exemple: mystere(2) retourne 10 car
2 est plus grand que 2 donc le programme retourne mystere(2 // 2) + str(2%2)
2//2 = 1
le programme cherche mystere(1): 1 plus petit que 2 donc mystere(1) retourne 1
maintenant le programme peut concaténer son résultat : 1
(mystere(2//21) = mystere(1)) + 0 (2%2 = 0)
donc le str retourner est 10
"""

# ex 3
couleurs = ["blue", "green", "yellow", "orange", "red", "purple"]
bgcolor('black')

def dessin() -> None:
    for i in range(180):
        color((couleurs[i % 6]))
        forward(i)
        right(69)

def new_dessin(n=0) -> None:
    color(couleurs[n % 6])
    if n == 179:
        forward(n)
    else:
        forward(n)
        right(69)
        new_dessin(n + 1)

# ex 4

class Citron:
    """classe de citron avec attributs:
        - taille
        - masse
    méthodes:
        - __init__, constructeur de la classe
        getteurs, qui permettent de donner l'accès au attributs en dehors de
        la classe:
            - get_size retourne la taille
            - get_weight reourne le poids

        - ajouter, qui ajoute une masse à la masse du citron
        - afficher, qui retourne un str qui décrit la classe
    """

    def __init__(self, taille: float, masse: float) -> None:
        self.size = taille
        self.weight = masse

    def get_size(self) -> float:
        return self.size

    def get_weight(self) -> float:
        return self.weight

    def ajouter(self, masse: float) -> None:
        self.weight += masse

    def afficher(self) -> str:
        return "taille : {}, poids : {}".format(
                self.get_size(),
                self.get_weight()
                )


def get_coef_com(a, b):
    coef = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
            61, 67, 71, 73, 79, 83, 89, 97]
    return [i
            for i in coef
            if (a % i == 0 and b % i == 0)
            ]



class Fraction:

    """classe qui représente une fraction
    attributs:
        - num, entier
        - denom, entier positif
    méthodes:
        - __init__, constructeur de la classe
        - get_num, retourne le numérateur
        - get_denom, retourne le dénominateur
        - afficher, qui affiche la fraction linéairement
    """

    def __init__(self, num: int, denom: int) -> None:
        assert isinstance(num, int), "num must be a int"
        assert isinstance(denom, int), "denom must a int"
        assert denom >= 0, "denom must be bigger than 0"
        a = get_coef_com(num, denom)
        self.num = num
        self.denom = denom
        if len(a) != 0:
            self.num /= a[-1]
            self.denom /= a[-1]

    def get_num(self) -> int:
        return self.num

    def get_denom(self) -> int:
        return self.denom

    def afficher(self) -> str:
        return "{}/{}".format(self.get_num(), self.get_denom())

    def egal_a(self, autre_frac) -> bool:
        return ((self.num * autre_frac.get_denom()) ==
                (self.denom * autre_frac.get_num()))

    def strict_inférieur_a(self, autre_frac) -> bool:
        return ((self.num * autre_frac.get_denom()) <
                (self.denom * autre_frac.get_num()))

    def somme(self, autre_frac):
        return Fraction((self.get_num() * autre_frac.get_denom() +
                         self.get_denom() * autre_frac.get_num()),
            (self.get_denom() * autre_frac.get_denom())
            )
    def produit(self, autre_frac):
        return Fraction((self.get_num() * autre_frac.get_denom()),
                        (self.get_denom() * autre_frac.get_denom()))


if __name__ == "__main__":
    # print("mystere(2) :" + mystere(2))
    ex = input("ex : ")
    print("\n")

    if ex == "1":
        x = 3
        n = 3
        print("x = " + str(x) + "n = " + str(n))
        print(puissance(x, n))
        print(puissance_itt(x, n))

    elif ex == "2":
        print(mystere(2))

    elif ex == "3":
        pu()
        goto(-150, 0)
        pd()
        dessin()
        pu()
        home()
        pu()
        goto(150, 0)
        pd()
        new_dessin()

    elif ex == "4":
        citron1 = Citron(223., 32.)
        print(citron1.afficher())
        citron1.ajouter(23)
        print(citron1.afficher())

    elif ex == "5":
        frac1 = Fraction(1, 3)
        frac2 = Fraction(5, 6)
        frac3 = Fraction(1, 3)
        frac4 = Fraction(2, 39)
        print(frac1.somme(frac2).afficher())
        print(frac1.produit(frac2).afficher())
        print(frac1.egal_a(frac3))
        print(frac2.strict_inférieur_a(frac4))
