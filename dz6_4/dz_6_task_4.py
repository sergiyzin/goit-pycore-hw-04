def parse_input(user_input):
    """Розбираємо рядок на команду та аргументи."""
    parts = user_input.split()
    if not parts:
        return "", []
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args


def add_contact(args, contacts):
    """add name phone -> додаємо новий контакт."""
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    """change name phone -> змінюємо номер, якщо контакт є."""
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."


def show_phone(args, contacts):
    """phone name -> показуємо номер контакту."""
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."


def show_all(contacts):
    """all -> показуємо всі контакти."""
    if not contacts:
        return "No contacts."
    lines = []
    for name, phone in contacts.items():
        lines.append(f"{name}: {phone}")
    return "\n".join(lines)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            # очікуємо: add name phone
            if len(args) != 2:
                print("Usage: add username phone")
            else:
                print(add_contact(args, contacts))

        elif command == "change":
            # очікуємо: change name phone
            if len(args) != 2:
                print("Usage: change username phone")
            else:
                print(change_contact(args, contacts))

        elif command == "phone":
            # очікуємо: phone name користувача
            if len(args) != 1:
                print("Usage: phone username")
            else:
                print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
