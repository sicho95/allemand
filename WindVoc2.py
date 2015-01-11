#!/usr/bin/python
# -*- coding: utf-8 -*-


from tkinter import *

class FenetreVoc(Frame):

    def __init__(self, master=NONE):

        Frame.__init__(self, master)

        self.ConsigneTxt = StringVar()
        self.MotLabel = StringVar()
        self.Reponse = StringVar()
        self.Resultat = StringVar()

        #------------ Label contenant la consigne ancré au nord --------------#

        self.LabelInstr = Label(self.master, textvariable=self.ConsigneTxt)
        self.LabelInstr.pack(anchor = N,pady=4)

        #---------------------------------------------------------------------#

        #-------- Frame contenant les boites de textes ancré au nord ---------#

        FrameText = Frame(self.master)
        FrameText.pack(anchor = N, pady=6)

        LabelVoc = Label(FrameText, textvariable=self.MotLabel, width=40)
        LabelFleche = Label(FrameText, text="->")
        TextRep = Entry(FrameText, textvariable=self.Reponse, width=40)

        TextRep.bind('<Return>', self.event)

        LabelVoc.grid(row=0, column=0, padx=10)
        LabelFleche.grid(row=0, column=1, padx=2)
        TextRep.grid(row=0, column=2, padx=10)

        #---------------------------------------------------------------------#

        #-Label contenant le resultat ancré au nord donc sous la frame precedente-#

        LabelResult = Label(self.master, textvariable=self.Resultat)
        LabelResult.pack(anchor = N,pady=4)

        #-------------------------------------------------------------------------#


    def event(self, *args):
        self.Reponse.get()
        print(self.Reponse.get())


    def ChgConsigne(self, NewConsigne):
        self.ConsigneTxt.set(NewConsigne)
        self.LabelInstr.configure(textvariable = self.ConsigneTxt)
        self.LabelInstr.update_idletasks()

    def ChgMot(self, NewMot):
        self.MotLabel.set(NewMot)


