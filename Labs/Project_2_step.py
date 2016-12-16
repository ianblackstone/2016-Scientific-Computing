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
dt0 = 4.0833E-15

# Create a list of times, the orbital period is 8.
a = 0
b = 170000
h = 0.1

# Store the initial conditions in an array.
p0 = [r0,th0,dr0,dt0]

#angular momentum
l = p0[3]*p0[0]**2

# This function steps the simulation forward one step.
def step(r,p):
	newr = 2*r[-1] - r[-2] + h**2 * (-M/r[-1]**2 + l**2 / r[-1]**3 - 3*M*l**2 / r[-1]**4)
	newt = p[-1] + 4*h*(l/(newr + r[-1]))
	return newr, newt

# Define a function to find the derivative of each component of r.
def Edr(p):

	# initialize an array of zeros.
	v = np.zeros_like(p)

	v[0] = p[2]
	v[1] = p[3]

	v[2] = -M/p[0]**2 + l**2 / p[0]**3 - 3*M*l**2 / p[0]**4
	v[3] = l/p[0]**2
	
	return v

# Make a single step
p1 = p0 + Edr(p0)*h

# Create two arrays for the radius and angle
rpos = [p0[0], p1[0]]
tpos = [p0[1], p1[1]]

# Calculate b steps of step size h.
for t in range(a,b):
	newr, newt = step(rpos,tpos)
	rpos.append(newr)
	tpos.append(newt)

#This code is used to see if there is any deviation in the orbit, turns out there isn't any.
# minimum = np.amin(rpos)
# maximum = np.amax(rpos)

# print(minimum)
# print(maximum)

# plot the data
plt.plot(np.multiply(rpos,np.cos(tpos)),np.multiply(rpos,np.sin(tpos)),'b')
plt.plot(0,0,'ro')
plt.ylim(ymax=1.5*r0,ymin=-1.5*r0)
plt.xlim(xmax=1.5*r0,xmin=-1.5*r0)
plt.title('Schwarzschild metric')
plt.xlabel('meters')
plt.ylabel('meters')
plt.axes().set_aspect('equal', 'datalim')
plt.savefig('Schwarz_plot_step.png')
plt.show()