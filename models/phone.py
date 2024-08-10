import re

from exceptions.exceptions import InvalidPhoneNumberLength
from models.field import Field


class Phone(Field):
    def __init__(self, phone):
        if not re.fullmatch(r'\d{10}', phone):
            raise InvalidPhoneNumberLength
        else:
            super().__init__(phone)

    def __repr__(self):
        return f"Phone: {self.value}"
