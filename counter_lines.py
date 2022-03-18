import requests
import json

def counterLines(tokenNotion, pageId ):

    url = f"https://api.notion.com/v1/blocks/{pageId}/children?page_size=100"

    payload = {}
    headers = {
        'Notion-Version': '2021-05-13',
        'Authorization': tokenNotion
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    jsonData = json.loads(response.text)

    lines = 0
    for data in jsonData['results']:
        if data['object'] == 'block':
            lines = lines + 1
    return f'{lines-1}'
    
