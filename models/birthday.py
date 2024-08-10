from datetime import datetime

from models.field import Field


class Birthday(Field):
    def __init__(self, value):
        try:
            birthday = datetime.strptime(value, '%d.%m.%Y')
            if datetime.now() > birthday:
                super().__init__(birthday)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY, or date in future.")
