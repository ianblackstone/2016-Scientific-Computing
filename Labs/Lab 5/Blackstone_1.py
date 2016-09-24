# Imports
import numpy as np
import matplotlib.pyplot as plt

# Declare constants and initial conditions
g = -9.8
V = 100
theta = 45
Vxi = np.cos(np.pi/180 * theta)*V
Vyi = np.sin(np.pi/180 * theta)*V
xi = 0
yi = 0

# Set initial values for x, y, vx, and vy in an array
r = np.array([xi,yi,Vxi,Vyi],float)

# Define a function of r that returns the values of dx, dy, d2x, and d2y
def f(r,t):
	x = r[0]
	y = r[1]
	dx = r[2]
	dy = r[3]
	d2x = 0
	d2y = g
	return np.array([dx,dy,d2x,d2y],float)

# Set range and interval size
a = 0.0
b = 18.0
N = 1000
h = (b-a)/N

# Create an array of time points and declare two empty lists.
tpoints = np.arange(a,b,h)
ypts = []
xpts = []

# For each time point track the values of x and y, then evaluate the function at the next points
# and set out current value of y and x equal to the weighted average of our four calculated points in each bin
for t in tpoints:
	ypts.append(r[0])
	xpts.append(r[1])
	k1 = h*f(r,t)
	k2 = h*f(r+0.5*k1,t)
	k3 = h*f(r + 0.5*k2,t)
	k4 = h*f(r+k3,t)
	r += (k1 + 2*k2 + 2*k3 + k4)/6

# Plot the data
plt.plot(ypts,xpts)
plt.xlabel("x")
plt.ylabel('y')
plt.title('Trajectory')
plt.ylim(ymin=0)
plt.xlim(xmax=1100)
plt.savefig(filename='plot1.png')
plt.show()