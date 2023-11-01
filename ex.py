import requests

key1 ="pk.eyJ1IjoiZHVkc2pqa2siLCJhIjoiY2xuM2FwbzV4MDlucTJpbncxM3lobzh5ZCJ9.vfwtiKnT4u5Y5y9v2Ttnvg"
local = "St. M QNM 14 - Ceilândia, Brasília - DF, 72210-140"

def geocoding_mapbox(local, key):
  
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{local} Brasil.json?access_token={key}"
    response = requests.get(url)
    return response.json()

dados = geocoding_mapbox(local, key1)

print("Endereço: "+ str(dados['query']))

print("Altitude e longitude: "+str(dados['features'][0]['geometry']['coordinates']))
