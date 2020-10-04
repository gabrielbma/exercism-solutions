import random


class Robot:

    _chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    _digits = "0123456789"
    _allocated_names = []

    def __init__(self):
        self.name = __class__._make_name()

    def reset(self):
        self.name = __class__._make_name()

    @classmethod
    def _make_name(cls):
        while True:
            char_part = [random.choice(cls._chars) for _ in range(2)]
            digit_part = [random.choice(cls._digits) for _ in range(3)]
            name = "".join(char_part + digit_part)
            if name not in cls._allocated_names:
                cls._allocated_names.append(name)
                break
        return name
