#!/usr/bin/python
# -*- coding: utf-8 -*-

import All_Fr
import Fr_All

def Choix_Application(choix):
    """cette fonction permet de prentre une variable en entré, celle de var_choix
    permettant de définir quelle fonction appeler et donc quel exercice"""
    if choix == 1:
       #lance la fonction choix1
        All_Fr.lancer()
    elif choix == 2:
        #lance la fonction choix2
        Fr_All.lancer()
