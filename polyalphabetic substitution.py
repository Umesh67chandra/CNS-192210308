def vigenere_encrypt(plain_text, key):
    encrypted = ""
    key = key.lower()
    key_index = 0

    for char in plain_text:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            k = ord(key[key_index % len(key)]) - ord('a')
            encrypted += chr((ord(char) - offset + k) % 26 + offset)
            key_index += 1
        else:
            encrypted += char
    return encrypted

def vigenere_decrypt(cipher_text, key):
    decrypted = ""
    key = key.lower()
    key_index = 0

    for char in cipher_text:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            k = ord(key[key_index % len(key)]) - ord('a')
            decrypted += chr((ord(char) - offset - k) % 26 + offset)
            key_index += 1
        else:
            decrypted += char
    return decrypted

# Example usage
plain = "HELLO WORLD"
key = "KEY"

encrypted = vigenere_encrypt(plain, key)
decrypted = vigenere_decrypt(encrypted, key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
