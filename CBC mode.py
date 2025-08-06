def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def pad(data, block_size=16):
    pad_len = block_size - (len(data) % block_size)
    return data + bytes([pad_len] * pad_len)

def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

def simple_encrypt_block(block, key):
    return xor_bytes(block, key)  # Fake encryption (XOR with key)

def simple_decrypt_block(block, key):
    return xor_bytes(block, key)  # Fake decryption (XOR with key)

def encrypt_cbc(plaintext, key, iv):
    plaintext = pad(plaintext)
    blocks = [plaintext[i:i+16] for i in range(0, len(plaintext), 16)]
    ciphertext = b''
    prev = iv
    for block in blocks:
        block = xor_bytes(block, prev)
        encrypted = simple_encrypt_block(block, key)
        ciphertext += encrypted
        prev = encrypted
    return ciphertext

def decrypt_cbc(ciphertext, key, iv):
    blocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]
    plaintext = b''
    prev = iv
    for block in blocks:
        decrypted = simple_decrypt_block(block, key)
        decrypted = xor_bytes(decrypted, prev)
        plaintext += decrypted
        prev = block
    return unpad(plaintext)

# Example usage
key = b'1234567890abcdef'  # 16 bytes
iv = b'initvector123456'   # 16 bytes
data = b'Hello CBC Mode Example!'

cipher = encrypt_cbc(data, key, iv)
print("Encrypted:", cipher)

plain = decrypt_cbc(cipher, key, iv)
print("Decrypted:", plain)
