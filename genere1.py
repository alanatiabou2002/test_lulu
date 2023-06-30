import mysql.connector
import random

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="projet"
)

mycursor = db.cursor()
mycursor.execute("SELECT enoncé, image_q FROM question")
questions = mycursor.fetchall()

 # nombre de questions à générer
num_questions = 10
selected_questions = random.sample(questions, num_questions)


with open ('sujet.txt', 'w') as file :
    file.write("EVALUATION :\n")
    for i, question in enumerate(selected_questions):
      file.write(f"{i+1}. {question[0]}\n")

print('ok')
#for question in selected_questions:
  #  print(question[0])
