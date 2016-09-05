# Imports.
import csv
import matplotlib.dates
import matplotlib.pyplot as plt
import datetime

# Define 4 blank lists for date, sunspot number, and dev.
date, ssn, dev, date_time = [] , [] , [] , []

# Open sunspot data.
with open('spot_num.txt','r') as sunspots:
	# Skip header line.
	next(sunspots)
	# Read data from open file.
	data=csv.reader(sunspots,delimiter=' ',skipinitialspace='true',quotechar='"')
	for row in data:
		# Collect data from each column into a variable.
		date.append(row[0] + '-' + row[1])
		ssn.append(float(row[2]))
		dev.append(float(row[3]))
sunspots.close()

# Converting the year and month data into a datetime object for matplotlib to use.
for item in date:
	date_time.append(datetime.datetime.strptime(item, '%Y-%m'))

# Create a plot of the data.
plt.plot_date(date_time,ssn,'ro')
plt.xlabel('Date')
plt.ylabel('Sunspot Number')
plt.title('Sunspots by date since 1749')
plt.show()