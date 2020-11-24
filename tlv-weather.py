import requests, json

api_key = "098009948ba5d2f73042764a9e43d3cc"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "Tel Aviv"

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":

    y = x["main"]

    current_temperature = y["temp"]
    Celsius = int(current_temperature - 273.15)

    z = x["weather"]
    weather_description = z[0]["description"]

    # print following values 
    print(" Temperature = " +
          str(Celsius) +
          "\n description = " +
          str(weather_description))

else:
    print(" City Not Found ") 
