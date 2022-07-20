import requests
import os

my_secret = os.environ['my_api_key']
def get_news(city,api_key=my_secret, units='metric'):

  url=f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}'
  r=requests.get(url)
  content=r.json()
  with open('data.txt', 'a') as file:
    for variable in content['list']:
      file.write(f"\n{city},{variable['dt_txt']},{variable['main']['temp']},{variable['weather'][0]['description']}")
  


print(get_news(city='Aleppo'))