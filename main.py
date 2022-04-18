import json
import os
from datetime import datetime, timedelta

from dotenv import load_dotenv

import counter_lines
import excel_writer
import graphs
import inspections_list
import sender_email
from sabana_class import Sabana

load_dotenv()

#Get period the execution program date and last week date.
def getDates(): 
    date1LastWeek = (datetime.now() - timedelta(days=8))
    weekNum = date1LastWeek.strftime('%U')
    subjectEmail = f'SEMANA {weekNum}: Informe de equipos revisados'
    date1Formatted = str(date1LastWeek.date())
    date2Formatted = str(datetime.now().date())
    return date1Formatted, date2Formatted, subjectEmail

def getKey(obj):
    return obj.lines
#Get token and database id from .env
tokenNotion = os.getenv('TOKEN_NOTION')
database = os.getenv('DATABASE')
#Variables
date1Formatted = ''
date2Formatted = ''
weekNum = ''
totalLines = 0
checkedAHU = 0
dataArray = []
sabanaArray = []
tagsArray = []

date1Formatted, date2Formatted, subjectEmail = getDates()

print('[+] Obteniendo equipos revisados...')
print('************************************************')

#Do the request to Notion and get the Json with the data list.
jsonResponse = inspections_list.toDoList(
    tokenNotion, database, date1Formatted, date2Formatted)
jsonData = json.loads(jsonResponse)

#Read the json and get the data in variables
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
    
    #Create a object with the datas.
    sabana = Sabana(dataOrder, dateFinal, dataMo, dataModelAHU, jsonInspectorName, int(countLines), dataArray, dataURL)
    #Write a excel row with the object datas.
    excel_writer.excelWriter(sabana)
    #Add the object into the a list.
    sabanaArray.append(sabana)
    print('************************************************')
    
sabanaLenght = len(sabanaArray)
print(f'Unidades revisadas: {sabanaLenght}')

sabanaArray.sort(key=getKey, reverse=True)
avgLines = totalLines/sabanaLenght
graphs.graphsAvgCreator()
sender_email.sendEmail(mail_subject= subjectEmail, mail_body= sabanaArray, avgLines=avgLines, tagsArray=tagsArray)
