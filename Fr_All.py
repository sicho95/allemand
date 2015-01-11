#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import WindVoc2
from tkinter import Tk

point = 0

def lancer():
    MonVoc = Tk()
    MonVoc.title("Allemand - Vocabulaire")
    Mafenetre = WindVoc2.FenetreVoc(master=MonVoc)
    MonVoc.mainloop()
    newconsigne = "Traduisez le mot ou l'expression suivante du Français à l'Allemand"
    Mafenetre.ChgConsigne(newconsigne)

   #  file = "voc.csv"
   #  fichier = open(file)
   #  reader = csv.reader(fichier)
   #
   #
   # for row in reader:
   #      newmot = row[0]
   #      # if (input("Traduisez "+row[0]+" : ") == row[1]):
   #      #     point = point + 1
   #      #     print("Bravo!!\n")
   #      # else:
   #      #     print ("Vous vous êtes trompé.")
   #      #     print ("La bonne réponse était : "+row[1]+"\n")
   #      #     point = point
   #  print ("\nVous avez "+str(point)+" point(s) sur "+str(reader.line_num)+"\n")
