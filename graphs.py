import matplotlib.pyplot as plt
import numpy as np
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
    counterAHU = []
    weeksAcum = 0
    initWeek = True

    path = 'dataAHU.xlsx'

    if os.path.exists(path):
        wb = load_workbook(path)
        sheet = wb.active
        lastRow = sheet.max_row

        for row in range(2, lastRow):
            cell_obj = sheet.cell(row=row, column=1)
            date = cell_obj.value
            dateformat = datetime.strptime(date, '%d/%m/%Y')
            weeknumber = dateformat.strftime('%U')

            if (weeknumber != weekNumberAux or initWeek == True):
                if row > 2:
                    dates.append(weeknumber)
                    linesAvg = int(linesAcum)/int(weeksAcum)
                    lines.append(linesAvg)
                    counterAHU.append(weeksAcum)
                    linesAvg = 0
                    linesAcum = 0
                    weeksAcum = 0
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
    else:
        print('El archivo no existe')

    
        
    dates.reverse()
    lines.reverse()

    fig, ax = plt.subplots()
    x = np.arange(len(dates))
    width = 0.35
    bar1 = ax.bar(x - width/2, counterAHU, width, label="Nº UTA's")
    bar2 = ax.bar(x + width/2, lines, width, label= "Media de lineas")
    
    ax.set_ylabel('Media por UTA')
    ax.set_title('Gráfica media de lineas por semana y UTA')
    ax.set_xticks(x)
    ax.set_xticklabels(dates)
    ax.legend()

    fig.tight_layout()
    
    dateGraph = datetime.now()
    dateGraphWeekNumber = dateGraph.strftime('%U')
    plt.savefig(f'avg_week_{dateGraphWeekNumber}_graph')
