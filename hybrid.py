def caesar_cipher(text, key, encrypt=True):
    """Applies Caesar cipher with given key for encryption/decryption."""
    result = ""
    shift = key if encrypt else -key  # Shift forward for encryption, backward for decryption
   
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result

def rail_fence_encrypt(text, rails):
    """Encrypts using Rail Fence cipher with given number of rails."""
    fence = [['\n' for _ in range(len(text))] for _ in range(rails)]
    direction_down = False
    row, col = 0, 0

    for char in text:
        if row == 0 or row == rails - 1:
            direction_down = not direction_down
       
        fence[row][col] = char
        col += 1
        row += 1 if direction_down else -1

    result = ''.join(char for row in fence for char in row if char != '\n')
    return result

def rail_fence_decrypt(text, rails):
    """Decrypts Rail Fence cipher with given number of rails."""
    fence = [['\n' for _ in range(len(text))] for _ in range(rails)]
    direction_down = None
    row, col = 0, 0

    for i in range(len(text)):
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False
       
        fence[row][col] = '*'
        col += 1
        row += 1 if direction_down else -1

    index = 0
    for i in range(rails):
        for j in range(len(text)):
            if fence[i][j] == '*' and index < len(text):
                fence[i][j] = text[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(text)):
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False
       
        result.append(fence[row][col])
        col += 1
        row += 1 if direction_down else -1
   
    return ''.join(result)

def hybrid_encrypt(text, caesar_key, rail_rails):
    """First applies Caesar cipher, then Rail Fence transposition."""
    caesar_encrypted = caesar_cipher(text, caesar_key, encrypt=True)
    rail_encrypted = rail_fence_encrypt(caesar_encrypted, rail_rails)
    return rail_encrypted

def hybrid_decrypt(text, caesar_key, rail_rails):
    """First applies Rail Fence decryption, then Caesar decryption."""
    rail_decrypted = rail_fence_decrypt(text, rail_rails)
    caesar_decrypted = caesar_cipher(rail_decrypted, caesar_key, encrypt=False)
    return caesar_decrypted

# Example Usage
plaintext = "HELLOHYBRID"
caesar_key = 3  # Shift for Caesar cipher
rail_rails = 3  # Number of rails for Rail Fence cipher

encrypted_text = hybrid_encrypt(plaintext, caesar_key, rail_rails)
decrypted_text = hybrid_decrypt(encrypted_text, caesar_key, rail_rails)

print(f"Original Text: {plaintext}")
print(f"Encrypted Text: {encrypted_text}")
print(f"Decrypted Text: {decrypted_text}")