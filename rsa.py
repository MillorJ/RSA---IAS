# Import necessary libraries
from sympy import gcd, mod_inverse

# Function to generate RSA keys
def generate_rsa_keys(p, q, e):
    # Compute n
    n = p * q
    # Compute Euler's Totient Function
    phi_n = (p - 1) * (q - 1)
    
    # Check if e is valid
    if gcd(e, phi_n) != 1:
        raise ValueError("e must be coprime to φ(n)")
    
    # Compute d (modular multiplicative inverse of e mod phi_n)
    d = mod_inverse(e, phi_n)
    
    # Return the public and private keys
    return (e, n), (d, n)

# Function to encrypt a plaintext message
def rsa_encrypt(plaintext, public_key):
    e, n = public_key
    m = int(plaintext)
    if m >= n:
        raise ValueError("Plaintext must be less than n")
    c = pow(m, e, n)
    return c

# Function to decrypt a ciphertext
def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    c = int(ciphertext)
    m = pow(c, d, n)
    return m

# Main program for user interaction
def main():
    print("=== RSA Cryptography ===")
    
    # Step 1: Input values for key generation
    print("\nStep 1: Key Generation")
    p = int(input("Enter a prime number (p): "))
    q = int(input("Enter another prime number (q): "))
    e = int(input("Enter a public exponent (e): "))
    
    try:
        public_key, private_key = generate_rsa_keys(p, q, e)
        print(f"\nPublic Key: {public_key}")
        print(f"Private Key: {private_key}")
    except ValueError as ve:
        print(f"Error: {ve}")
        return

    # Step 2: Encryption
    print("\nStep 2: Encryption")
    plaintext = input("Enter a plaintext number to encrypt (less than n): ")
    try:
        ciphertext = rsa_encrypt(plaintext, public_key)
        print(f"Ciphertext: {ciphertext}")
    except ValueError as ve:
        print(f"Error: {ve}")
        return

    # Step 3: Decryption
    print("\nStep 3: Decryption")
    decrypted_message = rsa_decrypt(ciphertext, private_key)
    print(f"Decrypted Message: {decrypted_message}")

# Run the main program
if __name__ == "__main__":
    main()
