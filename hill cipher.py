def hill_encrypt(plain_text, key):
    plain_text = plain_text.lower().replace(" ", "")
    if len(plain_text) % 2 != 0:
        plain_text += 'x'  # pad if odd

    def char_to_num(c): return ord(c) - ord('a')
    def num_to_char(n): return chr(n % 26 + ord('a'))

    cipher_text = ""
    for i in range(0, len(plain_text), 2):
        p1 = char_to_num(plain_text[i])
        p2 = char_to_num(plain_text[i+1])

        c1 = (key[0][0]*p1 + key[0][1]*p2) % 26
        c2 = (key[1][0]*p1 + key[1][1]*p2) % 26

        cipher_text += num_to_char(c1) + num_to_char(c2)
    return cipher_text

# Example usage
key_matrix = [[3, 3], [2, 5]]  # Must be invertible mod 26
plain = "help"

encrypted = hill_encrypt(plain, key_matrix)
print("Encrypted:", encrypted)
