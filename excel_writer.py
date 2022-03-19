from openpyxl import load_workbook

def excelWriter(dataArray):
    wb = load_workbook('dataAHU.xlsx')
    sheet = wb.active
    sheet.title = 'dataAHU'
    lastRow = sheet.max_row
    lenghtData = len(dataArray)
    
    for data in range (0, lenghtData):
        sheet.cell(row=lastRow + 1 , column=data + 1, value=dataArray[data])
        
    wb.save('dataAHU.xlsx')
