BLOCK_SIZE = 8

def xor_bytes(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

def dummy_encrypt(block):
    return bytes([(b + 1) % 256 for b in block])

def dummy_decrypt(block):
    return bytes([(b - 1) % 256 for b in block])

def pad(data):
    padding_len = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + bytes([padding_len] * padding_len)

def unpad(data):
    return data[:-data[-1]]

def ecb_encrypt(plaintext):
    plaintext = pad(plaintext)
    blocks = [plaintext[i:i+BLOCK_SIZE] for i in range(0, len(plaintext), BLOCK_SIZE)]
    return b''.join(dummy_encrypt(block) for block in blocks)

def ecb_decrypt(ciphertext):
    blocks = [ciphertext[i:i+BLOCK_SIZE] for i in range(0, len(ciphertext), BLOCK_SIZE)]
    decrypted = b''.join(dummy_decrypt(block) for block in blocks)
    return unpad(decrypted)

def cbc_encrypt(plaintext, iv):
    plaintext = pad(plaintext)
    blocks = [plaintext[i:i+BLOCK_SIZE] for i in range(0, len(plaintext), BLOCK_SIZE)]
    ciphertext = b''
    prev = iv
    for block in blocks:
        encrypted = dummy_encrypt(xor_bytes(block, prev))
        ciphertext += encrypted
        prev = encrypted
    return ciphertext

def cbc_decrypt(ciphertext, iv):
    blocks = [ciphertext[i:i+BLOCK_SIZE] for i in range(0, len(ciphertext), BLOCK_SIZE)]
    plaintext = b''
    prev = iv
    for block in blocks:
        decrypted = xor_bytes(dummy_decrypt(block), prev)
        plaintext += decrypted
        prev = block
    return unpad(plaintext)

def cfb_encrypt(plaintext, iv):
    plaintext = pad(plaintext)
    blocks = [plaintext[i:i+BLOCK_SIZE] for i in range(0, len(plaintext), BLOCK_SIZE)]
    ciphertext = b''
    prev = iv
    for block in blocks:
        keystream = dummy_encrypt(prev)
        encrypted = xor_bytes(block, keystream)
        ciphertext += encrypted
        prev = encrypted
    return ciphertext

def cfb_decrypt(ciphertext, iv):
    blocks = [ciphertext[i:i+BLOCK_SIZE] for i in range(0, len(ciphertext), BLOCK_SIZE)]
    plaintext = b''
    prev = iv
    for block in blocks:
        keystream = dummy_encrypt(prev)
        decrypted = xor_bytes(block, keystream)
        plaintext += decrypted
        prev = block
    return unpad(plaintext)

# Example usage
data = b"HelloCrypt"
iv = b"12345678"

ecb = ecb_encrypt(data)
cbc = cbc_encrypt(data, iv)
cfb = cfb_encrypt(data, iv)

print("ECB Enc:", ecb)
print("ECB Dec:", ecb_decrypt(ecb))

print("CBC Enc:", cbc)
print("CBC Dec:", cbc_decrypt(cbc, iv))

print("CFB Enc:", cfb)
print("CFB Dec:", cfb_decrypt(cfb, iv))
