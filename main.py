import requests

MY_LAT = 42.696491
MY_LON = 23.326010

ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "d10054c03a6fda2d717c1a48eb8bed6f"

params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
}

response = requests.get(ENDPOINT, params=params)
print(response.json())
