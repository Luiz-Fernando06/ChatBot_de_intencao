#Bibliotecas necessarias
from json import load
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import random

#Carregando dataset
with open('dataset_chatbot_beleza_raiz.json', 'r', encoding="utf-8") as f:
    dataset = load(f)

#preparação de dados para treino
perguntas = []
intencaos = []
for item in dataset['intents']:
  for pergunta in item['examples']:
    perguntas.append(pergunta)
    intencaos.append(item['name'])

#Transformando texto em número(vetrorização)
vetorizacao = TfidfVectorizer()
X = vetorizacao.fit_transform(perguntas)
y = intencaos

#Treinando modelo
modelo = LogisticRegression(max_iter=100)
modelo.fit(X, y)

#Vendo a acuracia
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
y_pred = modelo.predict(X_test) #Acuracia: 1.0

#Gerando respostas
def gerar_resposta(menssagem):
    pergunta_vetorizada = vetorizacao.transform([menssagem])
    intencao = modelo.predict(pergunta_vetorizada)[0]
    for item in dataset['intents']:
      if item['name'] == intencao:
        respostas = item['responses']
        resposta_bot = random.choice(respostas)
        return resposta_bot
    return "Desculpe, não entendi sua pergunta."

#Testando no terminal
print("Digite 'sair', 'fim' ou 'tchau' para encerrar a conversa.")
while True:
  entrada = input("Voce: ")
  if entrada.lower() in ["sair", "fim", "tchau"]:
    print("Bot: Até logo!")
    break
  resposta = gerar_resposta(entrada)
  print(f"Bot: {resposta}")

