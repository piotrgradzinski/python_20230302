import timeit

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

res = timeit.timeit(stmt='fibonacci(33)', setup='from __main__ import fibonacci', number=3)
print(res)
