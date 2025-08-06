def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def pad(data, block_size=16):
    pad_len = block_size - (len(data) % block_size)
    return data + bytes([pad_len] * pad_len)

def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

def simple_encrypt_block(block, key):
    return xor_bytes(block, key)

def simple_decrypt_block(block, key):
    return xor_bytes(block, key)

def encrypt_ecb(plaintext, key):
    plaintext = pad(plaintext)
    blocks = [plaintext[i:i+16] for i in range(0, len(plaintext), 16)]
    ciphertext = b''
    for block in blocks:
        encrypted = simple_encrypt_block(block, key)
        ciphertext += encrypted
    return ciphertext

def decrypt_ecb(ciphertext, key):
    blocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]
    plaintext = b''
    for block in blocks:
        decrypted = simple_decrypt_block(block, key)
        plaintext += decrypted
    return unpad(plaintext)

# Example usage
key = b'1234567890abcdef'  # 16 bytes key
data = b'Hello ECB Mode Example in Python'

cipher = encrypt_ecb(data, key)
print("Encrypted:", cipher)

plain = decrypt_ecb(cipher, key)
print("Decrypted:", plain)
