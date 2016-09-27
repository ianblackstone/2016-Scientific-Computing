# Imports
import numpy as np
import matplotlib.pyplot as plt

# Define a function of r that returns the values of y and dy
def f(r,t):
	x = r[0]
	y = r[1]
	dx = r[2]
	dy = r[3]
	d2x = 0
	d2y = g
	return np.array([dx,dy,d2x,d2y],float)

# Declare constants
g = -9.8
V = 100
theta = [15,30,45,60]
colors = ['red','blue','green','black']
xi = 0
yi = 0

# Set range, interval size, and initial conditions
a = 0.0
b = 20.0
N = 1000
h = (b-a)/N
tpoints = np.arange(a,b,h)

for num in range(0,len(theta)):
	Vxi = np.cos(np.pi/180 * theta[num])*V
	Vyi = np.sin(np.pi/180 * theta[num])*V

	# Create an array of time points and declare two empty lists.
	ypts = []
	xpts = []

	# Set initial values for x and y
	r = np.array([xi,yi,Vxi,Vyi],float)

	# For each time point track the values of x and y, then evaluate the function at the next points
	# and set out current value of y and x equal to the output of our function at the midpoint of each bin
	for t in tpoints:
		ypts.append(r[0])
		xpts.append(r[1])
		k1 = h*f(r,t)
		k2 = h*f(r+0.5*k1,t)
		r += k2
	# Plot the data
	plt.plot(ypts,xpts,color=colors[num])

plt.xlabel("x")
plt.ylabel('y')
plt.title('Trajectory')
plt.ylim(ymin=0)
plt.show()