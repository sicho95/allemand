#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv

def lancer():
    point =0
    file = "voc.csv"
    fichier = open(file)
    reader = csv.reader(fichier)
    for row in reader:
        if (input("Traduisez "+row[1]+" : ") == row[0]):
            point = point + 1
            print("Bravo!!\n")
        else:
            print ("Vous vous êtes trompé.")
            print ("La bonne réponse était : "+row[0]+"\n")
            point = point
    print ("\nVous avez "+str(point)+" point(s) sur "+str(reader.line_num)+"\n")