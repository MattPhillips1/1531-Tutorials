from abc import ABC, abstractmethod


class Movie(ABC):
    """
    The base class of a movie.
    Each genre of movie defines its own daily rate
    If later on a new genre of movie needs to be added, then just need to
    create a movie class for this genre that extends from this base class
    """
    @abstractmethod
    def __init__(self, title, daily_rate):
        self._title = title
        self._daily_rate = daily_rate

    @property
    def title(self):
        return self._title

    @property
    def daily_rate(self):
        return self._daily_rate


class Regular(Movie):
    def __init__(self, title):
        super().__init__(title, 2.0)


class NewRelease(Movie):
    def __init__(self, title):
        super().__init__(title, 3.0)


class Children(Movie):
    def __init__(self, title):
        super().__init__(title, 3.0)


class Rental(object):
    def __init__(self, movie, daysRented):
        """
        :param movie: movie rented
        :param daysRented: number of days rented
        """
        self._movie = movie
        self._daysRented = daysRented

    def calculate_rental(self):
        rental_cost = self._movie.daily_rate * self._daysRented
        return rental_cost


movie = Regular("Gone with the wind")
rental = Rental(movie, 4)
print(rental.calculate_rental())
