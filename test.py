import requests

# Local dev server location
# JSON file to avoid py object response

BASE = 'http://127.0.0.1:5000/' 

response = requests.get(BASE + 'test')

response = requests.post(BASE + 'test')

print(response.json()) 