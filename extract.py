import requests
import csv

def is_roman_number(s: str):
    roman = ["V", "X", "L", "C", "D", "M"]
    for c in s:
        if c in roman:
            return True
    return False

url = "https://api.cafci.org.ar/fondo?estado=1&include=entidad;depositaria,entidad;gerente,tipoRenta,region,benchmark,clase_fondo&limit=0"

response = requests.get(url)
data = response.json()
data = data["data"]
data = {d["nombre"]:[int(d["clase_fondos"][0]["fondoId"]), int(d["clase_fondos"][0]["id"])] for d in data if d.get("clase_fondos", [])}

data = {d:data[d] for d in data if not is_roman_number(d[-2:])}


print([(d,data[d]) for d in data if d.startswith("Adcap Renta Fija")])
print(len(data))

