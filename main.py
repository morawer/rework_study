import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

tokenNotion = os.getenv('TOKEN_NOTION')
database = os.getenv('DATABASE')

url = f"https://api.notion.com/v1/databases/{database}/query"

payload = "<file contents here>"
headers = {
    'Notion-Version': '2021-05-13',
    'Authorization': tokenNotion,
    'Content-Type': 'text/plain'
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

    jsonPedido = jsonProperties['Pedido']
    jsonPedidoTitle = jsonPedido['title']
    
    for dataOrder in jsonPedidoTitle:
        dataOrderText = dataOrder['text']
        print(dataOrderText['content'])
    
    for dataName in jsonMultiSelect:
        print(dataName['name'])
        
    jsonInspector = jsonProperties['Inspector']
    jsonInspectorSelect = jsonInspector['select']
    jsonInspectorName = jsonInspectorSelect['name']
    print('Inspector: ' + jsonInspectorName)
    print('************************************************')
