url = 'https://solved.ac/api/v3/problem/show?problemId=13460'

import requests
import json

# Request
requestData = requests.get(url)

json_ob = json.loads(requestData.content)
print(json_ob['level'])
