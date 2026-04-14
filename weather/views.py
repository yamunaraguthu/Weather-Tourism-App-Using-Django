import requests
from datetime import datetime
import pytz
from django.shortcuts import render

# Replace with your API keys
WEATHER_API_KEY = "767c1905e7ab50e9f6751515fd1e7d46"
UNSPLASH_API_KEY = "adKnaBDmLag5wNLBFh26k4EWzSsIwWB4rDexoILrlgQ"


def get_tourism_info(city):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{city}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("extract", "No tourism info available.")
    return "Tourism info not found."


# WIKI_API_URL="https://en.wikipedia.org/api/rest_v1/page/summary/{place_name}"
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url).json()
    
    if response.get("cod") != 200:
        return None

    timezone_offset = response["timezone"]  # Offset in seconds
    country_code = response["sys"]["country"]
    city_name = response["name"]
    temp = response["main"]["temp"]
    weather_desc = response["weather"][0]["description"]

    # Convert UTC time to local time
    utc_time = datetime.utcnow()
    local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(pytz.FixedOffset(timezone_offset // 60))
    
    # Get City Image from Unsplash
    unsplash_url = f"https://api.unsplash.com/search/photos?query={city_name}&client_id={UNSPLASH_API_KEY}&per_page=1"
    image_response = requests.get(unsplash_url).json()
    city_image = image_response["results"][0]["urls"]["regular"] if image_response["results"] else ""

    # Country Flag URL
    country_flag = f"https://flagsapi.com/{country_code}/flat/64.png"
   

    return {
        "city": city_name,
        "country": country_code,
        "temperature": temp,
        "weather": weather_desc,
        "local_time": local_time.strftime('%Y-%m-%d %H:%M:%S'),
        "city_image": city_image,
        "get_tourism_info": get_tourism_info,
        "country_flag": country_flag,
    }

def weather_view(request):
    city = request.GET.get("city", "Tokyo")  # Default city
    weather_data = get_weather(city)

    return render(request, "index.html", {"weather": weather_data})
