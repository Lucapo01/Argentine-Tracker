import requests
from typing import Dict, List
import csv

def is_roman_number(s: str):
    if s == "I": # ignore number 1
        return False
    roman = ["I", "V", "X", "L", "C", "D", "M"]
    for c in s:
        if c in roman:
            return True
    return False

url = "https://api.cafci.org.ar/fondo?estado=1&include=entidad;depositaria,entidad;gerente,tipoRenta,region,benchmark,horizonte,duration,tipo_fondo,clase_fondo&limit=0&order=clase_fondos.nombre&tipoRentaId=3"

response = requests.get(url)
data = response.json()
data = data["data"]
data = {d["nombre"]:[int(d["clase_fondos"][0]["fondoId"]), int(d["clase_fondos"][0]["id"])] for d in data if d.get("clase_fondos", [])}

data = {d:data[d] for d in data if not is_roman_number(d.split(" ")[-1])}


print(list(data.keys())[:10], list(data.values())[:10])
print(len(data))

with open("engine/funds_bonds.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "fondoId", "clase_fondoId"])
    for d in data:
        writer.writerow([d, data[d][0], data[d][1]])