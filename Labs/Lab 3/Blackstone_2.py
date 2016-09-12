# Imports
import numpy as np

# Load data from file
data = np.loadtxt(fname='co2_mm_mlo.txt')

# Create a list of all rows in the data with values for December
december = np.squeeze(np.where(data[:,1] == 12))

# Output the minimum and maximum values for the December data
print('The minimum for December is: ' + str(np.min(data[december,4])))
print('The maximum for December is: ' + str(np.max(data[december,4])))