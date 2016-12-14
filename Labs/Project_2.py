# Imports
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as inter

# # These are the constants and masses in SI units
# M = 1.9884E30
# m = 3.30104E23
# G = 6.674E-11
# c = 3E8

# # Define starting conditions in SI units
# th0 = np.pi
# dt0 = 1.255E-6
# r0 = 47E9
# dr0 = 0

# These are the constants and masses in geometric units
M = 1477
m = 2.451E-4
G = 1
c = 1

# Define starting conditions in geometric units
r0 = 156.8
dr0 = 0
th0 = 0
dt0 = -0.7

# Create a list of times
times = np.linspace(0,500,20000000)

# Store the initial conditions in an array.
p0 = [r0,th0,dr0,dt0]

h = p0[3]*p0[0]**2

# Define a function to find the derivative of each component of r.
def Edr(p,t):

	# initialize an array of zeros.
	v = np.zeros_like(p)

	v[0] = p[2]
	v[1] = p[3]

	v[2] = -1/( m/(h)**2 + 3*m/p[0]**3 - 1/p[0])
	v[3] = 0
	
	return v

def Ndr(p,t):

	v = np.zeros_like(p)

	v[0] = p[2]
	v[1] = p[3]

	# Newtonian equations of motion
	v[2] = -M/p[0]**2
	v[3] = -2*p[3]*p[3]/p[0]
	return v

# Call the ODE solver
Newt = inter.odeint(Ndr,p0,times)
Ein = inter.odeint(Edr,p0,times)

plt.plot(Newt[:,0]*np.cos(Newt[:,1]),Newt[:,0]*np.sin(Newt[:,1]))
plt.plot(0,0,'ro')
plt.title('Newtonian model')
plt.show()

plt.plot(Ein[:,0]*np.cos(Ein[:,1]),Ein[:,0]*np.sin(Ein[:,1]))
plt.plot(0,0,'ro')
plt.title('Schwarzschild metric')
plt.show()