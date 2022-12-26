#!/usr/bin/env python3

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(message_to_code, shift_number):

# Shift characters in the message
    result = ""
    for letter in range(len(message_to_code)):
        character = message_to_code[letter]
    
    # Encrypt uppercase letters
    if ord(character) >= 65 and ord(character) <= 91:
        result += chr((ord(character) + shift_number - 65) % 26 + 65)

    # Encrypt lowercase letters
    elif ord(character) >= 97 and ord(character) <= 122:
        result += chr((ord(character) + shift_number - 97) % 26 + 97)

    # No change if non-alphabet characters
    else:
        result += str(message_to_code[letter])
    return result

# Display ASCII art
from art import logo
print(logo)

# Check the above function
cipher_complete = False
while not cipher_complete:
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n(enter a negative number to decode)\n"))
    print(f"Plain Text: {text}")
    print(f"Shift pattern: {shift}")
    print("Cipher: " + encrypt(message_to_code=text, shift_number=shift))
    start_again = input("\nDo you want to encode/decode another message? \nType Y for yes and N for no to continue...").upper()
    if start_again == "N" or start_again == "NO":
        print("Goodbye.")
        cipher_complete = True
