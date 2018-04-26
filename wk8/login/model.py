from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, uid):
        self.id = uid
