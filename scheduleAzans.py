#!/usr/bin/python3

from crontab import CronTab
from random import randint
from praytimes import PrayTimes
from datetime import date

import os
import time

# strAzansPath = '~/AzanPlayer/azans/fazar'
filePath = os.path.abspath(__file__)
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
# system_cron.remove_all(comment='daily_run')

def schedule(time, cmd, cmt):
	job = system_cron.new(command=cmd, comment=cmt)
	t = time.split(":")
	hr = t[0]
	min = t[1]
	job.minute.on(int(min))
	job.hour.on(int(hr))
	job.set_comment("pi-cronJobs")


def getPrev15(time):

	t = time.split(":")
	hr = int(t[0])
	minute = int(t[1])
	minute -= 15
	if minute < 0:
		hr -= 1
		minute = 60 + minute
		print(minute)
		if hr < 0:
			hr = 24
	return str(hr) + ":" + str(minute)

# def dailyUpdate(cmd, cmt):
#	job = system_cron.new(command=cmd, comment=cmt)
#	job.minute.on(int(15))
#	job.hour.on(int(9))
#	job.set_comment("daily_run")


# dailyUpdate(f'python3 {filePath} >> {dirPath}/logs.txt', "daily time update")


fjr15 = getPrev15(times['fajr'])
schedule(fjr15, "omxplayer /home/pi/AzanPlayer/customTextSpeech/engMsg.mp3; omxplayer /home/pi/AzanPlayer/customTextSpeech/urduTest.mp3", "15 min before fajr")

schedule(times['fajr'], f'omxplayer {fajr}', 'fajr time schedule')


sunrise15 = getPrev15(times['sunrise'])
schedule(sunrise15, "omxplayer /home/pi/AzanPlayer/customTextSpeech/engFajrMsg.mp3; omxplayer /home/pi/AzanPlayer/customTextSpeech/urduFajrMsg.mp3", "15 before sunrise")

schedule(times['dhuhr'], f'omxplayer {dhuhr}', 'dhuhr time schedule')


asr15 = getPrev15(times['asr'])
schedule(asr15, "omxplayer /home/pi/AzanPlayer/customTextSpeech/engMsg.mp3; omxplayer /home/pi/AzanPlayer/customTextSpeech/urduTest.mp3", "15 min before asr")

schedule(times['asr'], f'omxplayer {asr}', 'asr time schedule')



maghrib15 = getPrev15(times['maghrib'])
schedule(maghrib15, "omxplayer /home/pi/AzanPlayer/customTextSpeech/engMsg.mp3; omxplayer /home/pi/AzanPlayer/customTextSpeech/urduTest.mp3", "15 min before maghrib")


schedule(times['maghrib'], f'omxplayer {maghrib}', 'maghrib time schedule')


isha15 = getPrev15(times['isha'])
schedule(isha15, "omxplayer /home/pi/AzanPlayer/customTextSpeech/engMsg.mp3; omxplayer /home/pi/AzanPlayer/customTextSpeech/urduTest.mp3", "15 min before isha")

schedule(times['isha'], f'omxplayer {isha}', 'isha time schedule')

system_cron.write()

print(f"Scheduled done for {dt.month}/{dt.day}/{dt.year} \n{times}")

for jobs in system_cron:
	print(jobs)

print()
