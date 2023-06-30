import nltk

'''nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')'''

import random
from nltk import word_tokenize, pos_tag
import mysql.connector
import reformulate

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="projet"
)

def reformulate_question(question):
    tokens = word_tokenize(question)
    tagged_tokens = pos_tag(tokens)
    reformulated_question= reformulate_sentence(tagged_tokens)
    return reformulate_question

def permute_questions(question):
    permuted_questions = random.sample(question, len(question))
    return permuted_questions

mycursor=db.cursor()
mycursor.execute("SELECT enoncé, image_q FROM question")
questions = mycursor.fetchall()


# nombre de questions à générer
num_questions = 10 
selected_questions = random.sample(questions, num_questions)

reformulated_questions = []
for question in selected_questions:
    reformulated_question = reformulate_question(question[0])
    reformulated_questions.append(reformulated_question)

permuted_questions = permute_questions(reformulated_questions)

with open ('sujet1.txt', 'w') as file :
    file.write("Sujet d'examen :\n")
    for i, question in enumerate(selected_questions):
      file.write(f"{i+1}. {question[0]}\n")

print('ok')


'''print("Sujet d'examen")
for i, question in enumerate(permuted_questions):
    print(f"{i+1}. {question}")'''