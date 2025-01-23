class Car:
    def __init__(self, seats, horsepower):
        self.seats = seats
        self.horsepower = horsepower
        self.sold = False
        print("new car being created...")

    def enter_race_mode(self):
        self.seats = 2

    def sell(self):
        self.sold = True


car_1 = Car(2, 412)
car_2 = Car(5, 177)

print(f"Car 2 seats number: {car_2.seats}")
print(f"Car 2 available: {car_2.sold}")

car_2.enter_race_mode()
car_2.sell()

print(f"Car 2 seats number: {car_2.seats}")
print(f"Car 2 available: {car_2.sold}")
