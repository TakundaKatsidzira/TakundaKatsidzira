def print_cwd():
    pass

def change_dir():
    pass

def list_dir():
    pass

def create_file():
    pass

def delete_file():
    pass

def write_file():
    pass

def read_file():
    pass

def create_folder():
    pass

def delete_folder():
    pass

def main():
    while True:
        print("\n1. CWD 2. Change Dir 3. List 4. Create File 5. Delete File 6. Write 7. Read 8. New Folder 9. Del Folder 10. Exit")
        choice = input("Choose: ")
        if choice == '1':
            print_cwd()
        elif choice == '2':
            change_dir()
        elif choice == '3':
            list_dir()
        elif choice == '4':
            create_file()
        elif choice == '5':
            delete_file()
        elif choice == '6':
            write_file()
        elif choice == '7':
            read_file()
        elif choice == '8':
            create_folder()
        elif choice == '9':
            delete_folder()
        elif choice == '10':
            break

if __name__ == "__main__":
    main()
