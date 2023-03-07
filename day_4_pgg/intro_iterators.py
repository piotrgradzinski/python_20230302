for liczba in [1, 2, 3]:
    print(liczba)

print('-' * 30)

my_list = [1, 2, 3]
list_iterator = iter(my_list)
print(list_iterator)
print(iter(list_iterator))

print(next(list_iterator))  # 1
print(next(list_iterator))  # 2
print(next(list_iterator))  # 3
# print(next(list_iterator))  # StopIteration

print('-' * 30)

from collections.abc import Iterable, Iterator
class Counter(Iterable):
    def __init__(self, how_many, start):
        self.how_many = how_many
        self.start = start

    def count(self, number):
        return self.start + number

    def __iter__(self):
        print('Counter - running __iter__')
        return CounterIterator(self)

class CounterIterator(Iterator):
    def __init__(self, counter: Counter):
        self.counter = counter
        self.computed = 0

    def __next__(self):
        print('CounterIterator - running __next__')
        if self.computed >= self.counter.how_many:
            raise StopIteration()

        val = self.counter.count(self.computed)
        self.computed += 1
        return val


    def __iter__(self):
        print('CounterIterator - running __iter__')
        return self


counter = Counter(5, -2)

counter_iterator = iter(counter)  # counter.__iter__()
print(counter_iterator)
print(next(counter_iterator))
print(next(counter_iterator))
print(next(counter_iterator))
print(next(counter_iterator))
print(next(counter_iterator))
print(next(counter_iterator))



