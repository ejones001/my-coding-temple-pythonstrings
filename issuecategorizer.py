def issue_categorizer(user_input):
    if "issue" in user_input.lower():
        keywords = ["login", "performance", "error"]
        for keyword in keywords:
            if keyword in user_input.lower():
                print(f"The issue seems to be related to {keyword}.")
                return
        print("The issue could not be categorized.")
    else:
        print("No issue found in the input.")

user_input = input("Please describe the issue you're facing: ")
issue_categorizer(user_input)
