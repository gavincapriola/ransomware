#!/usr/bin/env python3

from cryptography.fernet import Fernet
import os

class Ransomware:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.files = [file for file in os.listdir() if file !=
                      "main.py" and os.path.isfile(file)] 

    def encrypt_files(self):
        pass

    def decrypt_files(self):
        pass

    def delete_files(self):
        pass


if __name__ == "__main__":
    ransomware = Ransomware()
