"""
NEXT STEPS


ADD LIST CLIENTS
ADD SAVE AND LOAD
MULTIPLE CONTACT BOOKS
GET TO GET ALL DATA OR ONE VALUE
CASE INSENSITIVITY
ONLY TAKE KEY IN PHONE EMAIL
"""



# add client records
def add(contacts):
    name = input("Enter client name: ")
    phone = input("Enter client phone: ")
    email = input("Enter client email: ")

    contacts[name] = {
        "phone" : phone,
        "email" : email
    }
    return

# change client info
def update(contacts):
    name = input("Enter client name: ")
    key = input("Enter data type: ")
    value = input("Enter data: ")

    # client doesn't exist
    if name not in contacts:
        print("Client not found")
        return
    
    # field doesn't exist
    elif key not in contacts[name]:
        print("Invalid field name")
        return
    
    # index into dict of dict
    contacts[name][key] = value
    return

# print client info            
def get(contacts):
    name = input("Enter client name: ")
    key = input("Enter data type: ")

    # client doesn't exist 
    if name not in contacts:
        print("Client not found")
        return
    
    # field doesn't exist
    elif key not in contacts[name]:
        print("Invalid field name")
        return
    else:
        print(contacts[name][key]) 
        return
            
# remove client record
def delete(contacts):
    name = input("Enter client name: ")

    # client doesn't exist
    if name in contacts.keys():
        del contacts[name]
        print(f"Deleted {name}")
        return
    else:
        print("Client not found")
        return


def main():
    contacts = {}
    print("Contact Book Opened")
    print("Enter valid integer choice.")
    print("0. Quit, 1. Enter Client Record, 2. Update Client Info, 3. Retrieve Client Info, 4. Delete Client Record.")
    while True:

        # get integer choice
        try:
            choice = int(input(">> "))
        except ValueError:
            print("Enter Valid integer [0:4]")
            continue

        # map input to function 
        actions = {
            1 : add,
            2 : update,
            3 : get,
            4 : delete
        }
        if choice in actions:
            actions[choice](contacts)

        # quit    
        elif choice == 0:
            print("Contact Book Closed")
            break
        
        # invalid input
        else:
            print("Integer choice not in range")
    
    return

if __name__ == "__main__":
    main()
