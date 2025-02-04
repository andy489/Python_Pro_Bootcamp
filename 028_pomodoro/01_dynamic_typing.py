# https://stackoverflow.com/questions/11328920/is-python-strongly-typed

# Python is a strongly dynamically typed programming language
a = 3
print(type(a))
print(pow(a, 3))

a = "dynamic typing"
print(type(a))
# print(pow(a,3)) # boom

# Type hints and arrows
age: int
name: str
height: float
is_human: bool


def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check(12):
    print("You may pass")
else:
    print("Pay a fine.")
