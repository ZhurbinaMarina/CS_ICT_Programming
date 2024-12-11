class Respondent:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'{self.name} ({self.age})'

    def __lt__(self, other_respondent) -> bool:
        if self.age > other_respondent.age:
            return True
        elif self.age < other_respondent.age:
            return False
        return self.name < other_respondent.name
