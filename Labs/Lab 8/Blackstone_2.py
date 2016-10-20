# imports
import scipy.interpolate as inter
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Constants
M = 100
V = 10
target = 1e-4

# Create arrays to hold potential values.
phi = np.zeros([M+1,M+1],float)
phi[-1,:] = V
phi[:,-1] = V

# Main loop
delta = 1.0
w = 0.5
ncount = 0

while delta>target:
	phiold=np.copy(phi)

	# Calculate new values of the potential.
	for i in range(M+1):
		for j in range(M+1):
			if i == 0 or i == M or j == 0 or j == M:
				phi[i,j] = phi[i,j]
			else:
				phi[i,j] = (1. + w) * (phi[i + 1, j] + phi[i - 1 ,j] + phi[i,j + 1] + phi[i,j - 1])/4 - w*phi[i,j]

	# Calculate maximum difference from old values
	delta = np.max(abs(phi-phiold))
	ncount+=1

# Create an interpolation for the potential at the X midpoint of the cell.
X = np.arange(0,M+1)
Y = phi[:,int(M/2)]
Yinterp = inter.interp1d(X,Y)
Xnew = np.arange(0,M,0.1)

# Plot the interpolation
plt.plot(Xnew,Yinterp(Xnew))
plt.title('Potential at X = 0.5 as a function of Y')
plt.ylabel('potential')
plt.xlabel('Y')
plt.savefig(filename='plot2.png')
plt.show()
