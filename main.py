import json
import inspections_list
import os
from dotenv import load_dotenv

load_dotenv()

tokenNotion = os.getenv('TOKEN_NOTION')
database = os.getenv('DATABASE')

date1 = input('Introduce la primera fecha (yyyy-mm-dd):')
date2 = input('Introduce la segunda fecha (yyyy-mm-dd):')

#date1 = '2022-03-15'
#date2 = '2022-03-18'

jsonResponse = inspections_list.todoList(tokenNotion, database, date1, date2)
jsonData = json.loads(jsonResponse)

for data in jsonData['results']:
    jsonDate = data["created_time"]
    Date2 = jsonDate.split("T")[0].split("-")
    DateFinal = "/".join(reversed(Date2))
    print(DateFinal)
    
    jsonProperties = data['properties']
    jsonMo = jsonProperties['MO']
    print(jsonMo['number'])
    
    jsonTags = jsonProperties['Tags']
    jsonMultiSelect = jsonTags['multi_select']

    jsonOrder = jsonProperties['Pedido']
    jsonOrderTitle = jsonOrder['title']
    
    for dataOrder in jsonOrderTitle:
        dataOrderText = dataOrder['text']
        print(dataOrderText['content'])
    
    jsonModel = jsonProperties['Modelo']
    jsonModel_rich_text = jsonModel['rich_text']
    for dataModel in jsonModel_rich_text:
        print(dataModel['plain_text'])

    for dataName in jsonMultiSelect:
        print(dataName['name'])
        
    jsonInspector = jsonProperties['Inspector']
    jsonInspectorSelect = jsonInspector['select']
    jsonInspectorName = jsonInspectorSelect['name']
    print('Inspector: ' + jsonInspectorName)
    print('************************************************')
