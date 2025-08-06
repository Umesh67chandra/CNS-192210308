def string_to_binary(s):
    return ''.join(format(ord(c), '08b') for c in s)

def binary_to_string(b):
    return ''.join(chr(int(b[i:i+8], 2)) for i in range(0, len(b), 8))

def xor(a, b):
    return ''.join('0' if i == j else '1' for i, j in zip(a, b))

def simple_des_encrypt(plain_text, key):
    pt_bin = string_to_binary(plain_text)
    key_bin = string_to_binary(key)
    return xor(pt_bin, key_bin)

def simple_des_decrypt(cipher_bin, key):
    key_bin = string_to_binary(key)
    return binary_to_string(xor(cipher_bin, key_bin))

# Example
plain_text = "8letters"       # Exactly 8 chars
key = "mysecret"              # Exactly 8 chars

cipher_bin = simple_des_encrypt(plain_text, key)
decrypted = simple_des_decrypt(cipher_bin, key)

print("Encrypted (binary):", cipher_bin)
print("Decrypted:", decrypted)
