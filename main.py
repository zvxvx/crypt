import aes
import des
import rail_fence_cipher
import rsa

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
    asym_rsa()

def asym_rsa():
  key_question = input("Generate new public and private keys? y/n ")
  if key_question == "y":
    rsa.generate_keys()
    print("Keys have been generated in files private.pem and receiver.pem")
  elif key_question == "n":
    # This does not currently work. Keys need to be pulled in from files and not through console input!!!!
    question = input("Do you wish to (e)ncrypt or (d)ecrypt? ")
    if question == "e":
      pt = input("Input plaintext: ").strip()
      key = null # will be pulled from file 
      print(f"Your encrypted message: {rsa.encrypt_rsa(pt, key)}")
    if question == "d":
      ct = input("Input ciphertext: ").strip()
      key = null # will be pulled from file 
      print(rsa.decrypt_rsa(ct, key))

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
  while i < len(pt):
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
    while i < len(pt):
      if i < len(key):
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
  question = input("Do you wish to (e)ncrypt or (d)ecrypt? ")
  if question == "e":
    pt = input("Input plaintext: ")
    rails = int(input("Number of rails: "))
    print(rail_fence_cipher.encrypt_rail_fence(pt, rails))
  elif question == "d":
    ct = input("Input ciphertext: ")
    rails = int(input("Number of rails: "))
    print(rail_fence_cipher.decrypt_rail_fence(ct, rails))

def mod_ciphers():
    m = int(input("""
    Select the type of modern cipher you wish to use:
    1) AES (Advanced Encryption Standard)
    2) DES (Data Encryption Standard)
    """))

    if m == 1:
      mod_aes()
    elif m == 2:
      mod_des()

def mod_aes():
  question = input("Do you wish to (e)ncrypt or (d)ecrypt? ")
  if question == "e":
    key = aes.generate_key()
    pt = input("Input plaintext " )
    print(aes.encrypt_aes(pt, key))
  elif question == "d":
    ct = input("Please input ciphertext: ")
    key = input("Please input your key: ")
    print(aes.decrypt_aes(ct, key))

def mod_des():
  question = input("Do you wish to (e)ncrypt or (d)ecrypt? ")
  if question == "e":
    key = des.generate_key()
    pt = input("Input plaintext " )
    print(des.encrypt_des(pt, key))
  elif question == "d":
    ct = input("Please input ciphertext: ")
    key = input("Please input your key: ")
    print(des.decrypt_des(ct, key))

main()