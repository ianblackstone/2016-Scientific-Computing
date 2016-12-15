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
# dt0 = -1.255E-6
# r0 = 47E9
# dr0 = 0

# These are the constants and masses in geometric units
M = 1477
m = 2.451E-4
G = 1
c = 1

# Define starting conditions in geometric units
r0 = 4.7607E10
dr0 = 0
th0 = 0
dt0 = 4.0833
w0 = 0.177
dw0 = 0
rc = 57.9E9
uc = 1/rc

orbits = 1000

res = orbits*1000

# Create a list of times, the orbital period is 8.
angles = np.linspace(0,orbits*2*np.pi,res)

# Store the initial conditions in an array.
p0 = [w0,dw0]

# h = p0[3]*p0[0]/(r0*np.sqrt(r0-3))

# Define a function to find the derivative of each component of r.
def Edr(p,t):

	# initialize an array of zeros.
	v = np.zeros_like(p)

	v[0] = p[1]
	v[1] = -p[0]*(1-6*M*uc) + 3*M*uc*p[0]**2
	
	return v

Ein = inter.odeint(Edr,p0,angles)

upoints = uc*(1+Ein[:,0])
rpoints = 1/upoints

plt.plot(np.cos(angles[0:res])*rpoints[0:res],np.sin(angles[0:res])*rpoints[0:res])
# plt.plot(np.cos(angles[-res:-1])*rpoints[-res:-1],np.sin(angles[-res:-1])*rpoints[-res:-1])
plt.plot(0,0,'ro')
plt.title('Schwarzschild metric')
plt.xlabel('meters')
plt.ylabel('meters')
plt.axes().set_aspect('equal', 'datalim')
plt.savefig('Schwarz_plot_wobble.png')
plt.show()