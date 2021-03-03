#!/usr/bin/env python3

from crontab import CronTab
from random import randint
from praytimes import PrayTimes
from datetime import date

import os
import time

# strAzansPath = '~/AzanPlayer/azans/fazar'
filePath = os.path.abspath('scheduleAzans.py')
dirPath = os.path.dirname(filePath)

fajrAzansDir = dirPath + '/azans/fazar'
fajrAzans = os.listdir(fajrAzansDir)

otherAzansDir = dirPath + '/azans/others'
otherAzans = os.listdir(otherAzansDir)

fjrRand = randint(0, len(fajrAzans)-1)
fajr = fajrAzansDir + '/' + fajrAzans[fjrRand]


# otherRand = randint(0, len(otherAzans)-1)
dhuhr = otherAzansDir + '/' + otherAzans[randint(0, len(otherAzans)-1)]
asr = otherAzansDir + '/' + otherAzans[randint(0, len(otherAzans)-1)]
maghrib = otherAzansDir + '/' + otherAzans[randint(0, len(otherAzans)-1)]
isha = otherAzansDir + '/' + otherAzans[randint(0, len(otherAzans)-1)]


pt = PrayTimes()
dsT = time.localtime().tm_isdst

dic = {'imsak':0, 'fajr':5, 'sunrise':0, 'dhuhr':0, 'asr':0, 'maghrib':-16, 'isha':4, 'midnight':0}

dt = date.today()
cords = (40.277310, -74.561890)
pt.tune(dic)

times = pt.getTimes(dt, cords, -5, dst=dsT)


system_cron = CronTab(user='pi')

system_cron.remove_all(comment='pi-cronJobs')

def schedule(time, cmd, cmt):
	job = system_cron.new(command=cmd, comment=cmt)
	t = time.split(":")
	hr = t[0]
	min = t[1]
	job.minute.on(int(min))
	job.hour.on(int(hr))
	job.set_comment("pi-cronJobs")




schedule(times['fajr'], f'omxplayer {fajr}', 'fajr time schedule')
schedule(times['dhuhr'], f'omxplayer {dhuhr}', 'dhuhr time schedule')
schedule(times['asr'], f'omxplayer {asr}', 'asr time schedule')
schedule(times['maghrib'], f'omxplayer {maghrib}', 'maghrib time schedule')
schedule(times['isha'], f'omxplayer {isha}', 'isha time schedule')

system_cron.write()

print(f"Scheduled done for {dt.month}/{dt.day}/{dt.year} \n{times}!")

