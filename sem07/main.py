from bank import Bank
from errors import *


class Menu:
    def print_menu(self):
        print("1. Register a new user")
        print("2. Create an account for an existing user")
        print("3. List all users")
        print("4. List all accounts for an existing user")
        print("5. Deposit money to a user account")
        print("6. Withdraw money from a user account")
        print("7. Exit")

    def run(self):
        bank = Bank()

        # infinite menu loop
        while True:
            self.print_menu()
            choice = input("Choose an item from the menu: \n> ")

            try:
                if choice == "1":
                    print("1. Register a new user")
                    names = input("Enter the user's names (alpha-only): ")
                    fname, lname = names.split(" ")
                    if len(names) < 4 or not fname.isalpha() or not lname.isalpha():
                        raise InvalidUserData("Invalid names")

                    egn = input("Enter the user's EGN number (len 10, digits-only): ")
                    if len(egn) != 10 or not egn.isdigit():
                        raise InvalidUserData("Invalid EGN number")

                    bank.add_user(names, egn)
                elif choice == "2":
                    # second command
                    print("2. Create an account for an existing user\n")
                    egn = (input("Enter your EGN: "))
                    if len(egn) != 10:
                        raise InvalidUserData()

                    currency = input("Enter the currency: ")
                    type = input("Enter the type of the account -> (Credit, Savings, Payment): ")
                    bank.add_account(egn, currency, type)

                elif choice == "3":
                    print("3. List all users\n")
                    for u in bank.users:
                        print(u.get_print())
                elif choice == "4":
                    print("4. List all accounts for an existing user\n")
                    egn = input("Enter your EGN: ")
                    bank.list_all_accounts_for_user(egn)

                elif choice == "5":
                    print("5. Deposit money to a user account\n")
                    egn = input("Enter your EGN: ")
                    amount = input("Enter how much you want to deposit: ")
                    bank.deposit(amount, egn)
                elif choice == "6":
                    print("6. Withdraw money from a user account\n")
                    egn = input("Enter your EGN: ")
                    amount = input("Enter how much you want to withdrawal: ")
                    bank.withdrawal(amount, egn)

                elif choice == "7":
                    print("Goodbye\n")
                    break
                else:
                    raise InvalidMenuChoice()
            except Exception as ex:
                print(f"Error: There was an error while executing the command:\n{str(ex)}")

            print()


if __name__ == '__main__':
    menu = Menu()
    menu.run()
