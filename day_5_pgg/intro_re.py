test_string = """<em>Ala ma kota</em>
Ala ma kota.
Kot ma 1a kompilator a
1
31-421
!@#$%^&*()
1235-12345123123
00-123
Ala
Ola
Ela
1a
2B
3c
8b
9a
6c
panewka
konewka"""

import re

# lista z tuplami (lub stringami jak nie ma grup)
matches = re.findall(r'^((\d{2})-(\d{3}))$', test_string, flags=re.MULTILINE)
print(matches)

print('-' * 30)

# iterator z obiektami Match
for match in re.finditer(r'^((\d{2})-(\d{3}))$', test_string, flags=re.MULTILINE):
    print(match.groups())
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))

print('-' * 30)

# search zwraca pierwsze dopasowanie
match = re.search(r'^((\d{2})-(\d{3}))$', test_string, flags=re.MULTILINE)
print(match.groups())

print('-' * 30)

wynik = re.sub(r'^((\d{2})-(\d{3}))$', r'\g<3>-\g<2>', test_string, flags=re.MULTILINE)
print(wynik)


