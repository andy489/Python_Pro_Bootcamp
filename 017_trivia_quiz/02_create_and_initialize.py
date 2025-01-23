class Car:
    def __init__(self, seats, horsepower):
        self.seats = seats
        self.horsepower = horsepower
        self.sold = False
        print("new car being created...")


car_1 = Car(2, 412)
car_2 = Car(5, 177)
