def simple_xor_encrypt(msg, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(msg))

def simple_xor_decrypt(cipher, key):
    return simple_xor_encrypt(cipher, key)  # XOR is symmetric

message = "HELLO"
key = "KEY"

cipher = simple_xor_encrypt(message, key)
print("Encrypted:", [ord(c) for c in cipher])

decrypted = simple_xor_decrypt(cipher, key)
print("Decrypted:", decrypted)
