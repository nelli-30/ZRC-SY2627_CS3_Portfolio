class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        pass

    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        print(f"{self.name} roars loudly!")

    def eat(self):
        print(f"{self.name} eats fresh meat.")


class Elephant(Animal):
    def make_sound(self):
        print(f"{self.name} trumpets!")

    def eat(self):
        print(f"{self.name} eats grass and fruits.")


class Monkey(Animal):
    def make_sound(self):
        print(f"{self.name} chatters!")

    def eat(self):
        print(f"{self.name} eats bananas.")


animals = [
    Lion("Simba"),
    Elephant("Dumbo"),
    Monkey("George")
]

for animal in animals:
    animal.make_sound()
    animal.eat()
    print("-----")