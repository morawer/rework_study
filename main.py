import json
import os
from datetime import datetime, timedelta

from dotenv import load_dotenv

import counter_lines
import excel_writer
import inspections_list
import sender_email
from sabana_class import Sabana
import graphs

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
weekNum = ''
totalLines = 0
checkedAHU = 0
dataArray = []
sabanaArray = []
tagsArray = []

date1LastWeek = (datetime.now() - timedelta(days=8))
weekNum = date1LastWeek.strftime('%U')
subjectEmail = f'SEMANA {weekNum}: Informe de equipos revisados'
date1Formatted = str(date1LastWeek.date())
date2Formatted = str(datetime.now().date())

print('[+] Obteniendo equipos revisados...')
print('************************************************')


jsonResponse = inspections_list.toDoList(
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
        tagsArray.append(nameTag)
    
    sabana = Sabana(dataOrder, dateFinal, dataMo, dataModelAHU, jsonInspectorName, int(countLines), dataArray, dataURL)
    excel_writer.excelWriter(sabana)
    sabanaArray.append(sabana)
    print('************************************************')
    
sabanaLenght = len(sabanaArray)
print(f'Unidades revisadas: {sabanaLenght}')

sabanaArray.sort(key=getKey, reverse=True)
avgLines = totalLines/sabanaLenght
graphs.graphsAvgCreator()
sender_email.sendEmail(mail_subject= subjectEmail, mail_body= sabanaArray, avgLines=avgLines, tagsArray=tagsArray)
