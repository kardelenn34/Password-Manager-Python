from database import *

while True:

    print("\n========== PASSWORD MANAGER ==========")
    print("1 - Add Password")
    print("2 - View Passwords")
    print("3 - Search Password")
    print("4 - Delete Password")
    print("5 - Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_password()

    elif choice == "2":
        view_passwords()

    elif choice == "3":
        search_password()

    elif choice == "4":
        delete_password()

    elif choice == "5":
        close_connection()
        print("\nProgram closed.")
        break

    else:
        print("\nInvalid option.\n")
