numbers = [1, 2, 3]

# Ordinary way

new_list = []

for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
# print(new_list)

# Python way (list comprehension)
# Synthx: new_list = [new_item for item in list]
new_list = [n + 1 for n in numbers]
# print(new_list)

name = "Andrey"
letters_list = [letter for letter in name]
# print(letters_list)
range_list = [num * 2 for num in range(1, 5)]
# print(range_list)

# Conditional list comprehension
# new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
print(names)
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(s) for s in list_of_strings]
result = [num for num in numbers if num & 1 == 0]
print(result)

with open("file1.txt") as f:
    nums1 = [int(num.strip()) for num in f.readlines()]

with open("file2.txt") as f:
    nums2 = [int(num.strip()) for num in f.readlines()]

common_numbers = [num for num in nums1 if num in nums1 and num in nums2]
print(f"result: {common_numbers}")
