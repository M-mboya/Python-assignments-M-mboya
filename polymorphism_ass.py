# Base Fruit class
class Fruit:
    def __init__(self, name, color, taste):
        self.name = name
        self.color = color
        self.taste = taste

    def describe(self):
        print(f"{self.name} is {self.color} and tastes {self.taste}. 😋")

    def eat(self):
        print(f"You eat the {self.name}. Yum! 🍽️")


# Subclasses (Inheritance + Polymorphism)
class Banana(Fruit):
    def eat(self):
        print("Peel the banana before eating 🍌")

class Mango(Fruit):
    def eat(self):
        print("Slice the mango and enjoy the juicy flesh 🥭")

class Grape(Fruit):
    def eat(self):
        print("Pop a grape into your mouth 🍇")

class Orange(Fruit):
    def eat(self):
        print("Peel the orange before eating. Full of Vitamin C! 🍊")


# Demonstration of Polymorphism
fruits = [
    Banana("Banana", "Yellow", "Sweet"),
    Mango("Mango", "Golden", "Sweet & Tangy"),
    Grape("Grape", "Purple", "Juicy"),
    Orange("Orange", "Orange", "Tangy")
]

for f in fruits:
    f.describe()
    f.eat()
    print()
