phonebook = {}
def add_contact():
    name = input("enter name:").strip()
    number = input("Enter phone number:").strip()
    if name in phonebook:
        print("contact alredy exists")
    else:
        phonebook[name] = number
        print(f"contact'{name}'added")
def search_contact():
    name = input("enter name:").strip()
    if name in phonebook:
        print(f"{name}'{name}'added")
    else:
        print("contact not found")
def delete_contact():
    name = input("enter name to delete:").strip()
    if name in phonebook:
        print(f"contact '{name}' deleted")
    else:
        print("contact not found")
def display_contact():
    if not phonebook:
        print("phonebook is empty")
    else:
        print("contacts:")
        for name, number in phonebook.items():
            print(f"{name}'{number}'")