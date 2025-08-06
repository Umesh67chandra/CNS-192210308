import hashlib

# AES parameters
Nb = 4
Nk = 4
Nr = 10

# Rijndael S-box
s_box = [
    # (only partial shown due to size limits – you'll fill the full 256 values)
    0x63, 0x7C, 0x77, 0x7B, ..., 0x16
]

# Helper functions for AES - You'd need to define full key expansion, add_round_key, sub_bytes, etc.
# But for simplicity in CBC-MAC, we'll use SHA-256 digest to simulate block encryption.

def xor_bytes(a, b):
    return bytes(i ^ j for i, j in zip(a, b))

def simple_block_cipher(key, block):
    """Fake AES encryption for educational CBC-MAC example"""
    data = key + block
    return hashlib.sha256(data).digest()[:16]  # Simulate AES block (16 bytes)

def pad(message):
    pad_len = 16 - len(message) % 16
    return message + bytes([pad_len] * pad_len)

def cbc_mac(message, key):
    message = pad(message)
    iv = bytes([0]*16)
    prev = iv

    for i in range(0, len(message), 16):
        block = message[i:i+16]
        xor_block = xor_bytes(block, prev)
        prev = simple_block_cipher(key, xor_block)

    return prev

# Example usage
key = b'MySecretKey12345'  # 16 bytes
message = b'Hello, CBC-MAC World!'

mac = cbc_mac(message, key)
print("CBC-MAC:", mac.hex())
