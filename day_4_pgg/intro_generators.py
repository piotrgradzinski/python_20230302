def my_generator():
    print('a')
    yield 1
    print('b')
    yield 2
    print('c')
    yield 3


g = my_generator()
print(type(g), g)
print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
