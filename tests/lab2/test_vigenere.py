import unittest
import random
import string
from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere


class VigenereTestCase(unittest.TestCase):
    def test_randomized(self):
        kwlen = random.randint(4, 24)
        keyword = ''.join(random.choice(string.ascii_letters) for _ in range(kwlen))
        plaintext = ''.join(random.choice(string.ascii_letters + ' -,') for _ in range(64))
        ciphertext = encrypt_vigenere(plaintext, keyword)
        self.assertEqual(plaintext, decrypt_vigenere(ciphertext, keyword))

    def test_vigenere_1(self):
        self.assertEqual(encrypt_vigenere('Hello world!', 'aaa'), 'Hello world!')

    def test_vigenere_2(self):
        self.assertEqual(encrypt_vigenere('Hello world!', 'b'), 'Ifmmp xpsme!')

    def test_vigenere_3(self):
        self.assertEqual(decrypt_vigenere('Ifmmp xpsme!', 'b'), 'Hello world!')
