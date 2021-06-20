import requests

BASE = 'http://127.0.0.1:5000/' 

# r = requests.get(BASE + 'Video_Streaming/1')
r = requests.put(BASE + 'Video_Streaming/1', {'participant': 1})

print(r.json()) 