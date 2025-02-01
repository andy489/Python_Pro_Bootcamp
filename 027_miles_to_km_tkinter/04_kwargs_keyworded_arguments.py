def calculate(n, **kwargs):
    # print(type(kwargs))

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
        if "make" in kw:
            self.make = kw["make"]
        if "model" in kw:
            self.model = kw["model"]

    def __str__(self):
        attributes = []
        if getattr(self, "make", None) is not None:
            attributes.append(f"\"make\":\"{self.make}\"")
        if getattr(self, "model", None) is not None:
            attributes.append(f"\"model\":\"{self.model}\"")

        toReturn = ""
        if len(attributes) == 0:
            return "{}"
        else:
            toReturn += "{"
            for attr in attributes[0:len(attributes) - 1]:
                toReturn += attr + ", "
            toReturn += attributes[len(attributes) - 1]
            toReturn += "}"

        return toReturn


my_car1 = Car(make="Nissan", model="GT-R")
my_car2 = Car(make="Toyota")
my_car3 = Car()
print(my_car1)
print(my_car2)
print(my_car3)
