class Vehicle():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def start_engine(self):
        print(f'The engine of {first_car.make} is starting.')


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year)
        self.color = color

    def running(self):
        print('Our motorcycle is going now.')


class Bicycle(Vehicle):
    def __init__(self, make, model, year, number_of_wheels):
        super().__init__(make, model, year)
        self.number_of_wheels = number_of_wheels

    def start(self):
        print('We\'re riding a bike.')


first_car = Car('Honda', 'Accord', 2006, 'Gasoline')
first_motorcycle = Motorcycle('Suzuki', 'GTR', 1985, 'green')
first_bicycle = Bicycle('Ukraina', 'Standart', 1998, 2)

first_car.start_engine()
