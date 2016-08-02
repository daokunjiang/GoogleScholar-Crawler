from openpyxl import load_workbook as ldwb

wb = ldwb(filename='wbtest.xlsx')
ws = wb.create_sheet(title='test1')
ws.append([12,23,56,'m'])
wb.save(filename='wbtest.xlsx')
