# Python is a Strongly Dynamically Typed Programming Language:
# https://stackoverflow.com/questions/11328920/is-python-strongly-typed
a = 3
print(type(a))
print(pow(a, 3))

a = "dynamic typing"
print(type(a))
# print(pow(a,3)) # boom

# Type Hints and Arrows
age: int
name: str
height: float
is_human: bool

def police_check(input_age: int) -> bool:
    if input_age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check(12):
    print("You may pass")
else:
    print("Pay a fine.")
