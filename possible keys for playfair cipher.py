def prepare_text(text, for_encryption=True):
    text = text.upper().replace("J", "I").replace(" ", "")
    result = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = ''
        if (i + 1) < len(text):
            b = text[i + 1]
        else:
            b = 'X'

        if a == b:
            result += a + 'X'
            i += 1
        else:
            result += a + b
            i += 2

    if len(result) % 2 != 0:
        result += 'X'

    return result


def generate_key_matrix(keyword):
    matrix = []
    seen = set()
    keyword = keyword.upper().replace("J", "I")

    for char in keyword:
        if char not in seen and char.isalpha():
            matrix.append(char)
            seen.add(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # Note: 'J' is excluded
        if char not in seen:
            matrix.append(char)
            seen.add(char)

    # Create 5x5 matrix
    key_matrix = [matrix[i*5:(i+1)*5] for i in range(5)]
    return key_matrix


def find_position(letter, matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return i, j
    return None


def encrypt_pair(a, b, matrix):
    row1, col1 = find_position(a, matrix)
    row2, col2 = find_position(b, matrix)

    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]


def decrypt_pair(a, b, matrix):
    row1, col1 = find_position(a, matrix)
    row2, col2 = find_position(b, matrix)

    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]


def encrypt(text, matrix):
    text = prepare_text(text)
    result = ""
    for i in range(0, len(text), 2):
        result += encrypt_pair(text[i], text[i+1], matrix)
    return result


def decrypt(ciphertext, matrix):
    result = ""
    for i in range(0, len(ciphertext), 2):
        result += decrypt_pair(ciphertext[i], ciphertext[i+1], matrix)
    return result


# Example usage:
keyword = "MONARCHY"
plaintext = "INSTRUMENTS"

key_matrix = generate_key_matrix(keyword)
ciphertext = encrypt(plaintext, key_matrix)
decrypted_text = decrypt(ciphertext, key_matrix)

print("Keyword        :", keyword)
print("Key Matrix     :")
for row in key_matrix:
    print(row)
print("Plaintext      :", plaintext)
print("Ciphertext     :", ciphertext)
print("Decrypted Text :", decrypted_text)
