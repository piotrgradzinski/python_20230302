"""
orlen.txt
- usunięcie spacji między liczbami 3 199 -> 3199
- zamiana " mln" na "000000"
"""
import re
from pprint import pprint

with open('orlen.txt') as file:
    report = file.read()

    # usunięcie spacji między liczbami 3 199 -> 3199
    report = re.sub(r'(\d)\s(\d)', r'\1\2', report)
    # zamiana " mln" na "000000"
    report = re.sub(r'(\d)\s+mln', r'\g<1>000000', report)

    # positive look-ahead
    money = re.findall(r'(\d+)(?=\s?PLN)', report)

    pprint(money)

    with open('order_clean.txt', 'w') as output:
        output.write(report)
