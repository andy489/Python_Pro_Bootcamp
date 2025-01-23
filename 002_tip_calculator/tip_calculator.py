print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

result = (bill * (1 + tip / 100.0)) / people

print(f"Each person should pay: ${round(result, 2)}")
