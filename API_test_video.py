import requests

BASE = 'http://127.0.0.1:5000/' 

r = requests.get(BASE + 'test/Webex')

print(r.json()) 