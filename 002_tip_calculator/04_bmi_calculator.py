from math import floor

height = 1.75
weight = 91

# Calculate the bmi using weight and height.
bmi = weight / (height ** 2)

print(bmi)
print(int(bmi))
print(floor(bmi))
print(round(bmi))
print(round(bmi, 2))
