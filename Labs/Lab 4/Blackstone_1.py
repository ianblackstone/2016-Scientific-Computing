# Imports
import matplotlib.pyplot as plt
import numpy as np

# define mean lifetime (half life/ln(2)) and step size in years
tau = 75*1.44
h = 1

# Create a list with the initial value in the first cell
N = [1E6]

# Calculate the next value of N using the previous value of N
for t in np.arange(0,999,h):
	N.append(N[t] - h*N[t]/tau)

# Generate a figure with two subplots and save the resulting figure
plt.figure(1)
plt.subplot(211).set_title('Number of atoms over time (linear)')
plt.plot(np.arange(0,1000,h),N)
plt.xlabel('years')
plt.ylabel('Number of atoms')
plt.subplot(212).set_title('Number of atoms over time (log)')
plt.semilogy(np.arange(0,1000,h),N)
plt.xlabel('years')
plt.ylabel('Number of atoms')
plt.tight_layout()
plt.savefig(filename='plot1.png')
plt.show()