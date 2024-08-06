import mod
import trad
import rsa

def main():
  menu()

def menu():
  try:
    c = int(input("""
    Select the type of encryption you wish to perform: 
    1) Symmetric Encryption
    2) Asymmetric Encryption
    3) Quit
    """))
    if c == 1:
        sym_menu()
    elif c == 2:
        asym_menu()
    elif c == 3:
        print("""
        Thank you for using Crypt!
        """)
    else:
      print("""
      Invalid choice. Try again.
      """)
      menu()
  except ValueError:
    print("""
    Invalid input. Must be an integer. Try again.
    """)
    menu()

def sym_menu():
  try:
    s = int(input("""
    Select the type of cipher you wish to use:
    1) Traditional Cipher
    2) Modern Cipher
    3) Main Menu
    """))
    if s == 1:
      trad_ciphers()
    elif s == 2:
      mod_ciphers()
    elif s == 3:
      menu()
    else:
      print("""
      Invalid choice. Try again.
      """)
      sym_menu()
  except ValueError:
    print("""
    Invalid input. Must be an integer. Try again.
    """)
    sym_menu()

def asym_menu():
  a = int(input("""
  Select the type of Asymmetric cipher you wish to use:
  1) RSA (Rivist-Shamir-Adleman)
  """))

  if a == 1:
    print(rsa.asym_rsa())

def trad_ciphers():
    t = int(input("""
    Select the type of traditional cipher you wish to use:
    1) Caeser Cipher
    2) Autokey Cipher
    3) Rail Fence Cipher
    """))

    if t == 1:
      print(trad.caeser())
    elif t == 2:
      print(trad.autokey())
    elif t == 3:
      print(trad.rail_fence())

def mod_ciphers():
    m = int(input("""
    Select the type of modern cipher you wish to use:
    1) AES (Advanced Encryption Standard)
    2) DES (Data Encryption Standard)
    """))

    if m == 1:
      print(mod.mod_aes())
    elif m == 2:
      print(mod.mod_des())

main()