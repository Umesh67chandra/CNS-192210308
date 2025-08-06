import hashlib

message = "This is a secret message"
hash_object = hashlib.sha3_256(message.encode())
sha3_hash = hash_object.hexdigest()
print("SHA3-256 Hash:", sha3_hash)
