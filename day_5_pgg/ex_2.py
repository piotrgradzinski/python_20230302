"""
Wyciągnąć unikalne domeny z pliku adresy_url.txt
"""
import re

domains = set()
with open('adresy_url.txt', encoding='utf-8') as file:
    for address in file:
        address = address.strip().lower()
        match = re.search(r'https?://(?:www\.)?([^/]+)/.*', address)
        domains.add(match.group(1))

print('\n'.join(sorted(domains)))
