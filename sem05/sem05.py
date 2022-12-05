import random


class MissingParameterError(Exception):
    pass


class InvalidParameterError(Exception):
    def __init__(self, invl_param, *args):
        message = f"Invalid class parameter: {invl_param}"
        super().__init__(message, *args)


class InvalidAgeError(InvalidParameterError):
    def __init__(self):
        super().__init__("age")


class InvalidSoundError(InvalidParameterError):
    def __init__(self):
        super().__init__("sound")


class JungleAnimal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

        if type(name) != str:
            raise InvalidParameterError("name")
        elif type(age) != int:
            raise InvalidAgeError()
        elif type(sound) != str:
            raise InvalidSoundError()

    def make_sound(self):
        print(f"{self.name} says {self.sound}!")

    def print(self):
        pass

    def daily_task(self):
        pass


class Jaguar(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if self.age > 15:
            raise InvalidAgeError()
        elif not "rr" in self.sound:
            raise InvalidSoundError()

    def print(self):
        print(f"Jaguar({self.name}, {self.age}, {self.sound})")

    def daily_task(self, animals):
        for i in range(len(animals)):
            if type(animals[i]) == Lemur or type(animals[i]) == Human:
                animals.pop(i)
                print(f"{self.name} the Jaguar hunted down {animals[i].name} the {type(animals[i]).__name__}")
            break


class Lemur(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if self.age > 10:
            raise InvalidAgeError()
        elif not "e" in self.sound:
            raise InvalidSoundError()

    def print(self):
        print(f"Lemur({self.name}, {self.age}, {self.sound})")

    def daily_task(self, fruits):
        if fruits >= 10:
            fruits -= 10
            print(f"{self.name} the Lemur ate a full meal of 10 fruits")
            return fruits
        elif fruits < 10:
            print(f"{self.name} the Lemur could only find {fruits} fruits")
            return 0
        else:
            self.make_sound()
            self.make_sound()
            print(f"{self.name} the Lemur couldn't find anything to eat")
            return 0


class Human(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if age > 10:
            raise InvalidAgeError()
        elif not "e" in self.sound:
            raise InvalidSoundError()

    def print(self):
        print(f"Human({self.name}, {self.age}, {self.sound})")

    def daily_task(self, animals, buildings):
        for i in range(len(animals)):
            if animals[i] == self:
                if i != 0 and i != len(animals) - 1:
                    if type(animals[i - 1]) == Human and type(animals[i + 1]) == Human:
                        typeBuilding = input("Enter type of Building: ")
                        buildings.append(Building(typeBuilding))
                elif i == 0:
                    if type(animals[i + 1]) == Human:
                        typeBuilding = input("Enter type of Building: ")
                        buildings.append(Building(typeBuilding))
                elif i == len(animals) - 1:
                    if type(animals[i - 1]) == Human:
                        typeBuilding = input("Enter type of Building: ")
                        buildings.append(Building(typeBuilding))


class Building():
    def __init__(self, typeBuilding):
        self.typeBuilding = typeBuilding

    def print(self):
        print(self.typeBuilding)


fruits = 100
animals = []
buildings = []

names = [
    "Jacob",
    "David",
    "Bobby",
    "Steve",
    "Johanssen",
    "Mac",
    "Jason",
    "Edward",
    "Alex",
    "Maddie",
    "Susan",
    "Abigail",
    "Jessica",
    "Lizzy",
    "Monica",
    "Lorelei",
    "Sandra",
    "Michelle"
]

sounds = [
    "RAAWR",
    "ROAR",
    "Grrr",
    "Shriek",
    "Meow",
    "Eeek",
    "Aaaaa",
    "Speak",
    "I am a Human"
]

for i in range(102):
    rand_num = random.randint(0, 9)
    rand_name = random.randint(0, len(names) - 1)
    rand_sound = random.randint(0, len(sounds) - 1)
    rand_age = random.randint(7, 20)
    try:
        if 0 <= rand_num <= 3:
            animals.append(Lemur(names[rand_name], rand_age, sounds[rand_sound]))
        elif 4 <= rand_num <= 7:
            animals.append(Lemur(names[rand_name], rand_age, sounds[rand_sound]))
        elif 8 <= rand_num <= 9:
            animals.append(Lemur(names[rand_name], rand_age, sounds[rand_sound]))
    except InvalidAgeError:
        print(rand_num, names[rand_name], rand_age, sounds[rand_sound], InvalidAgeError())
    except InvalidSoundError:
        print(rand_num, names[rand_name], rand_age, sounds[rand_sound], InvalidSoundError())

print(f"The jungle now has {len(animals)} animals")

for animal in animals:
    if type(animal) == Lemur:
        fruits = animal.daily_task(fruits)
    if type(animal) == Jaguar:
        animal.daily_task(animals)
    if type(animal) == Human:
        animal.daily_task(animals, buildings)

print(f"The jungle now has {len(animals)} animals")
print(fruits)
print(animals)
print(buildings)


