# functions intro

"""
To jest docstring
"""

# type hinting
my_number: int = 10

wartosc = 123.456
print(f"{wartosc:.2}")
print("a=%f, b=%f" % (10, 20))
print("a={a}, b={b}".format(a=10, b=20))
print("a={}, b={}".format(10, 20))

print('-' * 10)

wartosc = 1230.456
print(f">{wartosc:10.2f}<")
print(f">{wartosc:^10.2f}<")
print(f">{wartosc:_^10_.2f}<")
print(f">{wartosc:_^10,.2f}<")

my_number = 10_674_231
print(my_number)

"""
ta zmienna wcześniej została opisana type hint int i dlatego PyCharm podpowiada, żeby przypisujemy niepoprawny typ
"""
my_number = 10_674_231.123
print(my_number)


def greeting(first_name, last_name, age):
    """Prepare special form of greeting.

    Some more information on the topic...

    :param first_name: Users first name
    :param last_name: Users last name
    :param age: Users age
    :return: Formatted string
    """
    return f"{first_name} {last_name} ({age:.2f})!"


print(greeting('Piotr', 'GG', 18))
