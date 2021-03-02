#!/usr/bin/env python3

import pandas as pd


class PrayerTimeCalculations:

	def __init__(self):
		dateAndTime = pd.datetime.now()
		self.year = dateAndTime.year
		self.month = dateAndTime.month
		self.day = dateAndTime.day
		print(dateAndTime)

	def get_julian_date(self):
		date = pd.Timestamp(year=self.year, month=self.month, day=self.day)
		return date.to_julian_date()


	def get_declination_and_EqT(self, julian_date):
		pass


if __name__ == "__main__":
	pt = PrayerTimeCalculations()
	print(pt.get_julian_date())


