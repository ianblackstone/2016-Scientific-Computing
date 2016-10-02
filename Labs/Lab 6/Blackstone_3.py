# Imports
import numpy as np
import matplotlib.pyplot as plt

# Declare constants and initial conditions
g = -4*np.pi**2
V = 2*np.pi
xi = 1
yi = 0
Vxi = V*yi/(xi**2 + yi**2)**(1/2)
Vyi = V*xi/(xi**2 + yi**2)**(1/2)

# Set range and interval size
a = 0.0
b = 100.0
h = 0.01

# Create an array of time points and declare three empty lists.
tpoints = np.arange(a,b,h)
ypts = []
xpts = []
Epoints = []

# Set initial values for x, y, vx, and vy in an array
r = np.array([xi,yi,Vxi,Vyi],float)

# Define a function of r that returns the values of dx, dy, d2x, and d2y
def f(r,t):
	x = r[0]
	y = r[1]
	dx = r[2]
	dy = r[3]
	d2x = g*x/(x**2 + y**2)**(1/2)
	d2y = g*y/(x**2 + y**2)**(1/2)
	return np.array([dx,dy,d2x,d2y],float)

# For each time point track the values of x, y, and energy.
# Then calculate the next point and recalculate using the midpoint between the initial point and the next point.
for t in tpoints:
	ypts.append(r[0])
	xpts.append(r[1])
	Epoints.append(1/2 * (r[2]**2 + r[3]**2) + g/(r[0]**2 + r[1]**2)**(1/2))
	k1 = h*f(r,t)
	k2 = h*f(r+0.5*k1,t)
	r += k2

# Plot the data
plt.plot(tpoints,Epoints)
plt.xlabel("t (years)")
plt.ylabel('E/M')
plt.title('E/M over time (RK2 method)')
plt.ylim(ymin=-20,ymax=-18)
plt.savefig(filename='plot3.png')
plt.show()