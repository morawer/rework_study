from importlib.resources import path
from turtle import mode
from openpyxl import load_workbook
from openpyxl import Workbook
import os

def excelWriter(dataArray):
    
    fileName = 'dataAHU.xlsx'
    pathFilename = 'U:\SISTEMA GESTIÓN CALIDAD\02 PROCEDIMIENTOS\PR-003 - CONTROL DE PRODUCTO NO CONFORME\01 PRODUCCIÓN\05 CONTROL RETRABAJOS (SÁBANAS)\Sabanas AHU.xlsx'
    
    if os.path.exists(fileName):
        wb = load_workbook(pathFilename)
    else:
        wb = Workbook()
    
    sheet = wb.active
    sheet.title = 'dataAHU'
    lastRow = sheet.max_row
    lenghtData = len(dataArray)

    for data in range (0, lenghtData):
        sheet.cell(row=lastRow + 1, column=data + 1, value=dataArray[data])
        
    wb.save(pathFilename)
    wb.close()