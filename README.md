# Chatbot Inteligente — Beleza Raiz

## Objetivo:
Desenvolver um chatbot baseado em Processamento de Linguagem Natural (NLP) capaz de identificar intenções e responder de forma coerente a perguntas sobre o tema “Beleza Raiz”.

## Principais etapas realizadas:

- Preparação dos dados: Carregamento do dataset em formato JSON, contendo intenções, exemplos de perguntas e possíveis respostas.

- Vetorização do texto: Conversão das mensagens em representações numéricas utilizando TF-IDF (Term Frequency–Inverse Document Frequency).

- Treinamento do modelo: Aplicação de Regressão Logística para classificar as intenções das mensagens com alta acurácia (≈ 100%).

- Geração de respostas: Mapeamento da intenção prevista para uma resposta correspondente, selecionada aleatoriamente para maior naturalidade.

- Interação em terminal: Implementação de um loop interativo, permitindo conversas diretas com o usuário até o comando de saída.

## Resumo:
Chatbot treinado com machine learning supervisionado, capaz de compreender perguntas em linguagem natural e responder de forma contextual.
