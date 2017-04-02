import csv

f = open('MonthwiseAirTemp.csv')

c = csv.reader(f)
for r in c[113]:
	print r[5]