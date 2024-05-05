import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

MY_LAT = 42.696491
MY_LON = 23.326010

ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "d10054c03a6fda2d717c1a48eb8bed6f"
ACCOUNT_SID = "YOUR ACCOUNT SID"
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(ENDPOINT, params=params)
response.raise_for_status()
weather_data = response.json()
#print(weather_data["list"][0]["weather"][0]["id"])


will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(ACCOUNT_SID, AUTH_TOKEN, http_client=proxy_client)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="YOUR TWILIO VIRTUAL NUMBER",
        to="YOUR TWILIO VERIFIED REAL NUMBER"
    )
    print(message.status)
