# Imports
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Constants
M = 100
V = 10
target = 1e-4

# Create arrays to hold potential values
phi = np.zeros([M+1,M+1],float)
phi[-1,:] = V
phi[:,-1] = V

# Main loop
delta = 1.0
w = 0.5
ncount = 0

while delta>target:
	phiold=np.copy(phi)

	# Calculate new values of the potential
	for i in range(M+1):
		for j in range(M+1):
			if i == 0 or i == M or j == 0 or j == M:
				phi[i,j] = phi[i,j]
			else:
				phi[i,j] = (1. + w) * (phi[i + 1, j] + phi[i - 1 ,j] + phi[i,j + 1] + phi[i,j - 1])/4 - w*phi[i,j]

	# Calculate maximum difference from old values
	delta = np.max(abs(phi-phiold))
	ncount+=1

# Make a plot of the contour lines
cont = plt.contour( phi , 15 , colors='black')
plt.title('Equipotential contours using Laplace\'s method')
plt.gca().invert_yaxis()
plt.clabel(cont, inline=True, fontsize=10)
plt.savefig(filename='plot1.png')
plt.show()