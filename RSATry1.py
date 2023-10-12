from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time

# Generate RSA keys
key = RSA.generate(2048)

# Separate the public and private keys
private_key = key
public_key = key.publickey()

# Create a cipher object for encryption using the public key
cipher_rsa_enc = PKCS1_OAEP.new(public_key)

# Sample data to encrypt
data = b's'

# Measure time for encryption
start_time = time.time()
encrypted_data = cipher_rsa_enc.encrypt(data)
end_time = time.time()
encryption_time_rsa = end_time - start_time

# Create a cipher object for decryption using the private key
cipher_rsa_dec = PKCS1_OAEP.new(private_key)

# Measure time for decryption
start_time = time.time()
decrypted_data = cipher_rsa_dec.decrypt(encrypted_data)
end_time = time.time()
decryption_time_rsa = end_time - start_time

# Record the data
print(f"RSA Encryption Time: {encryption_time_rsa}s")
print(f"RSA Decryption Time: {decryption_time_rsa}s")
