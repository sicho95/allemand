#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import csv

def logiciel(exercice):

    point = 0

    if (exercice == 2):
        file = "voc.csv"
        fichier = open(file)
        reader = csv.reader(fichier)
        for row in reader:
            if (input("Traduisez "+row[0]+" : ") == row[1]):
                point = point + 1
                print("Bravo!!\n")
            else:
                print ("Vous vous êtes trompé.")
                print ("La bonne réponse était : "+row[1]+"\n")
                point = point
        print ("\nVous avez "+str(point)+" point(s) sur "+str(reader.line_num)+"\n")
    else:
        if (exercice == 1):
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

