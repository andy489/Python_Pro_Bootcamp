programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary["Bug"])
print(programming_dictionary)

empty_dictionary = {}
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in dictionary
programming_dictionary["Bug"] = "Not a moth in your computer."
print(programming_dictionary)

# Loop through a dictionary 1
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Loop through a dictionary 2
for value in programming_dictionary.values():
        print(value)

# Loop through a dictionary 3
for key, value in programming_dictionary.items():
    print(key)
    print(value)
