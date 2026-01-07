def chatbot():

    #A simple rule-based chatbot that responds to predefined user inputs.
    #Type 'bye' to end the conversation.and this is just a simple conservation you can use you own choice to make the chatboot more batter
    
    print("Chatbot: Hello! I am a simple chatbot. How can I assist you today?")
    print("Chatbot: You can type 'hello', 'how are you', or 'bye' to exit.\n")

    # Infinite loop to keep the chatbot running
    while True:
        # Taking input from the user and converting it to lowercase
        user_input = input("User: ").strip().lower()

        # Checking user input and responding accordingly
        if user_input == "hello":
            print("Chatbot: Hi there! Nice to meet you.")
        
        elif user_input == "how are you":
            print("Chatbot: I'm doing well, thank you for asking!")
        
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a great day ahead.")
            break  # Exit the loop and end the chat
        
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Please try again.")

# Calling the chatbot function
chatbot()
