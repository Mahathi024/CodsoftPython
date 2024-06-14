import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("1. Generate a password")
    print("2. Exit")

    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            length = int(input("Enter the length of the password: "))
            use_uppercase = input("Use uppercase letters? (y/n): ").lower() == 'y'
            use_numbers = input("Use numbers? (y/n): ").lower() == 'y'
            use_special_chars = input("Use special characters? (y/n): ").lower() == 'y'

            password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
            print(f"Generated password: {password}")
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()