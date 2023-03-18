from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus

chatbot = ChatBot("Chatpot")
trainer = ListTrainer(chatbot)
CORPUS_FILE = "chat-demo.txt"

cleaned_corpus = clean_corpus(CORPUS_FILE)

trainer.train(cleaned_corpus)

exit_conditions = (":q", "quit", "exit")

print("Hello I'm Mathbot")
print("There is something that can I help you?")
while True:
    query = input("> ")

    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")
