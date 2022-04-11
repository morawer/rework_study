import matplotlib.pyplot as plt
from openpyxl import load_workbook
import os
from datetime import datetime


def graphsAvgCreator():
    
    weekNumberAux = 0
    linesAcum = 0
    linesAvg = 0
    linesRow = 0
    dates = []
    lines = []
    weeksAcum = 0
    initWeek = True

    path = 'dataAHU.xlsx'

    if os.path.exists(path):
        wb = load_workbook(path)
    else:
        print('El archivo no existe')

    sheet = wb.active
    lastRow = sheet.max_row

    for row in range(1, lastRow):
        cell_obj = sheet.cell(row=row, column=1)
        date = cell_obj.value
        dateformat = datetime.strptime(date, '%d/%m/%Y')
        weeknumber = dateformat.strftime('%U')
                        
        if (weeknumber != weekNumberAux or initWeek == True):
            if row > 1:
                dates.append(weeknumber)
                linesAvg = int(linesAcum)/int(weeksAcum)
                lines.append(linesAvg)
                linesAvg = 0
                linesAcum = 0
                weeksAcum=0
                initWeek = False
            weekNumberAux = weeknumber
            linesAcum = 0
            linesRow = sheet.cell(row=row, column=6)
            linesInt = linesRow.value
            linesAcum = int(linesAcum) + int(linesInt)
            weeksAcum = weeksAcum + 1
        else:
            linesRow = sheet.cell(row=row, column=6)
            linesInt = linesRow.value
            linesAcum = int(linesAcum) + int(linesInt)
            weeksAcum = weeksAcum + 1
        
    dates.reverse()
    lines.reverse()

    eje_x = dates
    eje_y = lines

    # Creamos Gráfica
    plt.bar(eje_x, eje_y)

    # Legenda en el eje y
    plt.ylabel('Media de lineas por equipo:')

    # Legenda en el eje x
    plt.xlabel('Semana:')

    # Título de Gráfica
    plt.title('Gráfica de media de líneas')

    # Mostramos Gráfica
    plt.savefig(f'week_{weeknumber}_graph')


graphsAvgCreator()
