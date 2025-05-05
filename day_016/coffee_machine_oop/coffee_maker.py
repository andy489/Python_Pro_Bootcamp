class CoffeeMaker:
    """Models the machine that makes the coffee"""

    def __init__(self):
        self.resources = {
            "water": (300, "ml"),
            "milk": (200, "ml"),
            "coffee": (100, "g"),
        }

    def report(self):
        """Prints a report of all resources."""
        keys = self.resources.keys()
        for key in keys:
            print(f"{key.capitalize()}: {self.resources[key][0]}{self.resources[key][1]}")

    def is_resource_sufficient(self, baverage):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in baverage.ingredients.keys():
            if item not in self.resources or baverage.ingredients[item] > self.resources[item][0]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources. Assumes that is_resource_sufficient returned True"""
        for item in order.ingredients:
            self.resources[item] = self.resources[item][0] - order.ingredients[item], self.resources[item][1]
        print(f"Here is your {order.name} ☕️. Enjoy!")
