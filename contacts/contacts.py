def load_contacts():
    pass

def save_contacts(contacts):
    pass

def add_contact(contacts):
    pass

def access_contact(contacts):
    pass

def change_contact(contacts):
    pass

def remove_contact(contacts):
    pass

def print_contacts(contacts):
    pass

def main():
    contacts = load_contacts()
    while True:
        print("\n1. Add 2. Access 3. Change 4. Remove 5. Print 6. Save & Exit")
        choice = input("Choose: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            access_contact(contacts)
        elif choice == '3':
            change_contact(contacts)
        elif choice == '4':
            remove_contact(contacts)
        elif choice == '5':
            print_contacts(contacts)
        elif choice == '6':
            save_contacts(contacts)
            break

if __name__ == "__main__":
    main()
