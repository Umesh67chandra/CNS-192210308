def xor_bytes(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

def pad(data):
    pad_len = 16 - len(data) % 16
    return data + bytes([pad_len] * pad_len)

def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

def aes_encrypt_block(block, key):
    return xor_bytes(block, key)  # simple XOR (not real AES)

def aes_decrypt_block(block, key):
    return xor_bytes(block, key)  # same for XOR

def ecb_encrypt(plaintext, key):
    plaintext = pad(plaintext)
    return b''.join(aes_encrypt_block(plaintext[i:i+16], key) for i in range(0, len(plaintext), 16))

def ecb_decrypt(ciphertext, key):
    return unpad(b''.join(aes_decrypt_block(ciphertext[i:i+16], key) for i in range(0, len(ciphertext), 16)))

# Example usage
key = b'Sixteen byte key'
plaintext = b'Hello AES World!'

cipher = ecb_encrypt(plaintext, key)
print("Encrypted:", cipher)

decrypted = ecb_decrypt(cipher, key)
print("Decrypted:", decrypted)
