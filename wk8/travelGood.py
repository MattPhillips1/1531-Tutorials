from abc import ABC, abstract_method


class Transport(ABC):
    @abstract_method
    def move(self):
        pass

class Car(Transport):
    def move(self):
        print("car moving..")


class Bike(Transport):
    def move(self):
        print("bike moving..")


class Traveller():
    def __init__(self, mode_travel):
        self._mode_travel = mode_travel

    def start_journey(self):
        self._mode_travel.move()


sam = Traveller()
sam.start_journey()
