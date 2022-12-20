from random import randint
from errors import *
from account import Account
from user import User


class Bank:
    def __init__(self):
        self.users = []

    def find_user(self, egn: str):
        for u in range(len(self.users)):
            if self.users[u].egn == egn:
                return self.users[u]

    def list_all_accounts_for_user(self, egn):
        user = self.find_user(egn)
        # if not user:
        #     raise UserNotFound()
        # else:
        print("Accounts:")
        for i in range(len(user.accounts)):
            print(user.accounts[i])

    def add_user(self, names, egn):
        found_user = self.find_user(egn)

        if type(found_user) == User:
            raise UserAlreadyExists()

        user = User(names, egn)
        self.users.append(user)

    def add_account(self, egn, currency, type):
        # user exists?
        found_user = self.find_user(egn)

        if found_user is None:
            raise UserNotFound()

        # generate iban
        iban = "BG9812"
        for i in range(0, 10):
            iban += str(randint(0, 9))

        # create account object
        account = Account(iban, currency, type)

        # call the user's add_account() method
        found_user.add_account(account)

    def deposit(self, amount, egn):
        if not egn:
            raise InvalidUserData

        self.balance += amount

    def withdrawal(self, amount, egn):
        if not egn:
            raise InvalidUserData

        if self.balance >= amount:
            self.balance -= amount
        else:
            raise InsufficientBalance
