from app_video import Video_Stream
import requests

BASE = 'http://127.0.0.1:5000/' 

dt = [
    {'spectators': 000, 'participant': 'AAAA', 'room': '1234ABCD'},
    {'spectators': 100, 'participant': 'BBBB', 'room': 'DCBA4321'},
    {'spectators': 817, 'participant': 'GASK', 'room': 'ABCD1234'}]

for i in range(len(dt)):
    r = requests.put(BASE + 'Video_Streaming/' + str(i), dt[i])
    print(r.json()) 

video_id = input('DELETE: ')
r = requests.delete(BASE + f'Video_Streaming/{video_id}')
print(r)

# just to wait for user input
video_id = input('GET: ')

r = requests.get(BASE + f'Video_Streaming/{video_id}')
print(r.json()) 
