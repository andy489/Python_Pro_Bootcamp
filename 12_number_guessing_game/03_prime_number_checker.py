def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


number = int(input("Enter a natural number: "))
print(f"{number} is {"not " if not is_prime(number) else ""}a prime.")
