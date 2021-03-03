from praytimes import PrayTimes
from datetime import date
import os

pt = PrayTimes()
dic = {'imsak':0, 'fajr':5, 'sunrise':0, 'dhuhr':0, 'asr':0, 'maghrib':-16, 'isha':4, 'midnight':0}

dt = date(2021, 4, 3)
cords = (40.277310, -74.561890)
pt.tune(dic)

times = pt.getTimes(dt, cords, -5, dst=1)

for k, v in times.items():
    print(f'{k} : {v}')

print("playing..")
# os.system('omxplayer ./azans/fazar/FajrAzan2.mp3')
print("Done!")
