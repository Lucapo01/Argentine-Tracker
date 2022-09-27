import requests

url = "http://fcitracker.online:8000/engineUpdate/123/a"

r = requests.post(url, json={})
print(r.text)