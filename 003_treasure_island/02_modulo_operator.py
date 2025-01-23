n = int(input("What is the number you want to check? "))

if n % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

if n & 1:
    print("Number is odd")
else:
    print("Number is even")
