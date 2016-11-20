# Imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

# Define constants and parameters.  A few combinations of values cause overflow errors.
g = 9.8
l1 = 3
l2 = 2
m1 = 2
m2 = 1

# Find the maximum length of the pendulum system so the figure window can display the system with adequate spacing.
tl = l1 + l2 + 0.5


# Define starting conditions.
th10 = 1/2 * np.pi
th20 = np.pi/2
w10 = 1
w20 = 0

# Store the initial conditions in an array.
r = [th10,th20,w10,w20]

# Define a function to find the derivative of each component of r.
def dr(r):

	# initialize an array of zeros.
	v = np.zeros_like(r)

	v[0] = r[2]
	v[1] = r[3]

	c = np.cos(r[1] - r[0])
	s = np.sin(r[1] - r[0])

	# The equations of motion for the double pendulum as derived using the Euler Lagrange equation.
	v[2] = (m2 * l1 * r[2]**2 * s * c + m2 * g * np.sin(r[1]) * c + m2 * l2 * r[3]**2 * s - (m1 + m2) * g * np.sin(r[0])) / ((m1 + m2) * l1 - m2 * l1 * c**2)
	v[3] = (-m2 * l2 * r[3]**2 * s * c + (m1 + m2) * g * np.sin(r[0]) * c - (m1 + m2) * l1 * r[2]**2 * s - (m1 + m2) * g * np.sin(r[1])) / ((l2 / l1) * (m1 + m2) * l1 - m2 * l1 * c**2)
	
	return v

# Define a function for the RK4 solver.
def rk4(r):
	k1 = h*dr(r)
	k2 = h*dr(r + 0.5*k1)
	k3 = h*dr(r + 0.5*k2)
	k4 = h*dr(r + k3)
	R = r + (k1 + 2*k2 + 2*k3 + k4)/6
	return R

# This function is needed to initialize the animation.  't' is needed as an output because the init and animate functions need two outputs for use in FuncAnimation, it is not used in this code.
def init():
	line.set_data([],[])
	t.set_text('')
	return line, t

# This is the animation function, it will be called at each interval and the results will be drawn onto the figure.
def animate(i):
	# Call the global variable r so it can be modified inside this function.  An alternate method would be to use 'class' and pass self arguments between functions inside the class.
	global r
	r = rk4(r)

	# Draw lines to each mass.
	xpos = np.cumsum([0,l1*np.sin(r[0]),l2*np.sin(r[1])])
	ypos = np.cumsum([0,-l1*np.cos(r[0]),-l2*np.cos(r[1])])
	line.set_data([xpos],[ypos])
	return line, t

# Draw the blank figure to be animated in and set the axes.
fig = plt.figure()
ax = plt.axes(xlim=(-tl , tl) , ylim=(-tl,tl))

# Define the style of the line to be drawn and set space for data.
line, = ax.plot([], [], 'k-o')

# Initialize 't', this variable is not used here but is needed to avoid errors from the FuncAnimation function.
t = ax.text(0,0,0)

# step size in seconds.  This number is converted to milliseconds for the animation interval.
h = 1/60

# Animate the figure.
anim = anim.FuncAnimation(fig,animate,init_func=init,interval=1000*h,blit=True)

# Display the animation
plt.show()
