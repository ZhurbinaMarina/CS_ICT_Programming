def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ''
    for elem in plaintext:
        if elem.isalpha():
            flag = False
            if elem.isupper():
                elem = elem.lower()
                flag = True
            x = ord(elem)
            if x + shift > 122:
                x = (x + shift) % 122 + 96
            else:
                x += shift
            x = chr(x)
            if flag:
                x = x.upper()
            ciphertext += x
        else:
            ciphertext += elem
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for elem in ciphertext:
        if elem.isalpha():
            flag = False
            if elem.isupper():
                elem = elem.lower()
                flag = True
            x = ord(elem)
            if x - shift < 97:
                x = 123 - (97 - x + shift) % 26
            else:
                x -= shift
            x = chr(x)
            if flag:
                x = x.upper()
            plaintext += x
        else:
            plaintext += elem
    return plaintext
