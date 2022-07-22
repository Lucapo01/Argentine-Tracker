import json
import requests

payload = {"hola": "chau"}
r = requests.post("http://localhost:8000/engineUpdate/1234", json=payload)