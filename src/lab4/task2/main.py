import typing as tp
from src.lab4.task2.respondent import Respondent
from src.lab4.task2.group import Group


def create_groups(borders_groups: str) -> tp.List[Group]:
    borders_groups = [-1] + [int(elem) for elem in borders_groups.split()] + [123]
    groups = []
    for i in range(len(borders_groups) - 1):
        groups.append(Group(borders_groups[i] + 1, borders_groups[i + 1]))
    return groups


def read_respondents(groups: tp.List[Group]):
    """Считывает респондентов из стандартного потока"""
    respondent = input()
    while respondent != 'END':
        name, age = respondent.split(',')
        add_respondent_to_group(Respondent(name, int(age)), groups)
        respondent = input()

def add_respondent_to_group(respondent: Respondent, groups: tp.List[Group]):
    """Добавляет нового респондента в подходящую по возрасту группу"""
    for group in groups:
        if group.suitable_respondent(respondent):
            group.add_respondent(respondent)
            return


def main(borders_groups: str):
    groups = create_groups(borders_groups)
    read_respondents(groups)
    groups.sort(key=lambda group: group.min_age, reverse=True)

    for group in groups:
        if group.have_respondents():
            print(group)
            print()



if __name__ == "__main__":
    borders_groups = input()
    main(borders_groups)

# 18 25 35 45 60 80 100
# Ярилова Розалия Трофимовна,29
# Старостин Ростислав Ермолаевич,50
# Иванов Варлам Якунович,88
# Соколов Андрей Сергеевич,15
# Дьячков Нисон Иринеевич,88
# Егоров Алан Петрович,7
# Кошельков Захар Брониславович,105
# END