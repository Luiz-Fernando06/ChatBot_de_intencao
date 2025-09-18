# 🤖 Chatbot Beleza Raiz


Este projeto é um chatbot de atendimento baseado em processamento de linguagem natural (NLP), capaz de responder a perguntas sobre o tema “Beleza Raiz” usando um modelo de Regressão Logística treinado com dados de intenções (intents) e exemplos de perguntas.

O bot é simples, mas eficiente, permitindo interações em tempo real pelo terminal.

⚙️ Como funciona

Carrega o dataset de intenções (dataset_chatbot_beleza_raiz.json) que contém:

Nome da intenção (name)

Exemplos de perguntas (examples)

Respostas possíveis (responses)

Prepara os dados:

Extrai as perguntas e suas respectivas intenções.

Vetoriza o texto com TF-IDF para transformar as palavras em números que o modelo entende.

Treina o modelo:

Usa Logistic Regression para classificar a intenção de cada pergunta.

Divide os dados em treino e teste, garantindo que o modelo seja preciso.

Geração de respostas:

O bot recebe uma pergunta do usuário.

Identifica a intenção usando o modelo treinado.

Seleciona aleatoriamente uma resposta adequada dentro da intenção.

Se não identificar a intenção, retorna: "Desculpe, não entendi sua pergunta."

Interação:

O usuário digita perguntas no terminal.

Comandos como "sair", "fim" ou "tchau" encerram a conversa.

🛠 Tecnologias utilizadas

Python 3 – Linguagem principal.

Scikit-learn – Vetorização de texto e classificação (TF-IDF + Logistic Regression).

JSON – Armazenamento das intenções, perguntas e respostas.

Random – Seleção aleatória de respostas.

▶️ Como usar
1. Instalar dependências
pip install scikit-learn pandas

2. Rodar o chatbot
python chatbot_beleza_raiz.py

3. Conversar

Digite perguntas relacionadas a cuidados, beleza ou informações do dataset.

Para encerrar a conversa, digite: "sair", "fim" ou "tchau".

🎯 Objetivo

Demonstrar processamento de linguagem natural com Python.

Criar um chatbot funcional capaz de identificar intenções e responder de forma coerente.

Servir como base para projetos de atendimento automatizado ou assistentes virtuais.
