import typing as tp
import re
from src.lab5.order import Order


def read_orders(orders_file_path: str) -> tp.List[tp.List[str]]:
    """Считывает список заказов"""
    orders = []
    with open(orders_file_path, encoding='utf-8') as orders_file:
        for line in orders_file.readlines():
            data = line.strip().split(';')
            data[1] = data[1].split(', ')
            orders.append(data)
    return orders


def validation_orders(data: tp.List[str]) -> tp.List[int]:
    """Проверяет заказ на валидность данных"""
    address = data[3].split(".")
    errors = []
    if not(len(address) == 4):
        if data[3] == "":
            error = f"{data[0]};1;no data"
        else:
            error = f"{data[0]};1;{data[3]}"
        errors.append(error)
    phone_number = data[4]
    phone_number_template = re.compile(r'\+\d-\d{3}-\d{3}-\d{2}-\d{2}$')
    if not phone_number_template.match(phone_number):
        if data[4] == "":
            error = f"{data[0]};2;no data"
        else:
            error = f"{data[0]};2;{data[4]}"
        errors.append(error)
    return errors


def write_orders(file_path: str, orders: tp.List[str]):
    """Записывает данные в указанный файл"""
    with open(file_path, 'wt', encoding='utf-8') as file:
        for order in orders:
            file.write(order + '\n')

if __name__ == "__main__":
    orders_file_path = "txtf/orders.txt"
    non_valid_orders_file_path = "txtf/non_valid_orders.txt"
    order_country_file_path = "txtf/order_country.txt"

    orders = read_orders(orders_file_path)

    non_valid_orders = []
    order_country = []

    for order in orders:
        errors = validation_orders(order)
        if errors == []:
            order_country.append(Order(*order))
        else:
            for error in errors:
                non_valid_orders.append(error)

    write_orders(non_valid_orders_file_path, non_valid_orders)

    order_country = [str(order) for order in sorted(order_country)]
    write_orders(order_country_file_path, order_country)