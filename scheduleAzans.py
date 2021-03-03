#!/usr/bin/env python3

from crontab import CronTab

import os

# strAzansPath = '~/AzanPlayer/azans/fazar'
filePath = os.path.abspath('scheduleAzans.py')
print(filePath)

dirPath = os.path.dirname(filePath)
print(dirPath)

fajrAzansDir = dirPath + '/azans/fazar'
fajrAzans = os.listdir(fajrAzansDir)

