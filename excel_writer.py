from turtle import mode
from openpyxl import load_workbook
from openpyxl import Workbook
import os

def excelWriter(dataArray):
    
    fileName = 'dataAHU.xlsx'
    
    if os.path.exists(fileName):
        wb = load_workbook(fileName)
    else:
        wb = Workbook()
    
    sheet = wb.active
    sheet.title = 'dataAHU'
    lastRow = sheet.max_row
    lenghtData = len(dataArray)
    print(lastRow)
    for data in range (0, lenghtData):
        sheet.cell(row=lastRow + 1, column=data + 1, value=dataArray[data])
        
    print(lastRow)
    wb.save('dataAHU.xlsx')
    wb.close()
    sheet.delete_rows(idx=1)
