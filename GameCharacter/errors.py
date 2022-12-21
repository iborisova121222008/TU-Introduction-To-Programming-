class InvalidCommand(Exception):
    def __init__(self, message="Enter a number between 1 and 5", *args: object) -> None:
        super().__init__(message, *args)


class CharacterExists(Exception):
    def __init__(self, message="Please register new character", *args: object) -> None:
        super().__init__(message, *args)


class CharacterDoesNotExists(Exception):
    def __init__(self, message="Character cannot be deleted, bc doesnot exsist", *args: object) -> None:
        super().__init__(message, *args)


class InvalidCharacterClass(Exception):
    def __init__(self, message="Choose between Warrior, Mage, Priest, Rogue", *args: object) -> None:
        super().__init__(message, *args)


class InvalidUserData(Exception):
    def __init__(self, message="Please enter valid data", *args: object) -> None:
        super().__init__(message, *args)
