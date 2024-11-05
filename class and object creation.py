class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}")

# Create an instance of Car
my_car = Car("Toyota", "Corolla", 2020)
my_car.display_info()
