def generate_matrix(key):
    matrix = []
    key = key.lower().replace('j', 'i')  # Replace 'j' with 'i'
    seen = set()

    for char in key + 'abcdefghijklmnopqrstuvwxyz':
        if char not in seen and char != 'j':
            matrix.append(char)
            seen.add(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def prepare_text(text):
    text = text.lower().replace('j', 'i').replace(' ', '')
    prepared = ''
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'x'
        if a == b:
            prepared += a + 'x'
            i += 1
        else:
            prepared += a + b
            i += 2
    if len(prepared) % 2 != 0:
        prepared += 'x'
    return prepared

def playfair_encrypt(plain_text, key):
    matrix = generate_matrix(key)
    text = prepare_text(plain_text)
    cipher = ''

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            cipher += matrix[r1][(c1 + 1) % 5]
            cipher += matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            cipher += matrix[(r1 + 1) % 5][c1]
            cipher += matrix[(r2 + 1) % 5][c2]
        else:
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]

    return cipher

# Example usage
key = "monarchy"
plain_text = "instruments"
encrypted = playfair_encrypt(plain_text, key)

print("Encrypted:", encrypted)
