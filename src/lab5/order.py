import typing as tp


class Order:
    def __init__(self, number: str, products: tp.List[str], full_name: str, address: str, phone_number: str,
                 priority: str):
        self.number = number
        self.products = products
        self.full_name = full_name
        self.country = address.split('. ')[0]
        self.address = address[address.index('.') + 2:]
        self.phone_number = phone_number
        self.priority = priority
        if priority == "MAX":
            self.priority_number = 1
        elif priority == "MIDDLE":
            self.priority_number = 2
        else:
            self.priority_number = 3
        self._sorted_list_product()

    def __str__(self) -> str:
        return f"{self.number};{self.products};{self.full_name};{self.address};{self.phone_number};{self.priority}"

    def __lt__(self, other_order) -> bool:
        if self.country == other_order.country == "Россия":
            return self.priority_number <= other_order.priority_number
        elif self.country == "Россия":
            return True
        elif other_order.country == "Россия":
            return False
        elif self.country == other_order.country:
            return self.priority_number <= other_order.priority_number
        return self.country <= other_order.country

    def _sorted_list_product(self):
        set_products = list(set(self.products))
        if len(set_products) == len(self.products):
            self.products = ", ".join(sorted(self.products))
        sorted_products = []
        for elem in set_products:
            sorted_products.append(f"{elem} x{self.products.count(elem)}")
        self.products = ", ".join(sorted(sorted_products))
