# Create a class Person that model the person object
# Class attibutes: Name, Age, Weight and Height
# Class methods: Aging, getting_fat, losing_weight, growing
from datetime import datetime


class Person:
    year = datetime.today().year

    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def aging(self, new_age):
        grow = new_age - self.age
        print(f'Grow up {grow} years.\n'
              f'Your age {self.age}')
        return grow

    def getting_fat(self, new_weight):
        if self.weight < new_weight:
            print(f'Fed up {new_weight - self.weight:.2f}KG')

    def loosing_weight(self, new_weight):
        if self.weight > new_weight:
            print(f'Lost {self.weight - new_weight:.2f}KG')

    def growing(self, new_age):
        grow = self.aging(new_age)
        if new_age <= 21:
            self.height += grow * 0.05
        elif new_age > 21:
            self.height += (21 - self.age) * 0.05
        if grow == 1:
            print(f'You grow up {grow} year.\n'
                  f'{self.height:.2f}M')
        else:
            print(f'You grow up {grow} years.\n'
                  f'{self.height:.2f}M')


p1 = Person('Joao', 19, 80.0, 1.70)
p1.growing(25)
