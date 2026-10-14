# BASIC CHATBOT

def ChatBot ():
    while True:
        
        you = input("Enter the massage: ").lower()

        if you == "hello":
            print("Bot: hi")

        elif you == "how are you":
            print("Bot: I'm fine thanks!")

        elif you == "bye":
            print("Bot: Goodbye!")
        
        else:
            print("Bot: sorry, I don't understand")

ChatBot()