"""
Implementation of caesar cipher in python
"""
import string


def caesar(plaintext, shift=3):
    alphabet = list(string.ascii_uppercase)
    plaintext = plaintext.replace(" ", "")
    plaintext = plaintext.upper()
    ciphertext = []

    for letter in plaintext:
        letter_pos = alphabet.index(letter)
        shift_len = letter_pos + shift
        caesared = alphabet[shift_len % len(alphabet)]  # wrap around list after done
        ciphertext.append(caesared)
    return ciphertext


def decrypt(ciphertext, shift=3):
    alphabet = list(string.ascii_uppercase)
    plaintext = []

    for letter in ciphertext:
        letter_pos = alphabet.index(letter)
        shift_len = letter_pos - shift
        caesared = alphabet[shift_len % len(alphabet)]  # wrap around list after done
        plaintext.append(caesared)
    return plaintext


ciphertext = caesar('POTATOES ARE GOOD YES ZZZZ XXX')
print(ciphertext)
print(decrypt(ciphertext))
