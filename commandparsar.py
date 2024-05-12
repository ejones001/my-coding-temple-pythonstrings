def command_parser(user_input):
    predefined_commands = ["help", "issue", "contact support"]

    for command in predefined_commands:
        if command in user_input.lower():
            if command == "help":
                print("Sure, how can I assist you?")
            elif command == "issue":
                print("I see you're experiencing an issue. Let's try to resolve it.")
            elif command == "contact support":
                print("Please contact our support team at support@example.com.")
            return

    print("Sorry, I couldn't understand your request.")


user_input = input("How can I assist you? ")
command_parser(user_input)
