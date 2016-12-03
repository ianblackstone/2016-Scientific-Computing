# Monte Carlo simulation for Argon atoms under the Lenard-Jones potential.
# Lennard-Jones: V(r) = 4E(sigma/r**12 - sigma/r**6)
# reduced distance unit is sigma = 1 where for argon sigma = 2.4 angstrom
# reduced energy unit is E = 1 where for argon e = eV
# Resulting potential is V(r) = 4(1/r**12-1/r**6)
# and force magnitude is F(r) = 24(2/r**13-1/r**7)

import numpy as np
from matplotlib import pyplot as plt

def sign(a, b):    # utility function to select proper sign for flipping distance
	if (b >=  0.0):
		return abs(a)
	else:
		return  - abs(a)

# Define the number of atoms so it is a perfect square, simplifies setup
Natoms = 16
sqrtNatoms = int(np.sqrt(Natoms))
Nsteps =  40
Kinit = 2.0    # initial average kinetic energy of each particle
v0 = np.sqrt(2.*Kinit)    # initial average speed of each particle, m = 1
dt = 0.02

# Now define all the variable arrays.  For now, do not keep track of forces.
x  = np.zeros( (Natoms,Nsteps),    float)                       #  x position of atoms
y  = np.zeros( (Natoms,Nsteps),    float)                       #  y position
vx = np.zeros( (Natoms,Nsteps),    float)               #  x vel. x of atoms
vy = np.zeros( (Natoms,Nsteps),    float)                #  y component velocity atoms
# fx = np.zeros( (Natoms,Nsteps, 2), float)                      #  x component of force
# fy = np.zeros( (Natoms,Nsteps, 2), float)                      #  y component of force

# setup the initial grid of particles, placing them in a squarish configuration
sigspace = 5.0 # average spacing between particles in sigma units
L = sigspace*sqrtNatoms                    #  side of square  
halfsig = sigspace/2.    # used for offset from x/y = 0 and x/y = L

# for now put each particle equally spaced in the region modified by a small amount
xvals = np.linspace(halfsig,L-halfsig,sqrtNatoms)
yvals = np.linspace(halfsig,L-halfsig,sqrtNatoms)
# startpos = [[xs,ys] for xs in xvals for ys in yvals] alternative position set

for ix in range(0, sqrtNatoms):                   #  x->   0  1  2  3  4
	for iy in range(0, sqrtNatoms):               #  y = 0   0  5  10 15 20 
		 x[sqrtNatoms*ix+iy,0] = xvals[ix] + np.random.rand()-0.5
		 y[sqrtNatoms*ix+iy,0] = yvals[iy] + np.random.rand()-0.5
		 # vx[sqrtNatoms*ix+iy,0] = twelveran()*sqrtKinit
		 # vy[iy+sqrtNatoms*ix,0] = twelveran()*sqrtKinit
		 angle = np.random.rand()*2.*np.pi               # to randomize v direction
		 vx[sqrtNatoms*ix+iy,0] = v0*np.cos(angle)
		 vy[sqrtNatoms*ix+iy,0] = v0*np.sin(angle)

# do the first step with Euler  new pos = old pos + old vel*time step
# for now, this is the only use of the speed array which is not now updated
for n1 in range(0, Natoms):
	x[n1,1] = x[n1,0] + vx[n1,0]*dt
	y[n1,1] = y[n1,0] + vy[n1,0]*dt
	vx[n1,1] = vx[n1,0]
	vy[n1,1] = vy[n1,0]

# now do all other steps with Verlet starting with third position
for ns in range(2, Nsteps):

	# this for loop checks for particles that have left the box, and re-introduces them 
	# on the other side.  It also adjust the previous position to make Verlet
	# calculation consistent.  As a result, some particle positions will be
	# slightly outside the box, but they will be traveling back into it
	for k in range(0,Natoms):
		if x[k,ns-1] > L:
			x[k,ns-1] = x[k,ns-1] - L
			x[k,ns-2] = x[k,ns-2] - L
		elif x[k,ns-1] < 0:
			x[k,ns-1] = x[k,ns-1] + L
			x[k,ns-2] = x[k,ns-2] + L
		if y[k,ns-1] > L:
			y[k,ns-1] = y[k,ns-1] - L
			y[k,ns-2] = y[k,ns-2] - L
		elif y[k,ns-1] < 0:
			y[k,ns-1] = y[k,ns-1] + L
			y[k,ns-2] = y[k,ns-2] + L
	
	# Now loop over all atoms . . . . 
	for n in range(0, Natoms):
		accx = 0
		accy = 0
		# . . . . and for each atom, find the current force/acceleration from all other atoms
		for m in range(0, Natoms): 
			if m == n:
			   continue
# calculate the minimum x distance
			dx = x[n,ns-1]-x[m,ns-1]
			dy = y[n,ns-1]-y[m,ns-1]
			if np.abs(dx) > L/2.:
				# dx = dx-L/2.
				dx = dx  -  sign(L, dx)    #  interact with closer image
# now get the minimum y distance
			if np.abs(dy) > L/2.:
				dy = dy  -  sign(L, dy)
		  
			rmn = np.sqrt(dx*dx+dy*dy)
			if rmn > 6.0:
				continue      # if the particle is beyond some max dist, ignore
			elif rmn < 0.0001:
				rmn = 0.0001  # limit the approach of particles, including the rmn = 0 case
			fmn = 24.*(2./rmn**13 - 1./rmn**7)  # force on n from m
			thetamn = np.arctan2(dy,dx)
			accx += fmn*np.cos(thetamn)   # accelerations, remember m = 1 otherwise divide f by m
			accy += fmn*np.sin(thetamn)

		# Verlet formula, new position depends on previous two and acceleration term
		x[n,ns] = 2.*x[n,ns-1] - x[n,ns-2] + accx*dt**2
		y[n,ns] = 2.*y[n,ns-1] - y[n,ns-2] + accy*dt**2

		# could calculate speed later, but go ahead and use central difference formula
		vx[n,ns-1] = (x[n,ns] - x[n,ns-2])/(2.*dt)
		vy[n,ns-1] = (y[n,ns] - y[n,ns-2])/(2.*dt)

# Plot the initial positions
plt.scatter(x[:,0],y[:,0])
plt.title('Initial atom positions')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Plot the final positions
plt.scatter(x[:,-1],y[:,-1])
plt.title('Final atom positions')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# particle velocity
vel = np.square(vx) + np.square(vy)

plt.hist(vel[:,-3],32)
plt.show()

# Create an array of velocities
velmap = np.zeros((int(L),int(L)))

for p in range(Natoms):
	velmap[int(x[p,-3]),int(y[p,-3])] = vel[p,-3]

plt.imshow(velmap,cmap = plt.cm.hot_r)
plt.title('Heat map of particle velocities')
plt.show()

KEnergy = 0.5*vel
PEnergy = 
Elist = np.zeros(Nsteps-2)

for step in range(Nsteps-2):
	Elist[step] = sum(KEnergy[:,step])

plt.plot(range(Nsteps-2),Elist)
plt.ylim(ymax=40,ymin=0)
plt.show()