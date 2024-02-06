import random
import string

def generate_password(length=8):
    # Combine all possible characters
    all5_characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(max(length, 8)))
    
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        print("Generated Password:", generate_password(length))
    except ValueError:
        print("Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()