def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    raise ValueError("No modular inverse found")

def affine_encrypt(text, a, b):
    result = ""
    for char in text:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            result += chr(((a * (ord(char) - offset) + b) % 26) + offset)
        else:
            result += char
    return result

def affine_decrypt(cipher, a, b):
    a_inv = mod_inverse(a, 26)
    result = ""
    for char in cipher:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            result += chr(((a_inv * ((ord(char) - offset) - b)) % 26) + offset)
        else:
            result += char
    return result

# Example usage
a = 5     # Multiplicative key (must be coprime with 26)
b = 8     # Additive key

plain_text = "Affine Cipher"
encrypted = affine_encrypt(plain_text, a, b)
decrypted = affine_decrypt(encrypted, a, b)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
