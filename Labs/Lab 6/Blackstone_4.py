# This code uses the Euler approximation method.  It is incredibly inaccurate over even a single year, but this can be mitigated by taking more data points.
# Over 100 years to be close to as accurate as the RK2 method we need to take 10 million data points.

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

# Set initial values for x, y, vx, and vy in an array
r = np.array([xi,yi,Vxi,Vyi],float)

# Create an array of time points and declare two empty lists.
tpoints = np.arange(a,b,h)
ypts = []
xpts = []
Epoints = []

# Define a function of r that returns the values of dx, dy, d2x, and d2y
def f(r,t):
	x = r[0]
	y = r[1]
	dx = r[2]
	dy = r[3]
	d2x = g*x/(x**2 + y**2)**(1/2)
	d2y = g*y/(x**2 + y**2)**(1/2)
	return np.array([dx,dy,d2x,d2y],float)

# For each time point track the values of x and y, then evaluate the function at the next point.
for t in tpoints:
	ypts.append(r[0])
	xpts.append(r[1])
	Epoints.append(1/2 * (r[2]**2 + r[3]**2) + g/(r[0]**2 + r[1]**2)**(1/2))
	k1 = h*f(r,t)
	r += k1

# Plot the data
plt.plot(tpoints,Epoints)
plt.xlabel("t (years)")
plt.ylabel('E/M')
plt.title('E/M over time (Euler method)')
plt.savefig(filename='plot4.png')
plt.show()