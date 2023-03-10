from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


# Quando o módulo time não funcionar

import time
time.clock = time.time

# corrigir o bug se caso acontencer
# from spacy.cli import download

# download("en_core_web_sm")

# class EMGSM:
#     ISO_639_1 = 'en_core_web_sm'

# # Iniciando o chatterBot

chatbot = ChatBot("BotCris") # tagger_language=EMGSM)

conversa = [
    "Olá",
    "Tudo bem",
    "Meu nome é Bot Cris",
    "Que legal, Oque você faz?",
    "Por enquanto tenho só conversas curtas! Mas estou aprendendo",
    "Showw",
    
]

trainer = ListTrainer(chatbot)
trainer.train(conversa)

while True:
    mensagem = input("Mande uma mensagem para o chatbot: ")
    if mensagem == "parar":
        break
    resposta = chatbot.get_response(mensagem)
    print(resposta)


# caso necessite depois do treino apagar o banco de dados
# usar o comando no terminal:
# chatbot.storage.drop()

