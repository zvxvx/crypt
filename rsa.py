from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    with open("private.pem", "wb") as f:
        f.write(private_key)
    public_key = key.publickey().export_key()
    with open("receiver.pem", "wb") as f:
        f.write(public_key)

def encrypt_rsa(plaintext, public_key):
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    ciphertext = cipher.encrypt(plaintext.encode('utf-8'))
    return base64.b64encode(ciphertext).decode('utf-8')

def decrypt_rsa(ciphertext, private_key):
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    ciphertext = base64.b64decode(ciphertext)
    pt = cipher.decrypt(ciphertext).decode('utf-8')
    return pt