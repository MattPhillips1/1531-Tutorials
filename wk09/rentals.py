class Movie(object):
    # Movie Types
    REGULAR = 0
    CHILDREN = 1
    NEW_RELEASE = 2

    def __init__(self, title, pricecode):
        """
        :param flight_number: string of flight number
        :param distance: distance in kilometres
        :param aircarft: Flag of the aircraft type
        """
        self._title = title
        self._price_code = pricecode


class Rental(object):
    def __init__(self, movie, days_rented):
        """
        :param movie: movie rented
        :param daysRented: number of days rented
        """
        self._movie = movie
        self._days_rented = days_rented

    def calculate_rental(self):
        rental_cost = 0
        if self._movie._price_code == Movie.REGULAR:
            rental_cost = 2.0 * self._days_rented
        elif self._movie._price_code == Movie.NEW_RELEASE:
            rental_cost = 3.0 * self._days_rented
        elif self._movie._price_code == Movie.CHILDREN:
            rental_cost = 1.5 * self._days_rented
        return rental_cost


movie = Movie("Gone with the wind", Movie.REGULAR)
rental = Rental(movie, 4)
print(rental.calculate_rental())
