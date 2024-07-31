from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import sys

def main():
  menu()

def menu():
   c = int(input("""
   Select the type of encryption you wish to perform: 
   1) Symmetric Encryption
   2) Asymmetric Encryption
   """))

   if c == 1:
    sym_menu()
   elif c == 2:
    asym_menu()

def sym_menu():
  s = int(input("""
    Select the type of cipher you wish to use:
    1) Traditional Cipher
    2) Modern Cipher
    """))

  if s == 1:
    trad_ciphers()
  elif s == 2:
    mod_ciphers()

def asym_menu():
  a = int(input("""
  Select the type of Asymmetric cipher you wish to use:
  1) RSA (Rivist-Shamir-Adleman)
  """))

  if a == 1:
    rsa()

def rsa():
  print("This is the RSA cipher")

def trad_ciphers():
    t = int(input("""
    Select the type of traditional cipher you wish to use:
    1) Caeser Cipher
    2) Autokey Cipher
    3) Rail Fence Cipher
    """))

    if t == 1:
      caeser()
    elif t == 2:
      autokey()
    elif t == 3:
      rail()

def caeser():
  print("""
  CAESER CIPHER
  """)
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  m = ""
  pt = input("Input plaintext: ").upper()
  key = int(input("Input key: "))
  i = 0 
  while (i < len(pt)):
    c_i = alphabet.index(pt[i])
    m_i = (c_i + key) % 26
    m_e = alphabet[m_i]
    m += m_e
    i = i + 1
  print(f"""
  ==========
  Your encrypted message is: {m}.
  Your key is {key}. Please keep this safe!
  Decypher using the unsigned or signed inverse of the key.
  ==========
  """)

def autokey():
  print("""
  AUTOKEY CIPHER
  """)
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  m = ""
  i = 0
  question = input("Do you wish to (e)ncrypt or (d)ecrypt? ")
  if question == "e":   
    pt = input("Input plaintext: ").upper()
    key = input("Input key: ").upper()
    while (i < len(pt)):
      if (i < len(key)):
        k_element= key[i]
      else:
        k_element = pt[i - len(key)]
      m_i= (alphabet.index(pt[i]) + alphabet.index(k_element)) % 26
      m_e = alphabet[m_i]
      m += m_e
      i = i + 1
    print(f"""
    ==========
    Your encrypted message is: {m}.
    Your key is {key}. Please keep this safe!
    ==========
    """)
  elif question == "d":
    ct = input("Input ciphertext: ").upper()
    key = input("Input key: ").upper()
    while i < len(ct):
      if i < len(key):
        k_element= key[i]
      else:
        k_element = m[i - len(key)]
      m_i= (alphabet.index(ct[i]) - alphabet.index(k_element) + 26) % 26
      m_e = alphabet[m_i]
      m += m_e
      i = i + 1
    print(f"""
    ==========
    Your decrypted message is: {m}.
    ==========
    """)
    

def rail():
  print("This is the rail fence cipher")

def mod_ciphers():
    m = int(input("""
    Select the type of modern cipher you wish to use:
    1) AES (Advanced Encryption Standard)
    2) DES (Data Encryption Standard)
    """))

    if m == 1:
      aes()
    elif m == 2:
      des()

def aes():
  print("This is the AES cipher")

def des():
  print("This is the DES cipher")

main()