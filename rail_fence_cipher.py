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

    return ''.join(rail)

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

    return ''.join(result)
