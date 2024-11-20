import random
from math import gcd

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to generate a prime number within a range
def generate_prime(start, end):
    while True:
        num = random.randint(start, end)
        if is_prime(num):
            return num

# Function to calculate modular multiplicative inverse
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Key generation function
def generate_keys():
    # Generate two distinct prime numbers
    p = generate_prime(100, 999)
    q = generate_prime(100, 999)
    while p == q:
        q = generate_prime(100, 999)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Choose e such that 1 < e < phi and gcd(e, phi) == 1
    e = random.choice([x for x in range(2, phi) if gcd(x, phi) == 1])
    
    # Calculate d
    d = mod_inverse(e, phi)
    
    return ((e, n), (d, n))  # Return public and private keys

# Encryption function
def encrypt(message, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in message]

# Decryption function
def decrypt(ciphertext, private_key):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

# Main function to demonstrate RSA
def rsa_encryption_decryption():
    print("RSA Encryption and Decryption")
    
    # Step 1: Generate keys
    public_key, private_key = generate_keys()
    print("\nPublic Key:", public_key)
    print("Private Key:", private_key)
    
    # Step 2: Get user input for plaintext
    message = input("\nEnter the plaintext message to encrypt: ")
    
    # Step 3: Encrypt the message
    ciphertext = encrypt(message, public_key)
    print("\nEncrypted Message (Ciphertext):", ciphertext)
    
    # Step 4: Decrypt the ciphertext
    decrypted_message = decrypt(ciphertext, private_key)
    print("\nDecrypted Message (Plaintext):", decrypted_message)

# Run the RSA demonstration
rsa_encryption_decryption()
