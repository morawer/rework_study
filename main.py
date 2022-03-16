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
    jsonFecha = data["created_time"]
    fecha2 = jsonFecha.split("T")[0].split("-")
    fechaFinal = "/".join(reversed(fecha2))
    print(fechaFinal)
    
    jsonProperties = data['properties']
    jsonEtiquetas = jsonProperties['Etiquetas']
    jsonMultiSelect = jsonEtiquetas['multi_select']
    
    for dataName in jsonMultiSelect:
        print(dataName['name'])
        
    jsonInspector = jsonProperties['Inspector']
    jsonInspectorSelect = jsonInspector['select']
    jsonInspectorName = jsonInspectorSelect['name']
    print('Inspector: ' + jsonInspectorName)
