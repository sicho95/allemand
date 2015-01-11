#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
from WindVoc2 import *
from tkinter import Tk

point = 0

def lancer():
    MonVoc = FenetreVoc(None)
    MonVoc.title("Allemand - Vocabulaire")
    newconsigne = "Traduisez le mot ou l'expression suivante du Français à l'Allemand"
    MonVoc.ChgConsigne(newconsigne)

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
