import requests

# Local dev server location
# JSON file to avoid py object response

BASE = 'http://127.0.0.1:5000/' 

r = requests.get(BASE + 'test/Webex')
# r.status_code

# response = requests.post(BASE + 'test')

print(r.json()) 