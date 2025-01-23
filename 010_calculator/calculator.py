from art import logo


def clear_screen():
    print("\n" * 20)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


# print(operations["*"](4,8))
def calculator():
    print(logo)
    should_accumulate = True
    num1 = float(input("Whats the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        result = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if choice != "n":
            num1 = result
        else:
            should_accumulate = False
            clear_screen()
            calculator()


calculator()
