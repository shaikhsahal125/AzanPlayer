#!/usr/bin/env python3

from math import sin, cos
from math import atan2 as arctan2
from math import asin as arcsin

import pandas as pd
import datetime


class PrayerTimeCalculations:

	def __init__(self, latitude, longitude):
		self.latitude = latitude
		self.longitude = longitude

		dateAndTime = pd.datetime.now()
		self.year = dateAndTime.year
		self.month = dateAndTime.month
		self.day = dateAndTime.day


	def get_julian_date(self):
		date = pd.Timestamp(year=self.year, month=self.month, day=self.day)
		return date.to_julian_date()

	def get_julian(self):
		a = (14 - self.month) // 12
		y = self.year + 4800 - a
		m = self.month + 12*a - 3
		jd = self.day + (153*m + 2)/5 + 365*y + y/4 - y/100 + y/400 - 32045
		return int(jd)


	def get_declination_and_EqT(self, julian_date):
		d = julian_date - 2451545.0

		g = 357.529 + 0.98560028 * d
		q = 280.459 + 0.98564736 * d
		L = q + 1.915 * sin(g) + 0.020 * sin(2 * g)

		R = 1.00014 - 0.01671 * cos(g) - 0.00014 * cos(2 * g)
		e = 23.439 - 0.00000036 * d
		RA = arctan2(cos(e) * sin(L), cos(L)) / 15

		D = arcsin(sin(e) * sin(L))  # declination of the Sun
		EqT = (q/15) - RA # Equation of time

		return (D, EqT)





if __name__ == "__main__":
	pt = PrayerTimeCalculations(40.277310, -74.561890)
	jd = pt.get_julian_date()
	print(jd)

	jd2 = pt.get_julian()
	print(jd2)
	# dAndEqT = pt.get_declination_and_EqT(jd)
	# print(dAndEqT)
	#
	# dhuhar = 12 + (-5) - (((-74.561890)/15) - (dAndEqT[1]))
	# print(f'Dhuhar time is: {dhuhar}')
	#
	# lol = None
	# print(f'Actual time: {lol}')
