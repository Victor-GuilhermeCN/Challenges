# Challenge number 1
# Creating the class and  3 methods.

class Car:

    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

    def turn_on(self):
        print('Car starting!')

    def turn_of(self):
        print('Car turning off!')

    def show_car(self):
        print(f'Model: {self.model}\n'
              f'Color: {self.color}\n'
              f'Year: {self.year}')


car1 = Car('Masserati', 'Red', 2011)

car1.show_car()