import inspections_list, counter_lines, excel_writer
import json, os
from datetime import datetime
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

tokenNotion = os.getenv('TOKEN_NOTION')
database = os.getenv('DATABASE')

def formatDate(date):
    dateSplit = date.split('/')
    return '-'.join(reversed(dateSplit))


dateNow = str(datetime.now().date())
dateLastWeek = (datetime.now() - timedelta(days=7))
dateLastWeek2 = str(dateLastWeek.date())

print(dateNow)
print(dateLastWeek2)


checkedAHU = 0
dataArray= []

jsonResponse = inspections_list.todoList(
    tokenNotion, database, dateLastWeek2, dateNow)
jsonData = json.loads(jsonResponse)

for data in jsonData['results']:
    dataArray.clear()

    jsonId = data['id']
    jsonDate = data["created_time"]
    date2 = jsonDate.split("T")[0].split("-")
    dateFinal = "/".join(reversed(date2))
    dataArray.append(dateFinal)
    print(dateFinal)
    
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
