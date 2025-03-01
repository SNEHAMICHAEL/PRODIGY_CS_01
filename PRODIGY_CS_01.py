# -*- coding: utf-8 -*-
"""Untitled45.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wnsdDjH747HmizoAKT0VBgggawemEoNU
"""

def encryption(pt, k):
    encrypted_msg = ''
    for char in pt:
        if char.isalpha():
            if char.islower():
                encrypted_msg += chr((ord(char) - 97 + k) % 26 + 97)
            else:
                encrypted_msg += chr((ord(char) - 65 + k) % 26 + 65)
        else:
            encrypted_msg =encrypted_msg + char
    return encrypted_msg

def decryption(ct, k):
    decrypted_msg = ''
    for char in ct:
        if char.isalpha():
            if char.islower():
                decrypted_msg += chr((ord(char) - 97 - k) % 26 + 97)
            else:
                decrypted_msg += chr((ord(char) - 65 - k) % 26 + 65)
        else:
            decrypted_msg =decrypted_msg + char
    return decrypted_msg

plain_text = input("Enter your message: ")
k = int(input("Enter the shift value: "))
c = encryption(plain_text, k)
print("Encrypted text is",c)
d = decryption(c, k)
print("Decrypted text is",d)