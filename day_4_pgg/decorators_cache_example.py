from functools import cache


@cache
def fibonacci(num):
    if num < 2:
        return num

    return fibonacci(num - 1) + fibonacci(num - 2)


"""
bez @cache: 2 692 537
z @cache: 31...
"""
print(fibonacci(30))
