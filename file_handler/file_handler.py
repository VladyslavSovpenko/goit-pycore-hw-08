import pickle

from models.address_book import AddressBook


def save_data(contacts, file="addressbook.pkl"):
    with open(file, "wb") as fh:
        pickle.dump(contacts, fh)


def load_data(file="addressbook.pkl"):
    try:
        with open(file, "rb") as fh:
            return pickle.load(fh)
    except FileNotFoundError as e:
        print("File not found. Create new one", e)
        return AddressBook()
