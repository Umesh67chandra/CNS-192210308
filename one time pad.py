import random
import string

def generate_key(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def otp_encrypt(plain_text, key):
    encrypted = ''
    for p, k in zip(plain_text, key):
        if p.isalpha():
            enc = (ord(p.lower()) - ord('a') + ord(k.lower()) - ord('a')) % 26
            encrypted += chr(enc + ord('a'))
        else:
            encrypted += p
    return encrypted

def otp_decrypt(cipher_text, key):
    decrypted = ''
    for c, k in zip(cipher_text, key):
        if c.isalpha():
            dec = (ord(c.lower()) - ord(k.lower()) + 26) % 26
            decrypted += chr(dec + ord('a'))
        else:
            decrypted += c
    return decrypted

# Example usage
plain = "hello"
key = generate_key(len(plain))

encrypted = otp_encrypt(plain, key)
decrypted = otp_decrypt(encrypted, key)

print("Plain Text :", plain)
print("Random Key :", key)
print("Encrypted  :", encrypted)
print("Decrypted  :", decrypted)
