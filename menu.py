#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from Application import Choix_Application


MonMenu = Tk() #création de la fenetre MonMenu
MonMenu.title("Menu - Allemand") #définition du titre de la fenetre

var_choix = IntVar() # création d'une variable de type integer
choix = IntVar()

#-------- Frame contenant les radioboutons ancré au nord -------------#
FrameRadio = Frame(MonMenu)
FrameRadio.pack(anchor = N, pady=6)

Choix1 = ttk.Radiobutton(FrameRadio, text="Vocabulaire Allemand -> Français", variable=var_choix, value=1) 
Choix2 = ttk.Radiobutton(FrameRadio, text="Vocabulaire Français -> Allemand", variable=var_choix, value=2)

Choix1.pack(anchor = W)
Choix2.pack(anchor = W)
#---------------------------------------------------------------------#

def Application():
    Choix_Application(var_choix.get())

#----------- Frame contenant les boutons ancré au sud ----------------#
FrameBoutons = Frame(MonMenu)
FrameBoutons.pack(anchor = S, pady=7)

BoutonQuitter = ttk.Button(FrameBoutons, text="Quitter", command=MonMenu.quit)
BoutonOk = ttk.Button(FrameBoutons, text="    Ok    ", command=Application)

BoutonOk.grid(row=0, column=0, ipadx=10, padx=10)
BoutonQuitter.grid(row=0, column=1, ipadx=10, padx=10)
#---------------------------------------------------------------------#

MonMenu.mainloop()
