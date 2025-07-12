import random
import string

def generate_password(length=12):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure password contains at least one of each type
    if length < 4:
        raise ValueError("Password length must be at least 4")

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Fill the rest with a mix of all characters
    all_characters = lowercase + uppercase + digits + symbols
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the result to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

# Example usage
password = generate_password(12)
print("Generated Password:", password)
