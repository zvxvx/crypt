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
  encrypted = ""
  pt = input("Input plaintext: ").upper()
  key = int(input("Input key: "))
  i = 0 
  while (i < len(pt)):
    c = alphabet.index(pt[i])
    newIndex = (c + key) % 26
    newChar = alphabet[newIndex]
    encrypted += newChar
    i = i + 1
  print(f"""
  ==========
  Your encrypted message is: {encrypted}.
  Your key is {key}. Please keep this safe!
  Decypher using the unsigned or signed inverse of the key.
  ==========
  """)

def autokey():
  print("This is the autokey cipher")

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