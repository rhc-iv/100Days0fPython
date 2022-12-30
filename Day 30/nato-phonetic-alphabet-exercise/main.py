#!/usr/bin/env python3

# Create an exception that disallows numeric characters from being
# entered into the app, along with an error message. Also, if an
# input error happens, repeat the input dialog until the user enters
# alphabetic characters.

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in
                 data.iterrows()}
print(phonetic_dict)

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry; please use only letter from the alphabet!")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()
