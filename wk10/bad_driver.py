class Car(object):
    def __init__(self, name, model, rego):
        self._name = name
        self._model = model
        self._rego = rego


class IllegalSpeed(Exception):
    def __init__(self, car, speed, msg=None):
        if msg is None:
            msg = "An error occurred with car %s" % car
        super().__init__()
        self.car = car
        self.speed = speed


def drive_car(car, speed):
    try:
        if speed > 100:
            raise IllegalSpeed(car, speed, "Car %s caught for driving at speed %d" % (car, speed))
    except IllegalSpeed as error:
        if error.speed >= 120:
            call_000()


def call_000():
    print("calling 000")

my_car = Car("mercedes", "glc coupe", "xyz133")
drive_car(my_car, 180)
