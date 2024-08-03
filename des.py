from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

def generate_key():
    return get_random_bytes(8)

def encrypt_des(plaintext, key):
    cipher = DES.new(key, DES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plaintext.encode('utf-8'), DES.block_size))
    iv = cipher.iv
    ct = base64.b64encode(iv + ct_bytes).decode('utf-8')
    encoded_key = base64.b64encode(key).decode('utf-8')
    return f"""
    ==========
    Your encrypted message is: {ct}
    Your key is: {encoded_key}
    Please keep this safe!
    ==========
    """

def decrypt_des(ciphertext, key):
    try:
        ct = base64.b64decode(ciphertext)
        key = base64.b64decode(key)
        iv = ct[:DES.block_size]
        ct = ct[DES.block_size:]
        cipher = DES.new(key, DES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), DES.block_size).decode('utf-8')
        return f"""
        ==========
        Your decrypted message is: {pt}
        ==========
        """
    except (ValueError, KeyError):
        return None
