import json
import inspections_list
import counter_lines
import excel_writer
import os
from dotenv import load_dotenv

load_dotenv()

tokenNotion = os.getenv('TOKEN_NOTION')
database = os.getenv('DATABASE')

def formatDate(date):
    dateSplit = date.split('/')
    return '-'.join(reversed(dateSplit))

print('PERIODO DE FECHAS:')
date1 = input('Introduce la primera fecha (dd-mm-aaaa):')
date1Formatted = formatDate(date1)
date2 = input('Introduce la segunda fecha (dd-mm-aaaa):')
date2Formatted = formatDate(date2)

checkedAHU = 0
dataArray= []

jsonResponse = inspections_list.todoList(tokenNotion, database, date1Formatted, date2Formatted)
jsonData = json.loads(jsonResponse)

for data in jsonData['results']:
    dataArray.clear()

    jsonId = data['id']
    jsonDate = data["created_time"]
    Date2 = jsonDate.split("T")[0].split("-")
    DateFinal = "/".join(reversed(Date2))
    dataArray.append(DateFinal)
    print(DateFinal)
    
    jsonProperties = data['properties']
    jsonOrder = jsonProperties['Pedido']
    jsonOrderTitle = jsonOrder['title']
    for dataOrder in jsonOrderTitle:
        dataOrderText = dataOrder['text']
        dataArray.append(dataOrderText['content'])
        print(dataOrderText['content'])
    
    jsonInspector = jsonProperties['Inspector']
    jsonInspectorSelect = jsonInspector['select']
    jsonInspectorName = jsonInspectorSelect['name']
    dataArray.append(jsonInspectorName)
    print('Inspector: ' + jsonInspectorName)
 
    jsonProperties = data['properties']
    jsonMo = jsonProperties['MO']
    dataArray.append(jsonMo['number'])
    print(jsonMo['number'])
    
    jsonModel = jsonProperties['Modelo']
    jsonModel_rich_text = jsonModel['rich_text']
    for dataModel in jsonModel_rich_text:
        dataArray.append(dataModel['plain_text'])
        print(dataModel['plain_text'])
        
    countLines = counter_lines.counterLines(tokenNotion, jsonId)
    print('Numero de lineas: ' + countLines)
    dataArray.append(countLines)

    jsonTags = jsonProperties['Tags']
    jsonMultiSelect = jsonTags['multi_select']
    
    counterTags = 0
    for dataName in jsonMultiSelect:
        nameTag = dataName['name']
        counterTags = counterTags + 1
        print(f'[{counterTags}] {nameTag}')
        dataArray.append(nameTag)
        
    checkedAHU = checkedAHU + 1
    excel_writer.excelWriter(dataArray)
    print('************************************************')
print(f'Unidades revisadas: {checkedAHU}')
