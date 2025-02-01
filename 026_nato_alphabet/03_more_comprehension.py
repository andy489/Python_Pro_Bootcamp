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