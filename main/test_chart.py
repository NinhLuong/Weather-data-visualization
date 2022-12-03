import codecs
import requests
import urllib.error
import sys
import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


api_key = 'TQ39TAZE5EZHHYRGNANAQ5JJB'
city = 'phan thiet'
url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/' + city + '?key=' + api_key
response = requests.get(url).json()

datetime = []
temp = []
humidity = []
windspeed = []
uvindex = []
num_hour_line =2
num_day_line = 0

fig ,ax = plt.subplots(1, dpi=100, figsize=(6, 6), 
            sharey=True, facecolor='white') 

def animate(h):
    global num_day_line,num_hour_line,datetime,temp,humidity,windspeed,uvindex
    num_hour_line+=1
    datetime.append(str(response["days"][num_day_line]["hours"][num_hour_line]["datetime"]))
    temp.append(round(float((response["days"][num_day_line]["hours"][num_hour_line]["temp"]-32)/1.8)))
    humidity.append(float(response["days"][num_day_line]["hours"][num_hour_line]['humidity']))
    windspeed.append(float(response["days"][num_day_line]["hours"][num_hour_line]['windspeed']))
    uvindex.append(float(response["days"][num_day_line]["hours"][num_hour_line]['uvindex']))
    day = str(response["days"][num_day_line]["datetime"])
    
    if (num_hour_line>22):
        num_day_line+=1
        num_hour_line=2
        datetime = []
        temp = []
        humidity = []
        windspeed = []
        uvindex = []

    print(datetime)
    print('========================================')
    print(temp)
    print('========================================')
    print(humidity)
    print('========================================')
    print(windspeed)
    print('========================================')
    print(uvindex)
    print('========================================')
    print(num_day_line)
    print(num_hour_line)
    plt.cla()
    fig.suptitle('Line Graph: Weather forecast for the next few hours of date {}'.format(day),size=9)
    plt.plot(datetime, humidity, 'b', label='Humidity (%)')
    plt.plot(datetime, temp, 'r', label='Temp (℃)')
    plt.plot(datetime, windspeed, 'g', label='Wind speed (m/s)')
    plt.plot(datetime, uvindex,'y', label="UV index")
    plt.xticks(fontsize = 5, rotation = 20)
    plt.legend(loc='best')
    plt.xlabel("Time")
    plt.ylabel("Index")  

anim = FuncAnimation(fig=fig, func=animate, interval = 1000)
plt.show()  