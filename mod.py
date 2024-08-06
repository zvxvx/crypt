from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Cipher import DES
import base64

# AES CIPHER

def generate_key_aes():
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
    Your key is: {encoded_key}
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

def mod_aes():
  question = input("Do you wish to (e)ncrypt or (d)ecrypt? ")
  if question == "e":
    key = generate_key_aes()
    pt = input("Input plaintext: " ).strip()
    return encrypt_aes(pt, key)
  elif question == "d":
    ct = input("Please input ciphertext: ").strip()
    key = input("Please input your key: ").strip()
    return decrypt_aes(ct, key)
  else:
    print("""
    Invalid option. Try again.
    """)
    mod_aes()
    

# DES CIPHER

def generate_key_des():
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

def mod_des():
  question = input("Do you wish to (e)ncrypt or (d)ecrypt? ")
  if question == "e":
    key = generate_key_des()
    pt = input("Input plaintext: " ).strip()
    return encrypt_des(pt, key)
  elif question == "d":
    ct = input("Please input ciphertext: ").strip()
    key = input("Please input your key: ").strip()
    return decrypt_des(ct, key)
  else:
    print("""
    Invalid option. Try again.
    """)
    mod_des()