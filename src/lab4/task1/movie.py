class Movie:
    def __init__(self, _id: int, name: str):
        self.id = _id
        self.name = name

    def return_name(self) -> str:
        """Возвращает название фильма"""
        return self.name