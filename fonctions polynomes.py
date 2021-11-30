from math import *

def second_degrés(a,b,c):
    delta = b**2 - 4*a*c
    if delta < 0:
        texte = "il n'y a pas de solution pour l'equation"
    elif delta == 0:
        texte = "la solution de l'equation est : " + str(-b/2*a)
    elif delta > 0:
        texte = "les solutions de l'equation sont : " + str(-b-sqrt(delta)/2*a ) + " et " + str(-b+sqrt(delta)/2*a)
    print (texte)


second_degrés(-1,7,1)