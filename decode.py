from bs4 import BeautifulSoup as bs

with open('xue.txt', 'r', encoding='utf-8') as f:
    doc = bs(f.read())
