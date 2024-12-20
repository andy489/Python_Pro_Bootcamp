numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# new_list = [new_item for item in list]

powers_of_2_list = [2 ** n for n in numbers]
print(f"List of powers of 2: {powers_of_2_list}")

memo_fact = {0: 0, 1: 1}


def fact(n):
    if n in memo_fact:
        return memo_fact[n]
    else:
        x = n * fact(n - 1)
        memo_fact[n] = x
        return x


factorials_list = [fact(n) for n in range(10)]
print(f"List of factorials: {factorials_list}")

memo_fib = {0: 0, 1: 1}


def fib(n):
    if n in {0, 1}:
        return n
    memo_fib[n] = fib(n - 1) + fib(n - 2)
    return memo_fib[n]


fibonacci_nums = [fib(n) for n in range(20)]
print(f"List of Fibonacci numbers: {fibonacci_nums}")

range_list_doubled = [num * 2 for num in range(1, 5)]
print(f"Range list doubled: {range_list_doubled}")

range_list_squared = [num * num for num in range(1, 5)]
print(f"Range list squared: {range_list_squared}")

# new_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

new_list_of_short_names = [name for name in names if len(name) < 5]
print(f"New list of short names: {new_list_of_short_names}")

new_list_of_long_names = [name.upper() for name in names if len(name) > 4]
print(f"New list of long names: {new_list_of_long_names}")

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num_str) for num_str in list_of_strings]
result = [num for num in numbers if num & 1 == 0]
print(f"Filter even numbers: {result}")