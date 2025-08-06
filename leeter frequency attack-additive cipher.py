from collections import Counter

def decrypt_caesar(ciphertext, key):
    decrypted = ''
    for char in ciphertext:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - offset - key) % 26 + offset)
        else:
            decrypted += char
    return decrypted

def frequency_attack(ciphertext):
    letters_only = [c.lower() for c in ciphertext if c.isalpha()]
    freq = Counter(letters_only)
    most_common = freq.most_common(1)[0][0]
    key = (ord(most_common) - ord('e')) % 26
    print(f"Guessed Key (from '{most_common}' → 'e'): {key}")
    return decrypt_caesar(ciphertext, key)

cipher_text = "Dro aesmu lbygx pyh TEWZC yfob dro vkji nyq."
decrypted = frequency_attack(cipher_text)
print("Decrypted:", decrypted)
