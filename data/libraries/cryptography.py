from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt_message(message, public_key):
    recipient_key = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    encrypted_message = cipher_rsa.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, private_key):
    private_key = RSA.import_key(private_key)
    cipher_rsa = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher_rsa.decrypt(encrypted_message).decode()
    return decrypted_message

if __name__ == "__main__":
    private_key, public_key = generate_key_pair()
    original_message = "Hello, World!"
    encrypted_message = encrypt_message(original_message, public_key)
    print("Encrypted message:", encrypted_message)

    decrypted_message = decrypt_message(encrypted_message, private_key)
    print("Decrypted message:", decrypted_message)
