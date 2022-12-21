from errors import *


class Character:
    def __init__(self, name, sex, class_in_game, weapon=None, items=[]):
        self.name = name
        self.sex = sex
        self.class_in_game = class_in_game
        self.weapon = weapon
        self.item = items


class Item:
    def __init__(self, name, durability):
        self.name = name
        self.durability = durability


class Weapon(Item):
    def __init__(self, name, durability, attack):
        super().__init__(name, durability)
        self.attack = attack


class Menu:

    def print_menu(self):
        print("1. Create a new character")
        print("2. Create weapon for an existing character")
        print("3. Create a item for an existing character")
        print("4. Print all characters")
        print("5. Delete an existing character")

    def __init__(self):
        self.characters = []

    def run(self):
        # infinite menu loop
        while True:
            # print the menu
            # ...

            # ask the user to choose a command

            # catch errors
            try:

                command = int(input("Choose an item from the menu: \n "))
                if command == 1:
                    self.command_create_character()
                elif command == 2:
                    self.create_weapon()
                elif command == 3:
                    self.create_item()
                elif command == 4:
                    self.print_characters()
                elif command == 5:
                    self.delete_character()
                elif command == 6:
                    break
                else:
                    raise InvalidCommand(f"{command} is not a valid command number")
            except Exception as ex:
                print(f"Error: {str(ex)}")

    print()

    def command_create_character(self):
        name = input("Enter character name: ")
        if len(name) < 4 or not name.isalpha():
            raise InvalidUserData("Invalid name")

        if name in self.characters:
            for character in self.characters:
                if character.name == name:
                    return character
            raise CharacterExists(f"Character {name} already exists")

        sex = input("Enter character gender: ")
        ch_class = input("Enter character class: ")
        if ch_class not in ["Warrior", "Mage", "Priest", "Rogue"]:
            raise InvalidCharacterClass(f"{ch_class} is not a valid character class")
        self.characters.append(Character(name, sex, ch_class))
        print(f"Character {name} created")

    def create_weapon(self):
        character_name = input("Enter character name: ")
        weapon_name = input("Enter weapon name: ")
        durability = input("Enter durability: ")
        attack = input("Enter weapon attack: ")
        attack = int(attack)
        if character_name in self.characters:
            character_name.weapon = (Weapon(weapon_name, durability, attack))
        print(f"Weapon {weapon_name} added to character {character_name}")

    def create_item(self):
        character_name = input("Enter character name: ")
        # character = self.get_character(character_name)
        item = input("Enter item name: ")
        durability = input("Enter durability: ")
        if character_name in self.characters:
            character_name.items.append(Item(item, durability))

        print(f"Item {item} added to character {character_name}")

    def print_characters(self):
        if self.characters:
            for character in self.characters:
                print(character)

    def delete_character(self):
        name = input("Enter character name: ")

        if self.characters.__contains__(name):  # item in list
            self.characters.remove(name)
        else:
            raise CharacterDoesNotExists()

    def get_character(self, name):
        for character in self.characters:
            if character.name == name:
                return character

        return None


if __name__ == '__main__':
    menu = Menu()
    menu.run()
