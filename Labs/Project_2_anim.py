# Imports
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as inter
import matplotlib.animation as anim

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
dt0 = 4.0833E-15

# Create a list of times, the orbital period is 8.
times = np.linspace(0,7603000,20000000)

# Store the initial conditions in an array.
p0 = [r0,th0,dr0,dt0]
p = p0

h = p0[3]*p0[0]**2

# Define a function to find the derivative of each component of r.
def Edr(p):

	# initialize an array of zeros.
	v = np.zeros_like(p)

	v[0] = p[2]
	v[1] = p[3]

	v[2] = -M/p[0]**2 + h**2 / p[0]**3 - 3*M*h**2 / p[0]**4
	v[3] = h/p[0]**2
	
	return v

def Ndr(p):

	v = np.zeros_like(p)

	v[0] = p[2]
	v[1] = p[3]

	# Newtonian equations of motion
	v[2] = -M/p[0]**2
	v[3] = -2*p[2]*p[3]/p[0]
	return v

# Call the ODE solver
# Newt = inter.odeint(Ndr,p0,times)

fig, ax = plt.subplots()
plt.ylim(ymin=-2*r0,ymax=2*r0)
plt.xlim(xmin=-2*r0,xmax=2*r0)

mercury, = ax.plot(p[0]*np.cos(p[1]), p[0]*np.sin(p[1]), marker='o')

def rk4(r):
	k1 = h*Edr(r)
	k2 = h*Edr(r + 0.5*k1)
	k3 = h*Edr(r + 0.5*k2)
	k4 = h*Edr(r + k3)
	R = r + (k1 + 2*k2 + 2*k3 + k4)/6
	return R

def animate(i):
	global p
	p = rk4(p)
	x = p[0]*np.cos(p[1])
	y = p[0]*np.sin(p[1])
	mercury.set_data(x, y)
	return mercury, 

anim = anim.FuncAnimation(fig, animate, interval=2000000, blit=True)

plt.show()

# Ein = inter.odeint(Edr,p0,times)

# FEin = np.copy(Ein)

# for k in range(0,500):
# 	Ein = inter.odeint(Edr,Ein[-1],times)

# plt.plot(Newt[:,0]*np.cos(Newt[:,1]),Newt[:,0]*np.sin(Newt[:,1]))
# plt.plot(0,0,'ro')
# plt.title('Newtonian model')
# plt.show()

# plt.plot(Ein[:,0]*np.cos(Ein[:,1]),Ein[:,0]*np.sin(Ein[:,1]),'b')
# plt.plot(FEin[:,0]*np.cos(FEin[:,1]),FEin[:,0]*np.sin(FEin[:,1]),'r')
# plt.plot(0,0,'ro')
# plt.title('Schwarzschild metric')
# plt.show()