import typing as tp
from src.lab4.task1.user import User
from src.lab4.task1.movie import Movie


def read_movies(movies_file_path: str) -> tp.Dict[int, Movie]:
    """Считывает список фильмов и преобразовывает в словарь"""
    movies = {}
    with open(movies_file_path, encoding='utf-8') as movies_file:
        for line in movies_file.readlines():
            _id, name = line.strip().split(',')
            movies[int(_id)] = Movie(int(_id), name)
    return movies


def read_users(users_file_path: str) -> tp.List[User]:
    """Считывает список пользователей и преобразовывает в список"""
    users = []
    with open(users_file_path) as users_file:
        data = [[int(elem) for elem in line.strip().split(',')] for line in users_file.readlines()]
        for i in range(len(data)):
            users.append(User(i, data[i]))
    return users


def main(data: tp.List[int], users_file_path: str, movies_file_path: str):
    users = read_users(users_file_path)
    movies = read_movies(movies_file_path)

    recommendations = [user.get_unique_films(data) for user in users]
    movies_recommendation = {}
    for recommend in recommendations:
        for key, value in recommend.items():
            movies_recommendation[key] = movies_recommendation.get(key, 0) + value

    movies_recommendation = sorted(movies_recommendation.items(), key=lambda item: item[1])
    movie_recomend_id = movies_recommendation[-1][0]  # Фильм с наибольшим весов
    return movies[movie_recomend_id].return_name()


if __name__ == "__main__":
    users_file_path = "txtf/users.txt"
    movies_file_path = "txtf/movies.txt"

    data = [int(elem) for elem in input().split(',')]
    print(main(data, users_file_path, movies_file_path))
