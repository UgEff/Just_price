import numpy as np
import random as rd
from tkinter import *



tirage=rd.randint(1,100)

while True:
    a=int(input("Entrer une valeur pour commencer le jeu:"))
    
    if a>100 or a<1:
        print("Valeur non comprise entre 1 et 100")
        continue
    if a==tirage:
        print("Bravo vous avez gagné")
        break
    if a>tirage:
        print("Non c'est moins")

    if a<tirage:
        print("Non c'est plus")


