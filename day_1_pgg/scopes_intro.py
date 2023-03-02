from pprint import pprint

a = 1
pprint(locals())
def outer():
    x = 10
    a = 1000
    pprint(locals())
    print(a, x)

    def inner():
        pprint(locals())
        print(a)

    inner()

outer()
print(a)
# print(x)  # KO: NameError,  x jest zdefiniowany w zasięgu lokalnym funkcji outer
