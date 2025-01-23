class User:
    pass

user_1 = User()
print("id" in dir(user_1))

user_1.id = "001"

print(user_1)
print(user_1.id)
print("id" in dir(user_1))

