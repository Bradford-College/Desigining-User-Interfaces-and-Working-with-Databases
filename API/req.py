'''
Making a simple api call in python
'''

import requests #type: ignore
import json
url = 'https://reqres.in/api/users'

response = requests.get(url)

print(json.dumps(json.loads(response.content.decode('utf-8')), indent=4))