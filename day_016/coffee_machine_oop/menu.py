import json


class MenuItem:
    """Models each Menu Item."""

    def __init__(self, name: str, ingredients: dict, cost: float):
        self.name = name
        self.ingredients = ingredients
        self.cost = cost

    def __str__(self):
        # Automatically gets all non-private attributes (excluding methods)
        obj_dict = {key: value for key, value in self.__dict__.items()
                    if not key.startswith('__') and not callable(value)}
        return json.dumps(obj_dict, indent=4)


class Menu:
    """Models the Menu with baverages."""

    def __init__(self):
        self.menu = [
            MenuItem("latte", {"water": 200, "milk": 150, "coffee": 24}, 2.5),
            MenuItem("espresso", {"water": 50, "coffee": 18}, 1.5),
            MenuItem("cappuccino", {"water": 250, "milk": 50, "coffee": 24}, 3.0),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options[:len(options) - 1]

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it existed, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
