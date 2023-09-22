import numpy as np
import random as rd
import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askinteger


root=tk.Tk()
root.withdraw() #permet de cacher la fenetre principale qui provient de tk.TK()
value=rd.randint(1,100)

while True:
    prompt=askinteger("Just Price","Input beetwenn 0 and 100 ") #on stock la valeur de l'utilisateur
    tk.messagebox.showinfo("Votre choix",f"{prompt}")

    if prompt is None:
        break
    if prompt>100 or prompt<1:
        tk.messagebox.showinfo("Erreur","Valeur non comprise entre 1 et 100")
        continue
    if prompt==value:
        tk.messagebox.showinfo("Bravo ","Bravo vous avez gagné")
        break
    if prompt>value:
        tk.messagebox.showinfo("Continue","Non c'est moins 👎")

    if prompt<value:
        tk.messagebox.showinfo("Continue","Non c'est plus 👍")

root.mainloop()