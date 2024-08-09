def caeser():
  print("""
 ██████╗███████╗ █████╗ ███████╗███████╗██████╗ 
██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗
██║     █████╗  ███████║███████╗█████╗  ██████╔╝
██║     ██╔══╝  ██╔══██║╚════██║██╔══╝  ██╔══██╗
╚██████╗███████╗██║  ██║███████║███████╗██║  ██║
 ╚═════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
  """)
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  m = ""
  pt = input("Input plaintext w/o punctuation or spaces, or input ciphertext: ").upper().strip()
  try:
    key = int(input("Input numerical key or inverse key: "))
  except ValueError:
    print("""
    Key must be a number. Try again.
    """)
    key = int(input("Input numerical key or inverse key: "))
  i = 0 
  while i < len(pt):
    c_i = alphabet.index(pt[i])
    m_i = (c_i + key) % 26
    m_e = alphabet[m_i]
    m += m_e
    i = i + 1
  return f"""
  ==========
  Your caeser output is: {m}.
  Your key is {key}. 
  Please keep this safe!
  Decypher using the unsigned or signed inverse of the key.
  ==========
  """

def autokey():
  print("""
 █████╗ ██╗   ██╗████████╗ ██████╗ ██╗  ██╗███████╗██╗   ██╗
██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝╚██╗ ██╔╝
███████║██║   ██║   ██║   ██║   ██║█████╔╝ █████╗   ╚████╔╝ 
██╔══██║██║   ██║   ██║   ██║   ██║██╔═██╗ ██╔══╝    ╚██╔╝  
██║  ██║╚██████╔╝   ██║   ╚██████╔╝██║  ██╗███████╗   ██║   
╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝   ╚═╝   
  """)
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  m = ""
  i = 0
  question = input("Do you wish to (e)ncrypt or (d)ecrypt? ")
  if question == "e":   
    pt = input("Input plaintext w/o punctuation or spaces: ").upper().strip()
    key = input("Input key: ").upper().strip()
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
    Your key is {key}. 
    Please keep this safe!
    ==========
    """)
  elif question == "d":
    ct = input("Input ciphertext: ").upper().strip()
    key = input("Input key: ").upper().strip()
    while i < len(ct):
      if i < len(key):
        k_element= key[i]
      else:
        k_element = m[i - len(key)]
      m_i= (alphabet.index(ct[i]) - alphabet.index(k_element) + 26) % 26
      m_e = alphabet[m_i]
      m += m_e
      i = i + 1
    return f"""
    ==========
    Your decrypted message is: {m}.
    ==========
    """
  else:
    print("""
    Invalid option. Try again.
    """)
    autokey()

def encrypt_rail_fence(plaintext, num_rails):
    rail = [['' for _ in range(len(plaintext))] for _ in range(num_rails)]

    dir_down = False
    row, col = 0, 0

    for i in range(len(plaintext)):
        if (row == 0) or (row == num_rails - 1):
            dir_down = not dir_down

        rail[row][col] = plaintext[i]
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    result = []
    for i in range(num_rails):
        for j in range(len(plaintext)):
            if rail[i][j] != '':
                result.append(rail[i][j])

    encrypted_message = ''.join(result)

    return f"""
    ==========
    Your encrypted message is: {encrypted_message}.
    Your key is {num_rails}.
    Please keep this safe!
    ==========
    """

def decrypt_rail_fence(ciphertext, num_rails):
    rail = [['\n' for i in range(len(ciphertext))] for j in range(num_rails)]

    dir_down = None
    row, col = 0, 0

    for i in range(len(ciphertext)):
        if row == 0:
            dir_down = True
        if row == num_rails - 1:
            dir_down = False

        rail[row][col] = '*'
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(num_rails):
        for j in range(len(ciphertext)):
            if (rail[i][j] == '*') and (index < len(ciphertext)):
                rail[i][j] = ciphertext[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(ciphertext)):

        if row == 0:
            dir_down = True
        if row == num_rails - 1:
            dir_down = False

        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    return f"""
    ==========
    Your decrypted message is: {''.join(result)}.
    ==========
    """

def rail_fence():
  print("""
██████╗  █████╗ ██╗██╗     ███████╗███████╗███╗   ██╗ ██████╗███████╗
██╔══██╗██╔══██╗██║██║     ██╔════╝██╔════╝████╗  ██║██╔════╝██╔════╝
██████╔╝███████║██║██║     █████╗  █████╗  ██╔██╗ ██║██║     █████╗  
██╔══██╗██╔══██║██║██║     ██╔══╝  ██╔══╝  ██║╚██╗██║██║     ██╔══╝  
██║  ██║██║  ██║██║███████╗██║     ███████╗██║ ╚████║╚██████╗███████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚══════╝
  """)
  question = input("Do you wish to (e)ncrypt or (d)ecrypt? ")
  if question == "e":
    pt = input("Input plaintext: ").strip()
    rails = int(input("Number of rails: "))
    return encrypt_rail_fence(pt, rails)
  elif question == "d":
    ct = input("Input ciphertext: ").strip()
    rails = int(input("Number of rails: "))
    return decrypt_rail_fence(ct, rails)
  else:
    print("""
    Invalid option. Try again.
    """)
    rail_fence()
