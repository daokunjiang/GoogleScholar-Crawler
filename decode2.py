from bs4 import BeautifulSoup as bs

def is_author_column(tag):
    return (tag.string == '作者') and tag.has_attr('class') and (tag.get('class') == ['gsc_field'])

def is_magazine_column(tag):
    return (tag.string == '期刊') and tag.has_attr('class') and (tag.get('class') == ['gsc_field'])

with open('test.txt', 'r', encoding='utf-8') as f:
    doc = bs(f.read(), "lxml")
    x = doc.find(is_magazine_column)
    x = x.find_next_sibling()
    print(x.string)

# tag.has_attr('class') and (tag.get('class') == 'gsc_field') and
