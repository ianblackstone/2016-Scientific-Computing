# imports
import numpy as np
import matplotlib.pyplot as plt

# Read data from file
data = np.loadtxt(fname='co2_mm_mlo.txt')

# Initialize two variables
slopedata = []
slope = 0

# find the number of rows in the data, skipping the last row
numrows = len(data) - 1

# Calculate the slope of all data points except the first and last
for row in range (1,numrows):
	slope = (data[row +1,5] - data[row-1,5])/2
	slopedata.append([data[row,2],slope])

# Convert the slopedata to a numpy array for easier plotting
slopedata = np.array(slopedata)

# Create a figure with two plots in it and save the plot as a .png file
plt.figure(1)
plt.subplot(211).set_title('trend data')
plt.plot(data[1:-2,2],data[1:-2,5])
plt.ylabel('CO2 concentration (ppm)')
plt.subplot(212).set_title('derivative')
plt.plot(slopedata[:,0],slopedata[:,1])
plt.ylabel('Slope')
plt.xlabel('Date')
plt.savefig(filename='plot1.png')
plt.show()