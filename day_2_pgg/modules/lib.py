# day_2_pgg/modules/lib.py

def square(number):
    return number ** 2


first_name = 'Piotr'
numbers = [1, 2, 3]


class DatabaseWrapper:
    def __init__(self):
        self.con = 'connection'

    def get_data(self):
        return [1, 2, 3]


# __main__
# day_2_pgg.modules.lib
if __name__ == '__main__':
    print(__name__)
    print('Ala ma kota')

