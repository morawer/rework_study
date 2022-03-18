import json
import inspections_list
import counter_lines
import os
from dotenv import load_dotenv

load_dotenv()

tokenNotion = os.getenv('TOKEN_NOTION')
database = os.getenv('DATABASE')

#date1 = input('Introduce la primera fecha (yyyy-mm-dd):')
#date2 = input('Introduce la segunda fecha (yyyy-mm-dd):')

date1 = '2022-03-13'
date2 = '2022-03-20'
checkedAHU = 0

jsonResponse = inspections_list.todoList(tokenNotion, database, date1, date2)
jsonData = json.loads(jsonResponse)

for data in jsonData['results']:
    jsonId = data['id']
    jsonDate = data["created_time"]
    Date2 = jsonDate.split("T")[0].split("-")
    DateFinal = "/".join(reversed(Date2))
    print(DateFinal)
    
    jsonProperties = data['properties']
    jsonMo = jsonProperties['MO']
    print(jsonMo['number'])
    
    jsonOrder = jsonProperties['Pedido']
    jsonOrderTitle = jsonOrder['title']
    
    for dataOrder in jsonOrderTitle:
        dataOrderText = dataOrder['text']
        print(dataOrderText['content'])
    
    jsonModel = jsonProperties['Modelo']
    jsonModel_rich_text = jsonModel['rich_text']
    for dataModel in jsonModel_rich_text:
        print(dataModel['plain_text'])

    jsonTags = jsonProperties['Tags']
    jsonMultiSelect = jsonTags['multi_select']
    
    counterTags = 0
    for dataName in jsonMultiSelect:
        nameTag = dataName['name']
        counterTags = counterTags + 1
        print(f'[{counterTags}] {nameTag}')
        
    jsonInspector = jsonProperties['Inspector']
    jsonInspectorSelect = jsonInspector['select']
    jsonInspectorName = jsonInspectorSelect['name']
    checkedAHU = checkedAHU + 1
    print('Inspector: ' + jsonInspectorName)
    print('Numero de lineas: ' + counter_lines.counterLines(tokenNotion, jsonId))
    print('************************************************')
print(f'Unidades revisadas: {checkedAHU}')
