# Imports
import numpy as np
import matplotlib.pyplot as plt

# Declare constants, initial values, theta values (in degrees) to be iterated over, and a list of colors for lines
g = -9.8
V = 100
theta = [15,30,45,60]
colors = ['red','blue','green','black']
xi = 0
yi = 0

# Set range, interval size, and the time values to be calculated at
a = 0.0
b = 20.0
N = 1000
h = (b-a)/N
tpoints = np.arange(a,b,h)

# Iterate over each angle listed in theta
for num in range(0,len(theta)):
	# determine the initial velocity components.
	Vxi = np.cos(np.pi/180 * theta[num])*V
	Vyi = np.sin(np.pi/180 * theta[num])*V

	# Create an array of time points and declare two empty lists.
	ypts = []
	xpts = []

	# Set initial values for x and y
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
	# Plot the data, changing color each loop
	plt.plot(ypts,xpts,color=colors[num],label=str(theta[num]) + ' degrees')

# format the figure and show it
plt.xlabel("x")
plt.ylabel('y')
plt.title('Trajectory')
plt.ylim(ymin=0, ymax=500)
plt.xlim(xmax=1100)
plt.legend(loc='upper right')
plt.savefig(filename='plot2.png')
plt.show()