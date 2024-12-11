import unittest
from src.lab5.order import Order
from src.lab5.main import validation_orders


class RespondentsTestCase(unittest.TestCase):

    def test_order(self):
        order = Order("46590", ["Колбаса", "Сыр", "Сыр"], "Журбина Марина",
                      "Россия. Ленинградская область. Санкт-Петербург. Альпийский переулок",
                      "+7-908-556-43-45", "MAX")

        self.assertEqual(str(order),
                         "46590;Колбаса x1, Сыр x2;Журбина Марина;Ленинградская область. Санкт-Петербург. Альпийский переулок;+7-908-556-43-45;MAX")

        order2 = Order("46592", ["Колбаса", "Сыр", "Сыр"], "Журбина Марина",
                       "Россия. Ленинградская область. Санкт-Петербург. Альпийский переулок",
                       "+7-908-556-43-45", "MIDDLE")
        self.assertEqual(order < order2, True)

        order3 = Order("43592", ["Колбаса", "Сыр", "Сыр"], "Журбина Марина",
                       "Италия. Лацио. Рим. Колизей", "+7-908-556-43-45", "MIDDLE")
        order4 = Order("43542", ["Колбаса", "Сыр", "Сыр"], "Журбина Марина",
                       "Германия. Бавария. Мюнхен. Мариенплац", "+7-908-556-43-45", "MIDDLE")
        order5 = Order("43543", ["Колбаса", "Сыр", "Сыр"], "Журбина Марина",
                       "Германия. Бавария. Мюнхен. Кауфингерштрассе", "+7-908-556-43-45", "LOW")

        self.assertEqual(order < order3, True)
        self.assertEqual(order2 < order4, True)
        self.assertEqual(order3 < order4, False)
        self.assertEqual(order4 < order5, True)

    def test_validation_orders(self):
        orders = [["43592", ["Колбаса", "Сыр", "Сыр"], "Журбина Марина", "Лацио. Рим. Колизей", "+7-908-556-43-45", "MIDDLE"],
                  ["43542", ["Колбаса", "Сыр", "Сыр"], "Журбина Марина", "Германия. Бавария. Мюнхен. Мариенплац", "+7-908-53356-43-45", "MIDDLE"],
                  ["43543", ["Колбаса", "Сыр", "Сыр"], "Журбина Марина", "Германия. Бавария. Мюнхен. Кауфингерштрассе", "+7-908-556-43-45", "LOW"],
                  ["46592", ["Колбаса", "Сыр", "Сыр"], "Журбина Марина", "Россия. Ленинградская область.", "+7-908-43-45", "MIDDLE"],
                  ["56592", ["Колбаса", "Сыр", "Сыр"], "Журбина Марина", "", "+7-908-556-43-45", "MIDDLE"]]

        self.assertEqual(validation_orders(orders[0]), ["43592;1;Лацио. Рим. Колизей"])
        self.assertEqual(validation_orders(orders[1]), ["43542;2;+7-908-53356-43-45"])
        self.assertEqual(validation_orders(orders[3]), ["46592;1;Россия. Ленинградская область.", "46592;2;+7-908-43-45"])
        self.assertEqual(validation_orders(orders[2]), [])
        self.assertEqual(validation_orders(orders[4]), ["56592;1;no data"])