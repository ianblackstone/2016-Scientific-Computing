# Imports
import numpy as np
import matplotlib.pyplot as plt

# Define a function of r that returns the values of omega and domega
def f(r):
	theta = r[0]
	omega = r[1]
	dtheta = omega
	domega = -10*np.sin(theta)
	return np.array([dtheta,domega],float)

# Set range, interval size, and initial conditions
a = 0.0
b = 10.0
N = 1000
h = (b-a)/N
x = 0.0

# Create an array of time points and declare two empty lists.
tpoints = np.arange(a,b,h)
omegapts = []
thetapts = []

# Set initial values for theta and omega
r = np.array([1.0,1.0],float)

# For each time point track the values of theta and omega, then evaluate the function at the next points
# and set out current value of omega and theta equal to the output of our function at the midpoint of each bin
for t in tpoints:
	omegapts.append(r[0])
	thetapts.append(r[1])
	k1 = h*f(r)
	k2 = h*f(r+0.5*k1)
	r += k2

# Plot the data over time.
plt.plot(tpoints,omegapts,label='omega')
plt.plot(tpoints,thetapts,label='theta')
plt.xlabel("t")
plt.legend(loc='upper right')
plt.savefig(filename='plot2.png')
plt.show()