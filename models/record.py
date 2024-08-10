from models.name import Name
from models.phone import Phone
from models.birthday import Birthday


class Record:
    def __init__(self, name):
        self._name = None
        self._name = name
        self.phones = []
        self.birthday = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        self._name = Name(value)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                break

    def find_phone(self, phone):
        return any(p.value == phone for p in self.phones)

    def add_birth(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        phone_list = '; '.join(p.value for p in self.phones)
        return f"Contact name: {self.name}, phones: {phone_list}"
