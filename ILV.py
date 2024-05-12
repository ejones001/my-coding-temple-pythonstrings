def input_length_validator(first_name, last_name):
    if len(first_name) < 2 or len(last_name) < 2:
        print("Error: Both first name and last name should be at least 2 characters long.")
    else:
        print("Input length validation successful.")

# Example:
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
input_length_validator(first_name, last_name)
