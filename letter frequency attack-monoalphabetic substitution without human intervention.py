from collections import Counter

def frequency_attack_mono(ciphertext):
    english_freq_order = 'etaoinshrdlcumwfgypbvkjxqz'
    cipher_freq = Counter(c for c in ciphertext.lower() if c.isalpha())
    sorted_cipher_letters = [item[0] for item in cipher_freq.most_common()]
    mapping = {c: p for c, p in zip(sorted_cipher_letters, english_freq_order)}
    
    decrypted = ''
    for char in ciphertext:
        if char.isalpha():
            lower = char.lower()
            sub = mapping.get(lower, lower)
            decrypted += sub.upper() if char.isupper() else sub
        else:
            decrypted += char
    return decrypted

cipher_text = "Wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj."
decrypted = frequency_attack_mono(cipher_text)
print("Decrypted:", decrypted)
