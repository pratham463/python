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
def main():
    while True:
        print("1. add contact")
        print("2. search contact")
        print("3. delete contact")
        print("4. display all contact")
        print("5. exit")
        choice = input("chose an option (1-5):").strip()
        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            display_contact()
        elif choice == '5':
            print("exiting phonebook bye")
        else:
            print("Invalid option pls try again")
main()