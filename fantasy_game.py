"""
Fantasy Inventory Game
Manage your player inventory: collect loot, add/drop items, and view your magical stash!
"""

def display_inventory(inventory):
    print("\n=== Your Inventory ===")
    total_items = 0
    for item, qty in inventory.items():
        print(f"{qty} x {item}")
        total_items += qty
    print(f"Total items: {total_items}\n")

def add_to_inventory(inventory, item, qty=1):
    inventory[item] = inventory.get(item, 0) + qty
    print(f"Added {qty} x {item} to your inventory.")

def drop_from_inventory(inventory, item, qty=1):
    if item in inventory:
        if inventory[item] > qty:
            inventory[item] -= qty
            print(f"Dropped {qty} x {item}.")
        elif inventory[item] == qty:
            del inventory[item]
            print(f"Dropped all of your {item}.")
        else:
            print(f"You don't have that many {item}s to drop.")
    else:
        print(f"You don't have any {item}.")

def collect_loot(inventory, loot):
    print("\nYou found a stash of loot!")
    for item in loot:
        add_to_inventory(inventory, item)
    print("Loot collected!")

def main():

    # Starting inventory
    player_inventory = {
        'gold coin': 20,
        'sword': 1,
        'healing potion': 3
    }

    # Sample loot
    stash = ['gold coin', 'dagger', 'gold coin', 'healing potion', 'ruby']

    # Game
    print("\n--- Fantasy Inventory Manager ---")
    choices = ["2", "4", "3", "1", "5"]
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Drop Item")
    print("4. Collect Loot")
    print("5. Quit")

    for choice in choices:
        if choice == '1':
            display_inventory(player_inventory)
        elif choice == '2':
            add_to_inventory(player_inventory, "sword", 3)
        elif choice == '3':
            drop_from_inventory(player_inventory, "healing potion", 2)
        elif choice == '4':
            collect_loot(player_inventory, stash)
        elif choice == '5':
            print("Farewell, brave adventurer!")
            break
        else:
            print("Invalid choice. Please pick between 1 and 5.")

if __name__ == "__main__":
    main()