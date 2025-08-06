def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift_amount = shift if mode == 'encrypt' else -shift
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char
    return result

# Example usage
plain_text = "Hello World"
shift = 3

encrypted = caesar_cipher(plain_text, shift, mode='encrypt')
decrypted = caesar_cipher(encrypted, shift, mode='decrypt')

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
