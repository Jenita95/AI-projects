import re
def chatbot_response(user_input):
    user_input = user_input.lower()
    if re.search(r'\b(hi|hello|hey|yey)\b', user_input):
        return "Hello! How can I assist you today?"
    elif re.search(r'\b(how are you|how do you do)\b', user_input):
        return "I'm just a bot, but I'm doing great! How about you?"
    elif re.search(r'\b(weather)\b', user_input):
       return "I'm not sure, but you can check your local weather forecast online."
    elif re.search(r'\b(help|support)\b', user_input):
        return "Sure! What do you need help with?"
    elif re.search(r'\b(can you suggest some positive quotes)\b', user_input):
        return "Sure! 1.You are your best 2.Think positive,feel positive,live positive 3.Mind is Everything"
    elif re.search(r'\b(bye|goodbye|exit)\b', user_input):
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you rephrase?"
print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['bye', 'exit']:
        print("Chatbot: Goodbye! Have a nice day!")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
