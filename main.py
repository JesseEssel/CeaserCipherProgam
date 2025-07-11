logo = '''

   _____          ______  _____         _____        _____ _____ _____  _    _ ______ _____  
  / ____|   /\   |  ____|/ ____|  /\   |  __ \      / ____|_   _|  __ \| |  | |  ____|  __ \ 
 | |       /  \  | |__  | (___   /  \  | |__) |    | |      | | | |__) | |__| | |__  | |__) |
 | |      / /\ \ |  __|  \___ \ / /\ \ |  _  /     | |      | | |  ___/|  __  |  __| |  _  / 
 | |____ / ____ \| |____ ____) / ____ \| | \ \     | |____ _| |_| |    | |  | | |____| | \ \ 
  \_____/_/    \_\______|_____/_/    \_\_|  \_\     \_____|_____|_|    |_|  |_|______|_|  \_\


'''

print(logo)
print("Welcome to Caesar Cipher(Encryption / Decryption) Of Messages")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# encrypt function
def encrypt(message, shift):
    ciphertext = ''
    for char in message:
        if char.isalpha():
            char_index = alphabet.index(char.lower())
            shifted_index = (char_index + shift) % len(alphabet)
            if char.isupper():
                ciphertext += alphabet[shifted_index].upper()
            else:
                ciphertext += alphabet[shifted_index]
        else:
            ciphertext += char
    return ciphertext


# decrypt function
def decrypt(ciphertext, shift):
    message = ''
    for char in ciphertext:
        if char.isalpha():
            char_index = alphabet.index(char.lower())
            shifted_index = (char_index - shift) % len(alphabet)
            if char.isupper():
                message += alphabet[shifted_index].upper()
            else:
                message += alphabet[shifted_index]
        else:
            message += char
    return message

# Accepting input
while True:  # looping the program when input is yes
    decision = input("Type 'encode' to encrypt or 'decode' to decrypt: ")
    message = input("Type your message: ")
    shift = int(input("Input your number of shifts: "))

    if decision == "encode":
        encrypted_text = encrypt(message, shift)
        print(f"This is the encrypted message: {encrypted_text}")
    elif decision == "decode":
        decrypted_text = decrypt(encrypted_text, shift)
        print(f"This is the decrypted message: {decrypted_text}")
    else:
        print("wrong input...Please read the question again!!!")

    question = input("Would you like to try again? Type 'yes' to continue or 'no' to end: ")
    if question == "no":
        print("Thank you for using the program...session end")
        break  # Exit the loop if the user enters "no"
# The End...



