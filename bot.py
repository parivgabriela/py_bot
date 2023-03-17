from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Chatpot")
trainer = ListTrainer(chatbot)

trainer.train([
    "Hi",
    "Welcome, friend 🤗",
])

trainer.train([
    "Are you a plant?",
    "No, I'm the pot below the plant!",
])
exit_conditions = (":q", "quit", "exit")

print("Hello I'm Mathbot")
print("There is something that can I help you?")
while True:
    query = input("> ")

    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")
