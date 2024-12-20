def add(n1, n2):
    return n1 + n2


def add_unlimited_args(*args):
    for n in args:
        print(n)


def sum_nums(*args):
    res = 0
    for n in args:
        res += n
    return res


print(sum_nums(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.mileage = kw.get("mileage")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.mileage)
