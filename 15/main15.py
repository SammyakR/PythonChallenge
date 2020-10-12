import datetime


for year in range(1016, 1996, 20):
	if datetime.date(year, 1, 26).isoweekday() == 1:
		print(year)


# did random google searches and  MOZART was born on 27 jan 1756
#

