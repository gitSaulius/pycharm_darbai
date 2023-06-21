import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

    # define website
url = "http://www.meteo.lt/lt/miestas?placeCode=Vilnius"

# response from the website
response = requests.get(url)
# create a bs4 object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# find all weather info in the class content city
week_days = soup.find_all('span', class_='date')

temperatures = soup.find_all('span', class_='big up-from-zero')

night_temp = [temperature.get_text() for temperature in temperatures[::2]]

week_day = [day.get_text() for day in week_days]

temp_values = night_temp

data = {'weekday': week_day, 'temperature': temp_values}

df=pd.DataFrame(data)

df_sorted=df.sort_values(by='temperature')

plt.bar(df_sorted['weekday'], df_sorted['temperature'])

plt.xlabel('savaites diena')
plt.ylabel('temperatura')
plt.title('Oru prognoze Vilniuje')

plt.show()








