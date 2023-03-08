"""
orlen.txt
- usunięcie spacji między liczbami 3 199 -> 3199
- zamiana " mln" na "000000"
"""
import re

with open('orlen.txt') as file:
    report = file.read()

    report = re.sub(r'', r'', report)

    with open('order_clean.txt', 'w') as output:
        output.write(report)
