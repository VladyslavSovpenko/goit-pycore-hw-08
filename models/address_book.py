from collections import UserDict
from datetime import datetime, timedelta

from models.record import Record


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data[name]

    def delete(self, name: str):
        del self.data[name]

    def adjust_for_weekend(self, date):
        if date.weekday() == 5:
            return date + timedelta(days=2)
        elif date.weekday() == 6:
            return date + timedelta(days=1)
        else:
            return date

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming_birthdays = []
        for record in self.data.values():
            if record.birthday:
                birthday = record.birthday.value.date()
                birthday_this_year = datetime(today.year, birthday.month, birthday.day).date()
                days_to_birthday = (birthday_this_year - today).days
                if 0 <= days_to_birthday <= 7:
                    birthday_this_year = self.adjust_for_weekend(birthday_this_year)
                    upcoming_birthdays.append({
                        "name": record.name,
                        "congratulation_date": birthday_this_year.strftime('%d.%m.%Y')
                    })
        return upcoming_birthdays

    def __str__(self):
        output = ["AddressBook:"]
        for name, record in self.data.items():
            output.append(str(record))
        return "\n".join(output)
