import random
import string

def generate_password(length):
    # Define the pool of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password using random.choices()
    password = ''.join(random.choices(characters, k=length))

    return password

def password_generator():
    print("Welcome to Password Generator!")
    length = int(input("Enter the desired length of the password: "))

    # Generate the password
    password = generate_password(length)

    # Display the password
    print("Generated Password:", password)

password_generator()