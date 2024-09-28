def encrypt(text, shift):
    result = ""
    # traverse through each character in the text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # non-alphabet characters remain unchanged
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Input from user
message = input("Enter message: ")
shift_value = int(input("Enter shift value: "))

# Encrypting the message
encrypted_message = encrypt(message, shift_value)
print("Encrypted message: " + encrypted_message)

# Decrypting the message
decrypted_message = decrypt(encrypted_message, shift_value)
print("Decrypted message: " + decrypted_message)
