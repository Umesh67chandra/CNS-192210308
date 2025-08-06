P = 23
G = 5

a = 6
b = 15

A = pow(G, a, P)
B = pow(G, b, P)

alice_shared_key = pow(B, a, P)
bob_shared_key = pow(A, b, P)

print("Publicly Shared Prime (P):", P)
print("Publicly Shared Base (G):", G)

print("Alice's Private Key (a):", a)
print("Bob's Private Key (b):", b)

print("Alice sends to Bob: A =", A)
print("Bob sends to Alice: B =", B)

print("Alice's Computed Shared Key:", alice_shared_key)
print("Bob's Computed Shared Key:", bob_shared_key)

if alice_shared_key == bob_shared_key:
    print("✅ Shared key successfully established!")
else:
    print("❌ Shared key mismatch!")
