# Imports
import numpy as np
import matplotlib.pyplot as plt

# Load data from file.
data = np.loadtxt(fname='co2_mm_mlo.txt')

# Some months are missing data for the average column.  Those values were entered with -99.99.  This section removes those missing months from the data.
data = data[(data[:,3] > 0)]

# Define variables as copies of the data.
date = np.copy(data[:,2])
average = np.copy(data[:,3])
interp = np.copy(data[:,4])
trend = np.copy(data[:,5])

# Generate a plot of the first 60 data points and save the plot as a jpg file.
plt.plot(date[:60],average[:60])
plt.ylim((300,330))
plt.savefig(filename='plot_1.jpg')
plt.show()

# Calculate the difference between the interpolated and trend values and plot those differences over time.
differences = np.subtract(interp,trend)
plt.plot(date,differences)
plt.savefig(filename='plot_2.jpg')
plt.show()

# Save the date and trend data in a text file
date_trend = np.stack((date,trend),axis=1)
savefile = np.savetxt(fname='data.txt',X=date_trend,fmt='%.3f')