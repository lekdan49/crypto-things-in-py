"""
quick implementation of the Vigenère cipher in python.
"""
import string


def vigenere(plaintext, key):
    alphabet = list(string.ascii_uppercase)
    plaintext = plaintext.replace(" ", "")
    plaintext = plaintext.upper()
    key = key.upper()
    shift_values = []
    ciphertext = []
    print(alphabet)
    for letter in key:                              # create key values
        position_in_list = alphabet.index(letter)
        shift_values.append(position_in_list)
    index_pos = 0

    for letter in plaintext:
        if index_pos >= 3:
            index_pos = 0

        position_in_list = alphabet.index(letter)
        new_letter = position_in_list + shift_values[0 + index_pos]

        vigenered = alphabet[new_letter % len(alphabet)]
        ciphertext.append(vigenered)

        index_pos += 1
    return ciphertext


print(vigenere('THEY DRINK THE TEA', 'DUH'))

