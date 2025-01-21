# https://haveibeenpwned.com/

fruits = ["Apple", "Peach", "Pear"]

for i in range(0, len(fruits)):
    print(i, fruits[i])

for fruit in fruits:
    print(fruit)

for i, fruit in enumerate(fruits):
    print(i, fruit)
