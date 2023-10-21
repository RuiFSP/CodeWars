""" 
Let's look at another OpenWeatherMap API response which is a bit bigger - this time 
we'll be looking at their weather forecast feature. 🌦️

Again, you can print the response variable directly in the terminal, or click here 
to access. These Chrome or Firefox extensions might help make it a bit more readable in your browser.

Using our new response's data structure we can define a function weather_forecast 
which will take one parameter - response of the same format as the example above - 
and return tomorrow's weather forecast for a given city!

Specs
weather_forecast should return a string:
“The weather in <city> tomorow is <forecast>”
The weather_state_name key is a good description of a forecast, but how can we access it 🤔
The forecast should be for tomorrow's date, where is that located in the response?
remember dicts built in get method to help keep your program from crashing
Dealing with dates
Let's not trust that our APIs response dates will always come in the same order - in fact 
OpenWeatherMap often returns forecast starting from the current day. How can we enhance our 
function to make sure it always gets the forecast for the tomorrow and that it will update each day?

importing the datetime library and this post on stackoverflow may help you create a string 
with tomorrow's date (like 2022-06-28)
the in operator in Python may help you check if you've found the weather for the right day """


import requests

response = requests.get("https://weather.lewagon.com/data/2.5/forecast?lat=51.5073219&lon=-0.1276474&units=metric").json()

import datetime

def weather_forecast(response):
    
    city = response.get("city")['name']
    
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    tomorrow_date = tomorrow.strftime('%Y-%m-%d')
    
    my_dict = {}
    
    # my dict for dates and predictions
    for date_info in response.get("list", []):
        date_string = date_info.get("dt_txt")
        
        # Check if date_string is not None
        if date_string is not None:
            datetime_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
            date_only_obj = datetime_obj.date()
            formatted_date_string = date_only_obj.strftime('%Y-%m-%d')
            forecast = date_info.get("weather", [{}])[0].get('description', 'No forecast available')
            my_dict[formatted_date_string] = forecast

    #print(my_dict)
    
    prediction_for_tomorrow = my_dict.get(tomorrow_date, "No forecast for tomorrow")
    
    return f"The weather in {city} tomorrow is {prediction_for_tomorrow}"

print(weather_forecast(response=response))