from json.tool import main
import requests
API_KEY="257f250f6b543ac4679972513695c446"

BASE_URL=" https://api.openweathermap.org/data/2.5/weather"

city=input("Enter a city name")
request_url=f"{BASE_URL}?q={city}&appid={API_KEY}"
response=requests.get(request_url)

if response.status_code==200:
    print("its successfull")
    data=response.json()
    weather=data['weather'][0]['main']
    print("weather:",weather)
    temperature=round(data['main']['temp']-273.15,2)
    print("Temperature",temperature)
else:
    print("bruh..")