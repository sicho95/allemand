#!/usr/bin/python
# -*- coding: utf-8 -*-


from tkinter import *

class FenetreVoc(Tk):

    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.parent = parent
        self.creationfenetre()

    def creationfenetre(self):

        self.MotLabel = StringVar()
        self.Reponse = StringVar()
        self.Resultat = StringVar()
        self.Consigne = StringVar()

        #------------ Label contenant la consigne ancré au nord --------------#

        self.LabelInstr = Label(self, textvariable=self.Consigne)
        self.LabelInstr.pack(anchor = N,pady=4)

        #---------------------------------------------------------------------#

        #-------- Frame contenant les boites de textes ancré au nord ---------#

        self.FrameText = Frame(self)
        self.FrameText.pack(anchor = N, pady=6)

        LabelVoc = Label(self.FrameText, textvariable=self.MotLabel, width=40)
        LabelFleche = Label(self.FrameText, text="->")
        TextRep = Entry(self.FrameText, textvariable=self.Reponse, width=40)

        TextRep.bind('<Return>', self.event)

        LabelVoc.grid(row=0, column=0, padx=10)
        LabelFleche.grid(row=0, column=1, padx=2)
        TextRep.grid(row=0, column=2, padx=10)

        #---------------------------------------------------------------------#

        #-Label contenant le resultat ancré au nord donc sous la frame precedente-#

        self.LabelResult = Label(self, textvariable=self.Resultat)
        self.LabelResult.pack(anchor = N,pady=4)

        #-------------------------------------------------------------------------#


    def event(self, *args):
        print(self.Reponse.get())
        self.Reponse.set("")


    def ChgConsigne(self, NewConsigne):
        self.Consigne.set(NewConsigne)
        self.update_idletasks()


if __name__ == "__main__":
    app = FenetreVoc(None)
    app.title('my application')
    app.mainloop()