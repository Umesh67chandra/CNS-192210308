import hashlib
import random

# Sample DSA parameters (small values for demo only)
p = 593
q = 29
g = 123

x = random.randint(1, q-1)        # Private key
y = pow(g, x, p)                  # Public key

def sha1_hash(m):
    return int(hashlib.sha1(m.encode()).hexdigest(), 16)

def modinv(a, m):
    return pow(a, -1, m)

def sign(message):
    h = sha1_hash(message) % q
    while True:
        k = random.randint(1, q-1)
        r = pow(g, k, p) % q
        if r == 0:
            continue
        k_inv = modinv(k, q)
        s = (k_inv * (h + x * r)) % q
        if s != 0:
            break
    return r, s

def verify(message, r, s):
    if not (0 < r < q and 0 < s < q):
        return False
    h = sha1_hash(message) % q
    w = modinv(s, q)
    u1 = (h * w) % q
    u2 = (r * w) % q
    v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q
    return v == r

# Example usage
msg = "hello"
r, s = sign(msg)
print("Signature:", r, s)
print("Verification:", verify(msg, r, s))
