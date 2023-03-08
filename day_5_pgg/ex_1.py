"""
Wczytaj plik daty.txt
Znajdź wszystkie daty i zamień je na format "D.M.Y r."
*Belgii* -> <em>Belgii</em>
"""
import re

with open('daty.txt', encoding='utf-8') as f:
    content = f.read()
    # result = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\g<3>.\g<2>.\g<1>', content)
    result = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3.\2.\1', content)
    # result = re.sub(r'\*(.*?)\*', r'<em>\1</em>', result)
    result = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', result)
    print(result)
