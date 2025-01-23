print(type("Hello"))
print(type(123))
print(type(2.718281))
print(type(True))

print(int(123) + int(456))
print(type(int("123")))

n = 10
bin_n = bin(10)
print(bin_n)
print(int(bin_n, 2))

username = input("Enter your username:\n")
username_length = len(username)

print(type(username))
print(type(username_length))

print("Number of letters in your username: " + str(username_length))
