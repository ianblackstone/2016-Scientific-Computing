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
M = 1
m = 2.451E-4
G = 1
c = 1

# Define starting conditions in geometric units
r0 = 50
dr0 = 0
th0 = 0
dt0 = 10/(r0*np.sqrt(r0-3))
# dt0 = 4E-15

# Create a list of times, the orbital period is 8.
times = np.linspace(0,1000,20000000)

# Store the initial conditions in an array.
p0 = [r0,th0,dr0,dt0]

h = p0[3]*p0[0]/(r0*np.sqrt(r0-3))

# Define a function to find the derivative of each component of r.
def Edr(p,t):

	# initialize an array of zeros.
	v = np.zeros_like(p)

	v[0] = p[2]
	v[1] = p[3]

	v[2] = -1/p[0]**2 + h**2 / p[0]**3 - 3*h**2 / p[0]**4
	v[3] = h/p[0]**2
	
	return v

# def Ndr(p,t):

# 	v = np.zeros_like(p)

# 	v[0] = p[2]
# 	v[1] = p[3]

# 	# Newtonian equations of motion
# 	v[2] = -M/p[0]**2 + h**2 /(m**2 * p[0]**3)
# 	v[3] = -2*h/(m*p[0])
# 	return v

# Call the ODE solver
# Newt = inter.odeint(Ndr,p0,times)
# Ein = inter.odeint(Edr,p0,times)
Ein = inter.ode(Edr)

# for k in range(0,28):
# 	Ein = np.append(Ein,inter.odeint(Edr,Ein[-1],times),axis=0)


# plt.plot(Newt[:,0]*np.cos(Newt[:,1]),Newt[:,0]*np.sin(Newt[:,1]))
# plt.plot(0,0,'ro')
# plt.title('Newtonian model')
# plt.xlabel('meters')
# plt.ylabel('meters')
# plt.axes().set_aspect('equal', 'datalim')
# plt.savefig('Newt_plot_test.png')
# plt.show()

plt.plot(Ein[:,0]*np.cos(Ein[:,1]),Ein[:,0]*np.sin(Ein[:,1]),'b')
plt.plot(0,0,'ro')
plt.title('Schwarzschild metric')
plt.xlabel('meters')
plt.ylabel('meters')
plt.axes().set_aspect('equal', 'datalim')
plt.savefig('Schwarz_plot_test.png')
plt.show()