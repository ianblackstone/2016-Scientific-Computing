# Imports
import numpy as np
import matplotlib.pyplot as plt

# Declare constants and initial conditions.  Units are in AU and years, so initial velocity is 2pi AU per year (or one orbit per year).
g = -4*np.pi**2
V1 = 2*np.pi
x1i = 1
y1i = 0
Vx1i = V1*y1i/(x1i**2 + y1i**2)**(1/2)
Vy1i = V1*x1i/(x1i**2 + y1i**2)**(1/2)
m1 = 100

V2 = 6*np.pi
x2i = 3
y2i = 0
Vx2i = V2*y2i/(x2i**2 + y2i**2)**(1/2)
Vy2i = V2*x2i/(x2i**2 + y2i**2)**(1/2)
m2 = 200

V3 = 0
x3i = 0
y3i = 0
Vx3i = V3*y3i/(x3i**2 + y3i**2)**(1/2)
Vy3i = V3*x3i/(x3i**2 + y3i**2)**(1/2)
m3 = 1000

# Set range and interval size
a = 0.0
b = 10.0
h = 0.01

# Create an array of time points and declare two empty lists.
tpoints = np.arange(a,b,h)
y1pts = []
x1pts = []
y2pts = []
x2pts = []
y3pts = []
x3pts = []

# Set initial values for x, y, vx, and vy in an array
r = np.array([x1i,x2i,x3i,y1i,y2i,y3i,Vx1i,Vx2i,Vx3i,Vy1i,Vy2i,Vy3i],float)

def g(x1,x2,y1,y2,m1,m2):
	acc = g*m2*(x1-x2)/((x1-x2)**2 + (y1-y2)**2)**(3/2)
	return acc

# Define a function of r that returns the next values of dx, dy, d2x, and d2y
def f(r,m,t):
	x1 = r[0]
	x2 = r[1]
	x3 = r[2]
	y1 = r[3]
	y2 = r[4]
	y3 = r[5]
	dx1 = r[6]
	dx2 = r[7]
	dx3 = r[8]
	dy1 = r[9]
	dy2 = r[10]
	dy3 = r[11]
	d21x = 
	d21y = g*y/(x**2 + y**2)**(1/2)
	return np.array([dx,dy,d2x,d2y],float)

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
plt.title('Earth\'s Orbit')
plt.ylim(ymin=-1.5,ymax=1.5)
plt.xlim(xmin=-1.5,xmax=1.5)
plt.savefig(filename='plot1.png')
plt.show()