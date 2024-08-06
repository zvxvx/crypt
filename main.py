import mod
import trad
import rsa

def main():
  print("""
                                                          
                                                   █    
                                                  ██    
                                                  ██    
           ███  ████   ██   ████        ████    ████████
    ████    ████ ████ █ ██    ███  █   █ ███  █████████ 
   █ ███  █  ██   ████  ██     ████   █   ████    ██    
  █   ████   ██         ██      ██   ██    ██     ██    
 ██          ██         ██      ██   ██    ██     ██    
 ██          ██         ██      ██   ██    ██     ██    
 ██          ██         ██      ██   ██    ██     ██    
 ██          ██         ██      ██   ██    ██     ██    
 ███     █   ███         █████████   ███████      ██    
  ███████     ███          ████ ███  ██████        ██   
   █████                         ███ ██                 
                          █████   █████                 
                        ████████  ██ ██                 
                       █      ████    ██                
 A friendly command-line application for encryption.                                                        
  """)
  return menu()

def menu():
  try:
    c = int(input("""
    Select the type of encryption you wish to perform: 
    1) Symmetric Encryption
    2) Asymmetric Encryption
    3) Quit
    """))
    if c == 1:
        return sym_menu()
    elif c == 2:
        return asym_menu()
    elif c == 3:
        print("""
        Thank you for using Crypt!
        """)
    else:
      print("""
      Invalid choice. Try again.
      """)
      return menu()
  except ValueError:
    print("""
    Invalid input. Must be an integer. Try again.
    """)
    return menu()

def sym_menu():
  try:
    s = int(input("""
    Select the type of cipher you wish to use:
    1) Traditional Cipher
    2) Modern Cipher
    3) Go Back
    """))
    if s == 1:
      return trad_ciphers()
    elif s == 2:
      return mod_ciphers()
    elif s == 3:
      return menu()
    else:
      print("""
      Invalid choice. Try again.
      """)
      return sym_menu()
  except ValueError:
    print("""
    Invalid input. Must be an integer. Try again.
    """)
    return sym_menu()

def asym_menu():
  try:
    a = int(input("""
    Select the type of Asymmetric cipher you wish to use:
    1) RSA (Rivist-Shamir-Adleman)
    2) Go Back
    """))
    if a == 1:
      print(rsa.asym_rsa())
      return menu()
    elif a == 2:
      return menu()
    else:
      print("""
      Invalid choice. Try again.
      """)
      return asym_menu()
  except ValueError:
    print("""
    Invalid input. Must be an integer. Try again.
    """)
    return asym_menu()

def trad_ciphers():
  try:
    t = int(input("""
    Select the type of traditional cipher you wish to use:
    1) Caeser Cipher
    2) Autokey Cipher
    3) Rail Fence Cipher
    4) Go Back
    """))
    if t == 1:
      print(trad.caeser())
      return menu()
    elif t == 2:
      print(trad.autokey())
      return menu()
    elif t == 3:
      print(trad.rail_fence())
      return menu()
    elif t == 4:
      return sym_menu()
    else:
      print("""
      Invalid choice. Try again.
      """)
      return trad_ciphers()
  except ValueError:
    print("""
    Invalid input. Must be an integer. Try again.
    """)
    return trad_ciphers()

def mod_ciphers():
  try:
    m = int(input("""
    Select the type of modern cipher you wish to use:
    1) AES (Advanced Encryption Standard)
    2) DES (Data Encryption Standard)
    3) Go Back
    """))
    if m == 1:
      print(mod.mod_aes())
      return menu()
    elif m == 2:
      print(mod.mod_des())
      return menu()
    elif m == 3:
      return sym_menu()
    else:
      print("""
      Invalid choice. Try again.
      """)
      return mod_ciphers()
  except ValueError:
    print("""
    Invalid input. Must be an integer. Try again.
    """)
    return mod_ciphers()


main()