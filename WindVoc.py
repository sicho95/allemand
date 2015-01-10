#!/usr/bin/python
# -*- coding: utf-8 -*-


from tkinter import *

class FenetreVoc(Frame):

    def __init__(self, master=NONE):

        Frame.__init__(self, master)

        self.Consigne()
        self.FrameExo()
        self.Result()


    def Consigne(self):
        #------------ Label contenant la consigne ancré au nord --------------#

        self.ConsigneTxt = StringVar()
        print("ma var consigne : "+self.ConsigneTxt.get())

        self.LabelInstr = Label(self.master, textvariable=self.ConsigneTxt)
        self.LabelInstr.pack(anchor = N,pady=4)

        #---------------------------------------------------------------------#

    def FrameExo(self):
        #-------- Frame contenant les boites de textes ancré au nord ---------#

        self.MotLabel = StringVar()
        self.Reponse = StringVar()

        FrameText = Frame(self.master)
        FrameText.pack(anchor = N, pady=6)


        LabelVoc = Label(FrameText, textvariable=self.MotLabel, width=40)
        LabelFleche = Label(FrameText, text="->")
        TextRep = Entry(FrameText, textvariable=self.Reponse, width=40)

        LabelVoc.grid(row=0, column=0, padx=10)
        LabelFleche.grid(row=0, column=1, padx=2)
        TextRep.grid(row=0, column=2, padx=10)

        TextRep.bind('<Return>', self.event)

        #---------------------------------------------------------------------#

    def Result(self):
        #-Label contenant le resultat ancré au nord donc sous la frame precedente-#

        self.Resultat = StringVar()

        LabelInstr = Label(self.master, textvariable=self.Resultat)
        LabelInstr.pack(anchor = N,pady=4)

        #-------------------------------------------------------------------------#

    def event(self, *args):
        return self.Reponse.get()

    def ChgConsigne(self, NewConsigne):
        self.ConsigneTxt.set(NewConsigne)
        self.LabelInstr.update_idletasks()

    def ChgMot(self, NewMot):
        self.MotLabel.set(NewMot)

