import string


plain_alphabet = string.ascii_lowercase
key = "QWERTYUIOPASDFGHJKLZXCVBNM".lower()  
encrypt_dict = dict(zip(plain_alphabet, key))
decrypt_dict = dict(zip(key, plain_alphabet))

def monoalphabetic_cipher(text, mode='encrypt'):
    result = ''
    for char in text.lower():
        if char in plain_alphabet:
            if mode == 'encrypt':
                result += encrypt_dict[char]
            else:
                result += decrypt_dict[char]
        else:
            result += char
    return result

message = "hello world"
encrypted = monoalphabetic_cipher(message, 'encrypt')
decrypted = monoalphabetic_cipher(encrypted, 'decrypt')

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
