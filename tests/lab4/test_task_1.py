import unittest
from src.lab4.task1.main import main
from src.lab4.task1.user import User

USERS_FILE_PATH = "txtf/users.txt"
MOVIES_FILE_PATH = "txtf/movies.txt"

class RecommenderTestCase(unittest.TestCase):

    def test_main(self):
        self.assertEqual(main([2, 5], USERS_FILE_PATH, MOVIES_FILE_PATH), "Унесенные призраками")
        self.assertEqual(main([2, 4], USERS_FILE_PATH, MOVIES_FILE_PATH), "Дюна")
        self.assertEqual(main([1], USERS_FILE_PATH, MOVIES_FILE_PATH), "Унесенные призраками")
        self.assertEqual(main([2, 4], USERS_FILE_PATH, MOVIES_FILE_PATH), "Дюна")
        self.assertEqual(main([1, 4], USERS_FILE_PATH, MOVIES_FILE_PATH), "Дюна")
        self.assertEqual(main([4], USERS_FILE_PATH, MOVIES_FILE_PATH), "Гарри Поттер и философский камень")
        self.assertEqual(main([1, 3], USERS_FILE_PATH, MOVIES_FILE_PATH), "Хатико")

    def test_user_coefficient(self):
        user = User(1, [1, 2, 2, 2, 3, 5, 5, 7, 9])

        self.assertEqual(user.get_coefficient([1, 2, 3]), 1.0)
        self.assertEqual(user.get_coefficient([1, 2, 4, 6]), 0.5)
        self.assertEqual(user.get_coefficient([1, 2, 3, 4]), 0.75)
        self.assertEqual(user.get_coefficient([1, 4, 6, 8]), 0.25)

    def test_user_unique_films(self):
        user = User(2, [2, 3, 4, 4, 5, 8, 8, 8, 9])

        self.assertEqual(user.get_unique_films([2, 3, 4]), {5: 1.0, 8: 3.0, 9: 1.0})
        self.assertEqual(user.get_unique_films([1, 2, 6, 8]), {3: 0.5, 4: 1.0, 5: 0.5, 9: 0.5})
        self.assertEqual(user.get_unique_films([1, 2, 3, 4]), {5: 0.75, 8: 2.25, 9: 0.75})
        self.assertEqual(user.get_unique_films([1, 2, 6, 7]), {})
