def greet():
    print("Hello Stranger.")
    print("How do you do Stranger?")
    print("Isn't the weather nice?")


greet()


def greet(name):
    print(f"Hello {name}.")
    print(f"How do you do {name}?")


greet("Andrey")


def greet(name, location):
    print(f"Hello {name}.")
    print(f"What is it like in {location}?")


greet("Jack Nicholson", "California")
greet(location="California", name="Jack Nicholson")
