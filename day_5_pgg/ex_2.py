"""
Wyciągnąć unikalne domeny z pliku adresy_url.txt
"""
import re
from collections import Counter
from pprint import pprint

domains = set()
domains_all = []
with open('adresy_url.txt', encoding='utf-8') as file:
    for address in file:
        address = address.strip().lower()
        match = re.search(r'https?://(?:www\.)?([^/]+)/.*', address)
        domains.add(match.group(1))
        domains_all.append(match.group(1))

print('\n'.join(sorted(domains)))

print('-' * 30)

domain_counter = Counter(domains_all)
for domain, number in domain_counter.items():
    print(f'{domain} - {number}')
