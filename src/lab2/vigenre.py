def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword = (keyword * (len(plaintext) // len(keyword) + 1)).lower()
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            flag = False
            if plaintext[i].isupper():
                x = ord(plaintext[i].lower())
                flag = True
            else:
                x = ord(plaintext[i])
            shift = ord(keyword[i]) - 97
            if x + shift > 122:
                x = (x + shift) % 122 + 96
            else:
                x += shift
            x = chr(x)
            if flag:
                x = x.upper()
            ciphertext += x
        else:
            ciphertext += plaintext[i]
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword = (keyword * (len(ciphertext) // len(keyword) + 1)).lower()
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            flag = False
            if ciphertext[i].isupper():
                x = ord(ciphertext[i].lower())
                flag = True
            else:
                x = ord(ciphertext[i])
            shift = ord(keyword[i]) - 97
            if x - shift < 97:
                x = 123 - (97 - x + shift) % 26
            else:
                x -= shift
            x = chr(x)
            if flag:
                x = x.upper()
            plaintext += x
        else:
            plaintext += ciphertext[i]
    return plaintext