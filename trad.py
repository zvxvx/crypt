def caeser():
  print("""
  CAESER CIPHER
  """)
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  m = ""
  pt = input("Input plaintext or ciphertext: ").upper().strip()
  key = int(input("Input key or inverse key: "))
  i = 0 
  while i < len(pt):
    c_i = alphabet.index(pt[i])
    m_i = (c_i + key) % 26
    m_e = alphabet[m_i]
    m += m_e
    i = i + 1
  return f"""
  ==========
  Your encrypted message is: {m}.
  Your key is {key}. Please keep this safe!
  Decypher using the unsigned or signed inverse of the key.
  ==========
  """

def autokey():
  print("""
  AUTOKEY CIPHER
  """)
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  m = ""
  i = 0
  question = input("Do you wish to (e)ncrypt or (d)ecrypt? ")
  if question == "e":   
    pt = input("Input plaintext: ").upper().strip()
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
    Your key is {key}. Please keep this safe!
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

def encrypt_rail_fence(plaintext, num_rails):
    rail = [''] * num_rails
    direction = None
    row = 0

    for char in plaintext:
        rail[row] += char
        if row == 0:
            direction = 1
        elif row == num_rails - 1:
            direction = -1
        row += direction

    return f"""
    ==========
    Your encrypted message is: {''.join(rail)}.
    Your key is {num_rails}. Please keep this safe!
    ==========
    """

def decrypt_rail_fence(ciphertext, num_rails):
    rail_len = len(ciphertext)
    rail = [['\n' for _ in range(rail_len)] for _ in range(num_rails)]
    
    direction = None
    row, col = 0, 0

    for _ in range(rail_len):
        rail[row][col] = '*'
        col += 1
        if row == 0:
            direction = 1
        elif row == num_rails - 1:
            direction = -1
        row += direction
    
    index = 0
    for i in range(num_rails):
        for j in range(rail_len):
            if rail[i][j] == '*' and index < rail_len:
                rail[i][j] = ciphertext[index]
                index += 1
    
    result = []
    row, col = 0, 0
    for _ in range(rail_len):
        result.append(rail[row][col])
        col += 1
        if row == 0:
            direction = 1
        elif row == num_rails - 1:
            direction = -1
        row += direction

    return f"""
    ==========
    Your decrypted message is: {''.join(result)}.
    ==========
    """

def rail_fence():
  question = input("Do you wish to (e)ncrypt or (d)ecrypt? ")
  if question == "e":
    pt = input("Input plaintext: ").strip()
    rails = int(input("Number of rails: "))
    return encrypt_rail_fence(pt, rails)
  elif question == "d":
    ct = input("Input ciphertext: ").strip()
    rails = int(input("Number of rails: "))
    return decrypt_rail_fence(ct, rails)