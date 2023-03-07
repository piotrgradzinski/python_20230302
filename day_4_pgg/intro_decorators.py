def fun_zew():
    def fun_wew1():
        print('fun_wew1')

    def fun_wew2():
        print('fun_wew2')

    fun_wew1()
    fun_wew2()

fun_zew()

# fun_wew1()  # KO
print('-' * 30)

def hello_world():
    return 'Hello world'

def fun_zew(dane):
    def fun_wew1():
        print('fun_wew1', dane())

    def fun_wew2():
        print('fun_wew2', dane())

    fun_wew1()
    fun_wew2()

fun_zew(hello_world)

print('-' * 30)

def say_hi(name):
    return f'Hi {name}!'

def fun_zew(dane, param):
    def fun_wew1():
        print('fun_wew1', dane(param))

    def fun_wew2():
        print('fun_wew2', dane(param))

    fun_wew1()
    fun_wew2()

fun_zew(say_hi, 'Piotr')

print('-' * 30)

def say_hi(name):
    return f'Hi {name}!'

def say_official(name):
    return f'Good morning {name}!'

def greeter(greeter_func, name):
    return greeter_func(name)

print(greeter(say_hi, 'Piotr'))
print(greeter(say_official, 'Piotr'))

print('-' * 30)

# closure / domknięcie
def fun_zew(ktora, param):
    def fun_wew1(liczba):
        print('fun_wew1', param, liczba)

    def fun_wew2(liczba):
        print('fun_wew2', param, liczba)

    if ktora == 1:
        return fun_wew1
    else:
        return fun_wew2

print(fun_zew(1, 'Piotr'))
fun_zew(1, 'Piotr')(350)

fun1_z_piotr = fun_zew(1, 'Piotr')
fun1_z_piotr(123)

print('-' * 30)

def my_fun(*args, **kwargs):
    print(*args, **kwargs)


my_fun(1, 2, 3, sep='<->')
print(1, 2, 3, sep='<->')

print('-' * 30)

# A teraz już dekorator na poważnie

def moj_dekorator(funkcja_do_udekorowania):
    # zwyczajowo wrapper lub inner
    def wrapper(*args, **kwargs):
        print('Przed wywolaniem funkcji')
        wynik = funkcja_do_udekorowania(*args, **kwargs)
        print('Po wywolaniu funkcji')
        return wynik

    return wrapper

def hello_world():
    print('Hello world!')

udekorowane_hello_world = moj_dekorator(hello_world)
udekorowane_hello_world()

print('-' * 30)

udekorowane_sum = moj_dekorator(sum)
suma = udekorowane_sum([1, 2, 3])
print(suma)

# @ - tzw. pie-syntax
# https://www.python.org/dev/peps/pep-0318/#background
@moj_dekorator
def dodawacz(a, b):
    return a + b

wynik = dodawacz(3, 4)
print(wynik)



