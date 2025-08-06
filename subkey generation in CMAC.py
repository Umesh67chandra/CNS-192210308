def left_shift_one_bit(input_bytes):
    shifted = int.from_bytes(input_bytes, byteorder='big') << 1
    shifted &= (1 << 128) - 1
    return shifted.to_bytes(16, byteorder='big')

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def generate_subkeys():
    const_Rb = 0x87
    L = bytes.fromhex('7df76b0c1ab899b33e42f047b91b546f')  # Simulated AES(key, 0)
    K1 = left_shift_one_bit(L)
    if L[0] & 0x80:
        K1 = xor_bytes(K1, b'\x00' * 15 + bytes([const_Rb]))
    K2 = left_shift_one_bit(K1)
    if K1[0] & 0x80:
        K2 = xor_bytes(K2, b'\x00' * 15 + bytes([const_Rb]))
    return K1, K2

K1, K2 = generate_subkeys()
print("K1:", K1.hex())
print("K2:", K2.hex())
