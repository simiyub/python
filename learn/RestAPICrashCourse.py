"""
Crash course with Caleb Curry
"""

import requests
import json

response = requests.get('https://api.stackexchange.com/2.3/articles?order=desc&sort=activity&site=stackoverflow')
print(response)
print(response.json())

for data in response.json()['items']:
    print(data['title'])


