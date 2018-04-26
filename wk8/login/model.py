from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, uid, name):
        self.id = uid
        self._name = name

    @property
    def name(self):
        return self._name
