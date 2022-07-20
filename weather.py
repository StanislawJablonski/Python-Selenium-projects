import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://pogoda.interia.pl/prognoza-szczegolowa-gdansk,cId,8048')
soup = BeautifulSoup(page.content, 'html.parser')

week = soup.find(class_='main-content col-xs-12 col-rs-12 col-sm-12 col-md-8 col-lg-8')
days = soup.find_all(class_ = 'weather-entry')

#print(days)
#costam = [days.find().get_text() for day in days]

hour = [day.find(class_ = 'entry-hour').find(class_ = 'hour').get_text() for day in days ]
temp = [day.find(class_ = 'entry-forecast').find(class_ = 'forecast-temp').get_text() for day in days]
clouds = [day.find(class_ = 'entry-forecast').find(class_ = 'forecast-phrase').get_text() for day in days]
rain = [day.find(class_ = 'entry-precipitation').find(class_ = 'entry-precipitation-label rain').get_text() for day in days]

weather_stuff = pd.DataFrame (
	{
		'hour': hour,
		'temperature': temp,
		'clouds': clouds,
		'rain': rain,
	})

print(weather_stuff)

