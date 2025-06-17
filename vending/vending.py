def load_inventory():
    pass

def save_inventory(inventory):
    pass

def update_inventory(inventory):
    pass

def process_order(inventory):
    pass

def print_inventory(inventory):
    pass

def main():
    inventory = load_inventory()
    while True:
        print("\n1. Update Inventory 2. Process Order 3. Show Inventory 4. Save & Exit")
        choice = input("Choose: ")
        if choice == '1':
            update_inventory(inventory)
        elif choice == '2':
            process_order(inventory)
        elif choice == '3':
            print_inventory(inventory)
        elif choice == '4':
            save_inventory(inventory)
            break

if __name__ == "__main__":
    main()
