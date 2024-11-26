from src.lab4.task2.respondent import Respondent


class Group:
    def __init__(self, min_age: int, max_age: int):
        self.min_age = min_age
        self.max_age = max_age
        self.respondents = []

    def __str__(self) -> str:
        if self.max_age == 123:
            return f'{self.min_age}+: {', '.join(str(respondent) for respondent in sorted(self.respondents))}'
        return f'{self.min_age}-{self.max_age}: {', '.join(str(respondent) for respondent in sorted(self.respondents))}'

    def add_respondent(self, new_respondent: Respondent):
        if self.min_age <= new_respondent.age <= self.max_age:
            self.respondents.append(new_respondent)

    def suitable_respondent(self, respondent: Respondent) -> bool:
        return self.min_age <= respondent.age <= self.max_age

    def have_respondents(self) -> bool:
        return len(self.respondents) > 0