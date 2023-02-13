"""Create functions that reply to users messages"""

import random
import data
import requests
import json
from google_images_search import GoogleImagesSearch
import game_compare

def handle_response_random(message, user_message:str) -> str:
    """
    generate response according to user input
    """
    p_message = user_message.lower()

    if p_message in data.HI:
        return (True, f'Hey there, {message.author} !')

def handle_response_standard(user_message:str) -> str:
    """
    generate responses according to specific keywords
    """
    p_message = user_message.lower()
    
    if p_message == '!help':
        return (True, data.HELP)
    
    elif p_message == '!roll':
        return (True, str(random.randint(1,6)))
    
    elif p_message == '!inspire':
        return (True, get_quote())
    
    elif p_message == '!weatherlabege':
        return (True, get_weather_Labege())
    
    elif p_message == '!weathergrenoble':
        return (True, get_weather_Grenoble())
    
    elif p_message == '!startgame':
        return (True, game_compare.start_game())
    
    elif p_message[:5] == '!game':
        return (True, game_compare.compare(p_message[5:]))
    
    elif p_message[:6] == '!image':
        return (True, search_image(p_message[6:]))

def get_quote():
    quote = requests.get("https://zenquotes.io/api/random")
    json_quote = json.loads(quote.text)
    response = json_quote[0]['q'] + ' - ' + json_quote[0]['a']
    return response

def get_weather(city:str) -> str:
    lat = data.CITY_DATA[city]['lat']
    lon = data.CITY_DATA[city]['lon']
    api = data.API_KEY_WEATHER
    forecast_data = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api}&units=metric")
    json_forecast = json.loads(forecast_data.text)
    city_name = json_forecast['city']['name']
    country = json_forecast['city']['country']
    def three_hour_forecast(json_forecast, index):
        detail_forecast = {
            'time': json_forecast['list'][index]['dt_txt'],
            'temp': json_forecast['list'][index]['main']['temp'],
            'feels_like': json_forecast['list'][index]['main']['feels_like'],
            'description': json_forecast['list'][index]['weather'][0]['description']
        }
        return detail_forecast
    first_forecast = three_hour_forecast(json_forecast, 0)
    second_forecast = three_hour_forecast(json_forecast, 1)
    third_forecast = three_hour_forecast(json_forecast, 2)
    forth_forecast = three_hour_forecast(json_forecast, 3)
    forecast_list = [first_forecast, second_forecast, third_forecast, forth_forecast]
    response = (f"**{city_name}, {country} 3 hour forecast**\n")
    for forecast in forecast_list:
        string = (
            f"Time: {forecast['time']}\n"
            f"Temperature: {forecast['temp']}\n"
            f"Feels like: {forecast['feels_like']}\n"
            f"Description: {forecast['description']}\n"
        )
        response += string
    return response
    
def get_weather_Labege() -> str:
    return get_weather('Labege')

def get_weather_Grenoble() -> str:
    return get_weather('Grenoble')

def search_image(query):
    gis = GoogleImagesSearch(data.API_GOOGLE, data.CX_GOOGLE_IMAGE)
    gis.search(search_params={
        'q':query,
        'num':1,
        'fileType': 'jpg|gif|png',
        'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived',
        'safe': 'off'
    })
    return gis.results()[0].url