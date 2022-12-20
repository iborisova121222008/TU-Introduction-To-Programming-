class InvalidUserData(Exception):
    def __init__(self, message="Please enter valid data", *args: object) -> None:
        super().__init__(message, *args)


class UserNotFound(Exception):
    def __init__(self, message="Such a user doesn't exist", *args: object) -> None:
        super().__init__(message, *args)


class UserAlreadyExists(Exception):
    def __init__(self, message="User already exists", *args: object) -> None:
        super().__init__(message, *args)


class UserAlreadyOwnsAccount(Exception):
    def __init__(self, message="This user already has an account", *args: object) -> None:
        super().__init__(message, *args)


# Account
class AccountNotFound(Exception):
    def __init__(self, message="Account not found", *args: object) -> None:
        super().__init__(message, *args)


class UnsufficientBalance(Exception):
    def __init__(self, message="Unsufficient Balance", *args: object) -> None:
        super().__init__(message, *args)


class InvalidAccountData(Exception):
    def __init__(self, message="Please enter valid data", *args: object) -> None:
        super().__init__(message, *args)


class InvalidAccountType(Exception):
    def __init__(self, message="Invalid type", *args: object) -> None:
        super().__init__(message, *args)


# Bank


# Menu
class InvalidMenuChoice(Exception):
    def __init__(self, message="Enter a number between 1 and 7", *args: object) -> None:
        super().__init__(message, *args)
