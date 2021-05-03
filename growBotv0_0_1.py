#! Python3

#growBot: House Plant Life Support

from datetime import datetime
import requests, re

ua = "Chrome/44.0.2403.157"
timeFindWide = re.compile('>\d.?.?.?.?.?.?M</div>')
timeFindFine = re.compile('\d.+M')
googleSearch = "https://www.google.com/search?q="
now = datetime.now().strftime('%H:%M')

def webPull(url):
    session = requests.Session()
    session.headers['User-Agent'] = ua
    html = session.get(url)
    return(html.text)

def timeWash(rawTime):
    timeClean = re.findall(timeFindFine, rawTime[0])
    hour = timeClean[0][:2]
    if(hour[-1:] == ":"):
        hour = hour[:1]
    hour = int(hour)
    minute = int(timeClean[0][-5:-2])
    meridian = timeClean[0][-2:]
    if (meridian == "PM"):
        hour = hour + 12
    timeClean = []
    timeClean.append(hour)
    timeClean.append(minute)
    timeClean.append(meridian)
    return(timeClean)

def daylightTime():
    riseSearch = webPull(googleSearch + "sunrise")
    sunriseTime = (re.findall(timeFindWide, riseSearch))
    sunriseTime = (timeWash(sunriseTime))
    
    setSearch = webPull(googleSearch + "sunset")
    sunsetTime = (re.findall(timeFindWide, setSearch))
    sunsetTime = (timeWash(sunsetTime))

    dayTime = ((sunsetTime[1]-sunriseTime[1])*60)
    dayTime += ((sunsetTime[0]-sunriseTime[0])*3600)
    print(dayTime)

    print(sunriseTime, now, sunsetTime)

daylightTime()