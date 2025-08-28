# Parent class
class Fruit:
    def __init__(self, name, color, taste):
        self.name = name
        self.color = color
        self.taste = taste

    def describe(self):
        print(f"{self.name} is {self.color} and tastes {self.taste}. 😋")

    def eat(self):
        print(f"You eat the {self.name}. Yum! 🍽️")


# Child class (Inheritance + Polymorphism)
class Citrus(Fruit):
    def __init__(self, name, color, taste, vitamin_c_level):
        super().__init__(name, color, taste)
        self.vitamin_c_level = vitamin_c_level

    # Polymorphism: redefine eat()
    def eat(self):
        print(f"You peel the {self.name} before eating. Full of Vitamin C! 🍊")

    def health_benefit(self):
        print(f"{self.name} boosts immunity with Vitamin C level {self.vitamin_c_level} 💪")


# Usage
apple = Fruit("Apple", "Red", "Sweet")
orange = Citrus("Orange", "Orange", "Tangy", "High")

apple.describe()
apple.eat()

orange.describe()
orange.eat()
orange.health_benefit()
