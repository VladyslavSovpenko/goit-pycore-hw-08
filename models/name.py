from models.field import Field


class Name(Field):
    def __init__(self, value):
        if isinstance(value, str):
            super().__init__(value)
        else:
            raise ValueError("Value must be of type str")

    def __str__(self):
        return self.value
