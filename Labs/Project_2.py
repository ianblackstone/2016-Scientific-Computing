# Imports
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as inter

# These are the constants and masses in geometric units
M = 1477
m = 2.451E-4
G = 1
c = 1

# Define starting conditions in geometric units
r0 = 4.7607E10
dr0 = 0
th0 = 0
dt0 = 1.22E-6

# Create a list of times, the orbital period is 8.
times = np.linspace(0,10000,200000)

# Store the initial conditions in an array.
p0 = [r0,th0,dr0,dt0]

h = m*p0[3]*p0[0]**2

# Define a function to find the derivative of each component of r.
def Edr(p,t):

	# initialize an array of zeros.
	v = np.zeros_like(p)

	v[0] = p[2]
	v[1] = p[3]

	v[2] = -M/p[0]**2 + h**2 / p[0]**3 - 3*M*h**2 / p[0]**4
	v[3] = h/p[0]**2
	
	return v

# Call the ODe function
Ein = inter.odeint(Edr,p0,times)

# I was getting errors from the ODEint call when I tried to pass too many points through at once, so I looped over the function call multiple times to complete one orbit.
for k in range(0,20):
	Ein = np.append(Ein,inter.odeint(Edr,Ein[-1],times),axis=0)

# Plot the data and mark the sun's position.
plt.plot(Ein[:,0]*np.cos(Ein[:,1]),Ein[:,0]*np.sin(Ein[:,1]),'b')
plt.plot(0,0,'ro')
plt.title('Schwarzschild metric using ODEint')
plt.xlabel('meters')
plt.ylabel('meters')
plt.axes().set_aspect('equal', 'datalim')
plt.savefig('Schwarz_plot_test.png')
plt.show()