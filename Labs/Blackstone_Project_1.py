# Imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

# Define constants and parameters.
g = -9.8
l1 = 1
l2 = 1
tl = l1 + l2
m1 = 1
m2 = 2

# Define starting conditions.
th10 = np.pi/2
th20 = -np.pi/4
w10 = 0
w20 = 0

r = [th10,th20,w10,w20]

h = 1/60

def dr(r):

	v = np.zeros_like(r)
	v[0] = r[2]
	v[1] = r[3]

	c = cos(r[1] - r[0])
	s = sin(r[1] - r[0])

	v[2] = (m2 * l1 * r[2] * r[2] * s * c + m2 * g * sin(r[1]) * c + m2 * l2 * r[3] * r[3] * s - (m1 + m2) * g * sin(r[0])) / ((m1 + m2) * l1 - m2 * l1 * c * c)

	v[3] = (-m2 * l2 * r[3] * r[3] * s * c + (m1 + m2) * g * sin(r[0]) * c - (m1 + m2) * l1 * r[2] * r[2] * s - (m1 + m2) * g * sin(r[1])) / ((l2 / l1) * (m1 + m2) * l1 - m2 * l1 * c * c)
	
	return v

def rk4(r,v):
	dr(r)
	k1 = h*dr(v,t)
	k2 = h*dr(v + 0.5*k1 ,t)
	k3 = h*dr(v + 0.5*k2 ,t)
	k4 = h*dr(v + k3 ,t)
	r += (k1 + 2*k2 + 2*k3 + k4)/6
	return r

def init():
	line.set_data([],[])
	return line

def animate(i):
	rk4(r,v)
	line.set_data([0,l1*np.sin(r[0]),l1*np.sin(r[0])+l2*np.sin(r[1])],[0,-l1*np.cos(r[0]),l1*np.cos(r[0])-l1*np.cos(r[1])])
	return line

# Draw the blank figure to be animated in.
fig = plt.figure()
ax = plt.axes(xlim=(-tl , tl) , ylim=(-tl,tl))

anim = anim.FuncAnimation(fig,animate,init_func=init,frames=100,interval=20,blit=True)

plt.show()

# class DoublePendulum:
# 	"""Double Pendulum Class

# 	init_state is [theta1, omega1, theta2, omega2] in degrees,
# 	where theta1, omega1 is the angular position and velocity of the first
# 	pendulum arm, and theta2, omega2 is that of the second pendulum arm
# 	"""
# 	def __init__(self,
# 				 init_state = [120, 0, -20, 0],
# 				 # l1=1.0,  # length of pendulum 1 in m
# 				 # l2=1.0,  # length of pendulum 2 in m
# 				 # m1=1.0,  # mass of pendulum 1 in kg
# 				 # m2=1.0,  # mass of pendulum 2 in kg
# 				 # g=9.8,  # acceleration due to gravity, in m/s^2
# 				 origin=(0, 0)): 
# 		self.init_state = np.asarray(init_state, dtype='float')
# 		self.params = (l1, l2, m1, m2, g)
# 		self.origin = origin
# 		self.time_elapsed = 0

# 		self.state = [th10, th20, w10, w20]
	
# 	def position(self):
# 		"""compute the current x,y positions of the pendulum arms"""
# 		(l1, l2, m1, m2, g) = self.params

# 		x = np.cumsum([self.origin[0],
# 					   l1 * sin(self.state[0]),
# 					   l2 * sin(self.state[2])])
# 		y = np.cumsum([self.origin[1],
# 					   -l1 * cos(self.state[0]),
# 					   -l2 * cos(self.state[2])])
# 		return (x, y)

# # Changed variables
# 	def dr(self, r, t):
# 		"""compute the derivative of the given r"""
# 		(m1, m2, l1, l2, g) = self.params

# 		v = np.zeros_like(r)
# 		v[0] = r[2]
# 		v[1] = r[3]

# 		c = cos(r[1] - r[0])
# 		s = sin(r[1] - r[0])

# 		v[2] = (m2 * l1 * r[2] * r[2] * s * c + m2 * g * sin(r[1]) * c + m2 * l2 * r[3] * r[3] * s - (m1 + m2) * g * sin(r[0])) / ((m1 + m2) * l1 - m2 * l1 * c * c)

# 		v[3] = (-m2 * l2 * r[3] * r[3] * s * c + (m1 + m2) * g * sin(r[0]) * c - (m1 + m2) * l1 * r[2] * r[2] * s - (m1 + m2) * g * sin(r[1])) / ((l2 / l1) * (m1 + m2) * l1 - m2 * l1 * c * c)
		
# 		return v

# 	def step(self, dt):
# 		"""execute one time step of length dt and update state"""
# 		self.state = integrate.odeint(self.dstate_dt, self.state, [0, dt])[1]
# 		self.time_elapsed += dt
# #------------------------------------------------------------
# # set up initial state and global variables
# pendulum = DoublePendulum([180., 0.0, -20., 0.0])
# dt = 1./30 # 30 fps

# #------------------------------------------------------------
# # set up figure and animation
# fig = plt.figure()
# ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
# ax.grid()

# line, = ax.plot([], [], 'o-', lw=2)

# def init():
# 	"""initialize animation"""
# 	line.set_data([], [])
# 	time_text.set_text('')
# 	energy_text.set_text('')
# 	return line, time_text, energy_text

# def animate(i):
# 	"""perform animation step"""
# 	global pendulum, dt
# 	pendulum.step(dt)
# 	line.set_data(*pendulum.position())
# 	return line

# # choose the interval based on dt and the time to animate one step
# from time import time
# t0 = time()
# animate(0)
# t1 = time()
# interval = 1000 * dt - (t1 - t0)

# ani = animation.FuncAnimation(fig, animate, frames=300,
# 							  interval=interval, blit=True, init_func=init)

# plt.show()