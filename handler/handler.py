from decorator import command_decorator, operations_decorator
from exceptions import ContactNameAlreadyExist
from file_handler import save_data, load_data
from models.address_book import AddressBook
from models.record import Record

contacts = load_data()


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@command_decorator
def handle_command(command, args):
    if command in operations:
        apply_operation(operations[command], args)
    else:
        print("Invalid command.")


def apply_operation(command, args):
    command(args)


def greeting(_=None):
    print("How can I help you?")


@operations_decorator
def add_contact(args):
    name, phone, *_ = args
    name = name.strip().capitalize()
    record = Record(name)
    record.add_phone(phone)
    if record.name not in contacts:
        contacts[record.name] = record
        print(f"Contact with name {record.name} added.")
    else:
        raise ContactNameAlreadyExist


@operations_decorator
def change_phone(args):
    name, old_phone, new_phone, *_ = args
    if name in contacts:
        record = contacts[name]
        record.edit_phone(old_phone, new_phone)
        print(f"Contact with name {record.name} updated.")
    else:
        raise KeyError


@operations_decorator
def get_by_name(args):
    name, *_ = args
    if name in contacts:
        print(f"{contacts[name]}")
    else:
        raise KeyError


@operations_decorator
def show_birthday(args):
    name = args[0].strip().capitalize()
    if name not in contacts:
        raise KeyError(f"Contact {name} not found.")
    record = contacts[name]
    if record.birthday:
        print(f"{name}'s birthday is on {record.birthday.value.strftime('%d.%m.%Y')}")
    else:
        print(f"{name} does not have a birthday set.")


@operations_decorator
def add_birthday(args):
    name, birthday = args
    name = name.strip().capitalize()
    if name not in contacts:
        raise KeyError(f"Contact {name} not found.")
    record = contacts[name]
    if not record.birthday:
        record.add_birth(birthday)
    else:
        raise ValueError
    print(f"Birthday added to {name}.")


@operations_decorator
def handle_birthdays(_=None):
    upcoming_birthdays = contacts.get_upcoming_birthdays()  # Call the method with parentheses
    for birthday in upcoming_birthdays:
        print(f"{birthday['name']}'s birthday is on {birthday['congratulation_date']}")


@operations_decorator
def get_all_contacts(_=None):
    if len(contacts) > 0:
        for name, record in contacts.items():
            birthday = record.birthday.value.strftime('%d.%m.%Y') if record.birthday else 'No birthday set'
            print(f"Name: {name}, Phones: {record.phones}, Birthday: {birthday}")


def close(_=None):
    save_data(contacts)
    print("Good bye!")
    exit()


def print_commands(_=None):
    print(f"Commands:{operations.keys()}")


operations = {
    "hello": greeting,
    "add": add_contact,
    "help": print_commands,
    "change": change_phone,
    "phone": get_by_name,
    "all": get_all_contacts,
    "add_birthday": add_birthday,
    "show_birthday": show_birthday,
    "birthdays": handle_birthdays,
    "close": close,
    "exit": close
}
