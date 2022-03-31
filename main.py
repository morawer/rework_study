import json
import os
from datetime import datetime, timedelta

from dotenv import load_dotenv

import counter_lines
import excel_writer
import inspections_list
import sender_email
from sabana_class import Sabana

load_dotenv()


def getKey(obj):
    return obj.lines

def formatDate(date):
    dateSplit = date.split('/')
    return '-'.join(reversed(dateSplit))

tokenNotion = os.getenv('TOKEN_NOTION')
database = os.getenv('DATABASE')

date1Formatted = ''
date2Formatted = ''

opt = '3'
while opt > str(2):
    print('Elige tipo de selección de fecha:')
    print('[1]: Última semana.\n[2]: Selección de fecha manual.')
    opt = input('>>>')
    if opt == str(1):
        date1LastWeek = (datetime.now() - timedelta(days=8))
        date1Formatted = str(date1LastWeek.date())
        date2Formatted = str(datetime.now().date())
    elif opt == str(2):
        print('PERIODO DE FECHAS:')
        print('Introduce la primera fecha')
        date1 = input('>>> dd/mm/aaaa >>> ')
        date1Formatted = formatDate(date1)
        print('Introduce la segunda fecha')
        date2 = input('>>> dd/mm/aaaa >>> ')
        date2Formatted = formatDate(date2)

totalLines = 0
checkedAHU = 0
dataArray = []
sabanaArray = []

jsonResponse = inspections_list.todoList(
    tokenNotion, database, date1Formatted, date2Formatted)
jsonData = json.loads(jsonResponse)

for data in jsonData['results']:
    dataArray.clear()

    jsonId = data['id']
    jsonDate = data["created_time"]
    date2 = jsonDate.split("T")[0].split("-")
    dateFinal = "/".join(reversed(date2))
    print(dateFinal)
    
    dataURL = data['url']

    jsonProperties = data['properties']
    jsonOrder = jsonProperties['Pedido']
    jsonOrderTitle = jsonOrder['title']
    for data in jsonOrderTitle:
        dataOrderText = data['text']
        dataOrder = dataOrderText['content']
        print(dataOrder)

    jsonInspector = jsonProperties['Inspector']
    jsonInspectorSelect = jsonInspector['select']
    jsonInspectorName = jsonInspectorSelect['name']
    print('Inspector: ' + jsonInspectorName)

    jsonMo = jsonProperties['MO']
    dataMo = jsonMo['number']
    print(dataMo)

    jsonModel = jsonProperties['Modelo']
    jsonModel_rich_text = jsonModel['rich_text']
    for dataModel in jsonModel_rich_text:
        dataModelAHU = dataModel['plain_text']
        print(dataModelAHU)

    countLines = counter_lines.counterLines(tokenNotion, jsonId)
    print('Numero de lineas: ' + countLines)
    totalLines = totalLines + int(countLines)

    jsonTags = jsonProperties['Tags']
    jsonMultiSelect = jsonTags['multi_select']
    
    counterTags = 0
    for dataName in jsonMultiSelect:
        nameTag = dataName['name']
        counterTags = counterTags + 1
        print(f'[{counterTags}] {nameTag}')
        dataArray.append(nameTag)

    sabana = Sabana(dataOrder, dateFinal, dataMo, dataModelAHU, jsonInspectorName, countLines, dataArray, dataURL)
    checkedAHU = checkedAHU + 1
    excel_writer.excelWriter(sabana)
    sabanaArray.append(sabana)
    print('************************************************')
print(f'Unidades revisadas: {checkedAHU}')

sabanaArray.sort(key=getKey, reverse= True)

for sabana in sabanaArray:
    print(Sabana.__repr__(sabana))
    
sender_email.sendEmail(mail_subject= date2Formatted, mail_body= 'TEST!!')
avgLines = totalLines/checkedAHU    
print(f'La media de lineas por sábana es de {avgLines:.0f} lineas')
