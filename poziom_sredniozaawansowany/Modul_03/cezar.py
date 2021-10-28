def rot13_encrypt(text: str) -> str:
    if type(text) is not str:
        return False

    encrypted_text = ""
    for letter in text.lower():
        ascii_code = ord(letter)
        if ascii_code > 109:  # 122 (z) - 13
            encrypted_text += chr(ascii_code + 13 - 26) # 26 - ilość liter w ang.
        else:
            encrypted_text += chr(ascii_code + 13)

    return encrypted_text

def rot13_decrypt(text: str) -> str:
    if type(text) is not str:
        return False

    encrypted_text = ""
    for letter in text.lower():
        ascii_code = ord(letter)
        if ascii_code - 13 < 97:
            encrypted_text += chr(ascii_code - 13 + 26)
        else:
            encrypted_text += chr(ascii_code - 13)

    return encrypted_text

encrypted = rot13_encrypt("Python")
print(f"Encrypted text is: {encrypted}")

decrypted = rot13_decrypt(encrypted)
print(f"Decrypted text is: {decrypted}")
