import requests
import json

def todoList(tokenNotion, database, date1, date2) :
    
    url = f"https://api.notion.com/v1/databases/{database}/query"
    
    payload = json.dumps({
        "filter": {
            "and": [
                {
                    "property": "Creado",
                    "created_time": {
                        "after": date1
                    }
                },
            {
                    "property": "Creado",
                    "created_time": {
                        "before": date2
                    }
            }

            ]
        }
    })
    headers = {
        'Notion-Version': '2021-05-13',
        'Authorization': tokenNotion,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return(response.text)
