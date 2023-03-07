import datetime

d = datetime.datetime.now()
print(datetime.datetime.now())

d = datetime.datetime(year=2023, month=3, day=7, hour=12, minute=1, second=0)
print(d.year)
print(d.month)
print(d.day)
print(d.weekday())  # pon - 0

print(d.strftime('%d-%m-%Y'))
print(d.isoformat())

d = datetime.datetime.strptime('15-07-2023 10:11:12', '%d-%m-%Y %H:%M:%S')
print(type(d), d)
print(d.strftime('%d.%m.%Y'), type(d.strftime('%d.%m.%Y')))


print('-' * 30)


# pip install python-dateutil
from dateutil.relativedelta import relativedelta

epoch = datetime.datetime(year=1960, month=1, day=1)
# result = epoch + relativedelta(days=22969)
result = epoch + relativedelta(weeks=3164)
print(result)

teraz = datetime.datetime.now()
kiedys = datetime.datetime(year=2015, month=7, day=18, hour=12, minute=1, second=0)

wynik = teraz - kiedys
print(wynik)
print(wynik.days)
print(wynik.seconds)

wynik = relativedelta(teraz, kiedys)
print(wynik)

print('-' * 30)

# 1 dzień aktualnego miesiąca
d = teraz + relativedelta(day=1)
print(d.isoformat())

# najbliższy poniedziałek
d = teraz + relativedelta(weekday=0)
print(d.isoformat())

# ostatni dzień aktualnego miesiąca
d = teraz + relativedelta(day=31)
print(d.isoformat())

# ostatni dzień lutego
luty = datetime.datetime(year=2023, month=2, day=18)
d = luty + relativedelta(day=31)
print(d.isoformat())

# ostatni dzień kwietnia
luty = datetime.datetime(year=2023, month=4, day=18)
d = luty + relativedelta(day=31)
print(d.isoformat())

# ostatni dzień poprzedniego miesiąca
d = teraz + relativedelta(months=-1, day=31)
print(d.isoformat())

import dateutil.parser
d = dateutil.parser.parse('12.09.2023')
print(d.isoformat())