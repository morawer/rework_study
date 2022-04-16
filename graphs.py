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

        for row in range(2, lastRow + 1):
            cell_obj = sheet.cell(row=row, column=1)
            date = cell_obj.value
            dateformat = datetime.strptime(date, '%d/%m/%Y')
            weeknumber = dateformat.strftime('%U')

            if (weeknumber != weekNumberAux or initWeek == True or row == lastRow):
                if row > 2:
                    dates.append(weekNumberAux)
                    linesAvg = int(linesAcum)/int(weeksAcum)
                    lines.append(float("{:.1f}".format(linesAvg)))
                    counterAHU.append(weeksAcum)
                    linesAvg = 0
                    linesAcum = 0
                    weeksAcum = 0
                    initWeek = True
                elif row == lastRow:
                    dates.append(weeknumber)
                    linesAvg = int(linesAcum)/int(weeksAcum)
                    lines.append(float("{:.1f}".format(linesAvg)))
                    counterAHU.append(weeksAcum)
                    linesAvg = 0
                    linesAcum = 0
                    weeksAcum = 0
                    initWeek = True
                weekNumberAux = weeknumber
                linesAcum = 0
                linesRow = sheet.cell(row=row, column=6)
                linesInt = linesRow.value
                linesAcum = int(linesAcum) + int(linesInt)
                weeksAcum = weeksAcum + 1
                initWeek = False
            else:
                linesRow = sheet.cell(row=row, column=6)
                linesInt = linesRow.value
                linesAcum = int(linesAcum) + int(linesInt)
                weeksAcum = weeksAcum + 1
                initWeek = False
    else:
        print('El archivo no existe')

    fig, ax = plt.subplots()
    x = np.arange(len(dates))
    width = 0.35
    bar1 = ax.bar(x - width/2, counterAHU, width, label="Nº UTA's")
    bar2 = ax.bar(x + width/2, lines, width, label= "Media de lineas")
    
    ax.set_xlabel('Semanas')
    ax.set_title("Número de UTA's y media de líneas por semana")
    ax.set_xticks(x)
    ax.set_xticklabels(dates)
    ax.legend()
    
    def autolabel(bars):
        for bar in bars:
            height = bar.get_height()
            ax.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

    autolabel(bar1)
    autolabel(bar2)
    fig.tight_layout()
    
    dateGraph = datetime.now()
    dateGraphWeekNumber = dateGraph.strftime('%U')
    plt.savefig(f'avg_week_{dateGraphWeekNumber}_graph')
