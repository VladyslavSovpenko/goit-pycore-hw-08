class ContactNameAlreadyExist(Exception):
    def __init__(self, message="Контакт з таким ім'ям вже наявний"):
        self.message = message
        super().__init__(self.message)

class InvalidPhoneNumberLength(Exception):
    def __init__(self, message="Невірна довжина номера"):
        self.message = message
        super().__init__(self.message)
