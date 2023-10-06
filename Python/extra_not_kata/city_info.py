""" 
For the next two challenges, instead of classes, we will be learning how to work 
with API. We will cover API’s much more in depth throughout the course, for these 
challenges all you need to worry about is the data structures stored within the 
response variable that we have defined for you.

You can click here to view the object directly in your browser, or simply print 
it out in the terminal print(response). Do the structures look familar?

Specs
Let's define a city_info function

city_info should take one argument, in this case our response variable
It should return a dictionary with the following keys:
'city' - the name of the city in response
'lat' - the latitude of the city in response as a float
'lon' - the longitude of the city in response as a float
city_info(response)
{
  'city': 'London', 
  'lat': 51.5073219,
  'lon': -0.1276474
} 
"""

import requests
response = requests.get("https://weather.lewagon.com/geo/1.0/direct?q=london").json()

def city_info(response):
    city = response[0]['name']
    lat = response[0]['lat']
    lon = response[0]['lon']
    
    return {'city': city, 'lat': lat, 'lon': lon}
    