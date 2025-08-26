def person():
    print("person: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("person: Hi!")
        elif user_input == "how are you ?":
            print("person: I'm fine, thanks!")
        elif user_input == "bye":
            print("person: Goodbye!")
            break
        else:
            print("person: Sorry, I don't understand that.")

person()

