# Робота з класами та обʼєктами
# Task 1

class Animal:
    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(f'{self.name} буде видавати звук {self.sound}')


a = str(input('Name of animal: '))
dog = Animal(a, "Dog", 5, "Woof!")
dog.make_sound()

# Робота з обʼєктами
# Task 1


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        print(rectangle.width * rectangle.height)


rectangle = Rectangle(4, 6)
rectangle.calculate_area()
rectangle = Rectangle(2, 5)
rectangle.calculate_area()
