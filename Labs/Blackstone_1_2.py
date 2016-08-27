#imports
import csv
import matplotlib.pyplot as plt

#Define 4 blank lists
year, month, ssn, dev = [] , [] , [] , []

#Open sunspot data
with open('spot_num.txt','r') as sunspots:
	#skip header line
	next(sunspots)
	#store data
	data=csv.reader(sunspots,delimiter=' ',skipinitialspace='true',quotechar='"')
	for row in data:
		year.append(row[0])
		month.append(row[1])
		ssn.append(row[2])
		dev.append(row[3])
sunspots.close()

print(year[3])
print(month[3])
print(ssn[3])
print(dev[3])