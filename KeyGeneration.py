from Crypto.PublicKey import RSA
import time

# Measure time to generate RSA keys of size 2048
start_time = time.time()
key = RSA.generate(2048)
end_time = time.time()
keygen_time_rsa = end_time - start_time

# Record the data
print(f"RSA Key Generation Time (2048 bits): {keygen_time_rsa}s")
