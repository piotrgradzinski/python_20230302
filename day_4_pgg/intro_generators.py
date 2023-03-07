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


print([x for x in my_generator()])
print(list(my_generator()))
print(tuple(my_generator()))
print(set(my_generator()))
print(list(map(lambda x: x * 10, my_generator())))