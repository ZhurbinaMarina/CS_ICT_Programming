import unittest
import random
import string
from src.lab2.caesar import decrypt_caesar, encrypt_caesar


class CaesarTestCase(unittest.TestCase):
    def test_caesar_1(self):
        self.assertEqual(encrypt_caesar('Hello world!'), 'Khoor zruog!')

    def test_caesar_2(self):
        self.assertEqual(encrypt_caesar('Hello world!', 5), 'Mjqqt btwqi!')

    def test_caesar_3(self):
        self.assertEqual(decrypt_caesar('Mjqqt btwqi!', 5), 'Hello world!')
