from  datetime import datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import json
import sys

def dattim():
    current = datetime.now()
    print("date and time ", current)
    dt= current.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt)
    return dt


def cNews():
    news_url="https://news.google.com/news/rss"
    tex=urlopen(news_url)
    xml_page=tex.read()
    tex.close()
    page=BeautifulSoup(xml_page,"lxml")
    news_list=page.findAll("item")
    for news in news_list:
        print(news.title.text)
        print(news.link.text)
        #print(news.pubDate.text)
        print("-"*60)
    return news



def weather(): 
    apiKey = "37496d91404adcec15e926979834fc2c"
    url = "http://api.openweathermap.org/data/2.5/weather?"
    cityName = input("Enter city name you want to search : ") 
    completeUrl = url + "appid=" + apiKey + "&q=" + cityName 
    response = requests.get(completeUrl) 
    x = response.json() 
    if x["cod"] != "404": 
       y = x["main"] 
       currentTemperature = y["temp"] 
       currentPressure = y["pressure"] 
       currentHumidiy = y["humidity"] 
       z = x["weather"] 
       weatherDescription = z[0]["description"] 
       print(" Temperature (in kelvin unit) = " +
                str(currentTemperature) + 
             "\n atmospheric pressure (in hPa unit) = " +
                str(currentPressure) +
             "\n humidity (in percentage) = " +
                str(currentHumidiy) +
            "\n description = " +
                str(weatherDescription)) 
    else: 
       print(" City Not Found ") 
  

print("-- Welcome --")
print()
while(True):
    print()
    print("Enter 1 to view Date and Time")
    print("Enter 2 to View some news")
    print("Enter 3 to view weather of a particular city")
    print("Enter 4 to exit")

    print()
    k = int(input("Enter Your Choice: "))
    if k==1:
        dattim()
    elif k==2:
        cNews()
    elif k==3:
        weather()
    elif k==4:
        sys.exit()
