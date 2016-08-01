# Read in from csv
# with open('sample_input.csv', 'r', encoding='gbk') as f:
#     for x in f:
#         x = x.split(',')
#         name = x[0]
#         url = x[1].strip()
#         print(name)
#         print(url)

from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = 'Good'

ws.append([1,2,3,4,5]) # 横着同一行

# 循环遍历
for i in range(1,101):
      for j in range(1,101):
           ws.cell(row = i, column = j)

wb.save(filename='goodman.xlsx')