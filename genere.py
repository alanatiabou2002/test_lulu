import mysql.connector
from sentence_transformers import SentenceTransformer
import random
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="projet"
)

mycursor = db.cursor()
mycursor.execute("SELECT enoncé FROM question")
questions = mycursor.fetchall()

model = SentenceTransformer('bert-base-nli-mean-tokens')

num_questions = 10

selected_questions = random.sample(questions, num_questions)

#question_embeddings = model.encode([q[1] for q in selected_questions])
question_embeddings = model.encode([q[0] for q in selected_questions])

similarities = []
for i, emb1 in enumerate(question_embeddings):
    sim_list = []
    for j, emb2 in enumerate(question_embeddings):
        if i != j:
            sim_list.append((j, model(emb1, emb2)))
    sim_list.sort(key=lambda x: x[1], reverse=True)
    similarities.append(sim_list)

groups = []
for i, sim_list in enumerate(similarities):
    group = [selected_questions[i]]
    for j, sim in sim_list:
        if len(group) == 4:
            break
        if not any(q[0] == selected_questions[j][0] for q in group):
            group.append(selected_questions[j])
    groups.append(group)

    exam_questions = [random.choice(group) for group in groups]

print("Sujet d'examen :")
for i, q in enumerate(exam_questions):
    print(f"{i+1}. {q[1]}")