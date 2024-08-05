import os
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

def generate_keys():
    rsa_newpath = r'rsa/'
    if not os.path.exists(rsa_newpath):
      os.makedirs(rsa_newpath)

    key = RSA.generate(2048)
    private_key = key.export_key()
    with open("rsa/private.pem", "wb") as f:
        f.write(private_key)
    public_key = key.publickey().export_key()
    with open("rsa/receiver.pem", "wb") as f:
        f.write(public_key)

def encrypt_rsa(plaintext):
    data = plaintext.encode("utf-8")

    recipient_key = RSA.import_key(open("rsa/receiver.pem").read())
    session_key = get_random_bytes(16)

    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)

    with open("rsa/encrypted_data.bin", "wb") as f:
        f.write(enc_session_key)
        f.write(cipher_aes.nonce)
        f.write(tag)
        f.write(ciphertext)

    return f"""
    ++++ ENCRYPTION COMPLETE ++++
    Your input has been encryped in file rsa/encrypted_data.bin
    ++++ ENCRYPTION COMPLETE ++++
    """

def decrypt_rsa():
    private_key = RSA.import_key(open("rsa/private.pem").read())

    with open("rsa/encrypted_data.bin", "rb") as f:
        enc_session_key = f.read(private_key.size_in_bytes())
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()

    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)

    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    
    plaintext = data.decode("utf-8")
    
    return f"""
    ++++ DECRYPTION COMPLETE ++++
    {plaintext}
    ++++ DECRYPTION COMPLETE ++++
    """