from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import *
import pymysql
import os 

class Formulaire:
    def _init_(self,root):
        self.root = root
        self.root.title('FORMULAIRE')
        self.root.geometry('1920x1080+0+0')
        frame1= Frame(self.root, bg='white')
        frame1.place(x=50, y=50, width=50, height= 50)


        #title=Label(frame1, text='hello')'''


root=Tk()
obj=Formulaire()
root.mainloop()

#fenetre=Tk()
#fenetre.geometry('500x500')
#fenetre.title('Enregistrer une question')
#fenetre['bg']='black'
'''fenetre.resizable(height=False, width=False)

def ajouter():
    label['text']= enoncé.get()
enoncé= StringVar()
label= Label(fenetre, text='ENREGISTRER UNE NOUVELLE QUESTION', font=('verdana',10,'italic bold',))
label.pack()
entree= Entry(fenetre, textvariable=enoncé)
entree.pack()
bouton= Button(fenetre, text='Enregistrer', bg='white', fg='black', command= ajouter)
bouton.pack()


fenetre.mainloop()'''
