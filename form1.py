from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import *
import pymysql
import os 
import mysql.connector
#connexion à la base de données
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="projet"
)

#enregistrer une question

def enregistrer_question():
    enoncé= user_enonce.get()
    notation= user_notation.get()
    image_q= image_q.get()
    typeQuestion= type_id.get()
    cursor= db.cursor()
    sql='INSERT INTO question (enoncé,notation, image_q, typeQuestion) VALUES (%s,%s,%s,%s)' 
    val=(enoncé, notation, image_q, typeQuestion)  
    cursor.execute(sql,val) 
    db.commit()
   # message_label.config(text='Question enregistrée avec succès')



maFenetre = Tk()
maFenetre.title('ENREGISTRER UNE QUESTION')
maFenetre.geometry('500x500')
def f1():
    print ('hello')

label = Label (maFenetre , text = 'Enregistrez vos questions' )
label.pack()


user_enonce = Entry(maFenetre ,bg='white' )
user = Label (maFenetre, text ='enoncé' )
user . pack()
user_enonce. pack()

user_notation = Entry(maFenetre ,bg='white' )
user2 = Label (maFenetre, text ='notation' )
user2 . pack()
user_notation. pack()

image_q= Entry(maFenetre ,bg='white' )
user3 = Label (maFenetre, text ='image' )
user3 . pack()
image_q. pack()

type_id = Entry(maFenetre ,bg='white' )
user4 = Label (maFenetre, text ='type de question' )
user4. pack()
type_id. pack()


b = Button(maFenetre , text ='Enregistrer'  , command = enregistrer_question)
b.pack()

b1 = Button(maFenetre , text ='composer'  , command = f1 )
b1.pack()
maFenetre .mainloop ()
