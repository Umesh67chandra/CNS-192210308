def str_to_bin(s):
    return ''.join(format(ord(c), '08b') for c in s)

def bin_to_str(b):
    return ''.join(chr(int(b[i:i+8], 2)) for i in range(0, len(b), 8))

def xor(a, b):
    return ''.join('0' if x == y else '1' for x, y in zip(a, b))

def des_simulate(text, key, mode='encrypt'):
    text_bin = str_to_bin(text)
    key_bin = str_to_bin(key)
    result_bin = xor(text_bin, key_bin)
    return bin_to_str(result_bin)

def triple_des_encrypt(plain, k1, k2, k3):
    step1 = des_simulate(plain, k1, 'encrypt')
    step2 = des_simulate(step1, k2, 'decrypt')
    step3 = des_simulate(step2, k3, 'encrypt')
    return step3

def triple_des_decrypt(cipher, k1, k2, k3):
    step1 = des_simulate(cipher, k3, 'decrypt')
    step2 = des_simulate(step1, k2, 'encrypt')
    step3 = des_simulate(step2, k1, 'decrypt')
    return step3

# Example usage
plain_text = "hellotxt"    # Must be 8 characters
key1 = "keyone11"
key2 = "keytwo22"
key3 = "keytri33"

cipher = triple_des_encrypt(plain_text, key1, key2, key3)
decrypted = triple_des_decrypt(cipher, key1, key2, key3)

print("Encrypted:", cipher)
print("Decrypted:", decrypted)
