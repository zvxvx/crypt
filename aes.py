from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
import base64

def generate_key():
  return get_random_bytes(16)

def encrypt_aes(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
    iv = cipher.iv
    ct = base64.b64encode(iv + ct_bytes).decode('utf-8')
    encoded_key = base64.b64encode(key).decode('utf-8')
    return f"""
    ==========
    Your encrypted message is: {ct}
    Your key is {encoded_key}
    Please keep this safe!
    ==========
    """
def decrypt_aes(ciphertext, key):
    try:
        ct = base64.b64decode(ciphertext)
        key = base64.b64decode(key)
        iv = ct[:AES.block_size]
        ct = ct[AES.block_size:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')
        return f"""
        ==========
        Your decrypted message is: {pt}
        ==========
        """
    except (ValueError, KeyError):
        return None
