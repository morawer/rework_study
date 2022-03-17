import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

tokenNotion = os.getenv('TOKEN_NOTION')
database = os.getenv('DATABASE')

url = f"https://api.notion.com/v1/databases/{database}/query"

payload = json.dumps({
    "filter": {
        "property": "Creado",
        "created_time": {
            "after": "2022-03-15"
        }
    }
})
headers = {
    'Notion-Version': '2021-05-13',
    'Authorization': tokenNotion,
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

#print(response.text)
jsonData = json.loads(response.text)


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
