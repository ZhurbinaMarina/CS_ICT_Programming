import unittest
from src.lab4.task2.group import Group
from src.lab4.task2.respondent import Respondent


class RespondentsTestCase(unittest.TestCase):

    def test_group(self):
        group = Group(19, 25)
        self.assertEqual(group.have_respondents(), False)

        group.add_respondent(Respondent("Соколов Андрей Сергеевич", 15))
        self.assertEqual(group.have_respondents(), False)

        group.add_respondent(Respondent("Егоров Алан Петрович", 20))
        self.assertEqual(group.have_respondents(), True)

        self.assertEqual(group.suitable_respondent(Respondent("Дьячков Нисон Иринеевич", 25)), True)
        self.assertEqual(group.suitable_respondent(Respondent("Иванов Варлам Якунович", 88)), False)

        group.add_respondent(Respondent("Дьячков Нисон Иринеевич", 25))
        self.assertEqual(str(group), "19-25: Дьячков Нисон Иринеевич (25), Егоров Алан Петрович (20)")

