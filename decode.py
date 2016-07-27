from pyquery import PyQuery as pyq

with open('test.txt','r',encoding='utf-8') as f:
    docs = f.read()
    res = pyq(docs)
    table = pyq(res('#gsc_a_b'))
    for i in table.find('tr').text():
        print()