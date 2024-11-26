import pandas as pd
import typing as tp


class User:
    def __init__(self, _id: int, movies: tp.List[int]):
        self.id = _id
        self.movies = movies

    def get_unique_films(self, other_movies: tp.List[int]) -> tp.Dict[int, float]:
        """Возвращает список рекомендованных фильмов с весом, в зависиммости от рассчитаного коэффециента"""

        coefficient = self.get_coefficient(other_movies)

        movies_recommendations = {}
        if coefficient >= 0.5:
            for film in self.movies:
                if film not in other_movies:
                    movies_recommendations[film] = movies_recommendations.get(film, 0) + 1
            movies_recommendations.update(
                (key, float(value * coefficient)) for key, value in movies_recommendations.items())
        return movies_recommendations

    def get_coefficient(self, other_movies: tp.List[int]) -> float:
        """Подсчитывает коэффициент в зависимости от общих просмотренных фильмов"""
        general = pd.Series(map(' '.join, map(str, other_movies))).isin(
            list(map(' '.join, map(str, self.movies)))).sum()
        coefficient = round(general / len(other_movies), 2)
        return coefficient
