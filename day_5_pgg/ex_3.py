"""
Wczytać plik emails.txt i odfiltrować poprawne mejle:
- usunąć białe znaki
- przerobić na małe litery
- usunąć duplikaty mejli
- odflitrować tylko (w miarę) poprawne adresy email
- wynik zapisać do pliku
"""
import re

emails = set()
with open('emails.txt') as file:
    for line in file:
        if line.count('@') != 1:
            continue

        address = line.strip().lower()
        # usunięcie spacji
        # address = address.replace(' ', '')

        # usunięcie białych znaków
        address = re.sub(r'\s+', '', address)
        # if re.match(r'[\w.+-]+@[\w.+-]+\.[\w.+-]+', address):
        if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', address):
            emails.add(address)

with open('emails_cleaned.txt', 'w') as output_file:
    output_file.write('\n'.join(emails))
