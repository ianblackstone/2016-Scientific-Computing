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
Natoms = 64
sqrtNatoms = int(np.sqrt(Natoms))
Nsteps =  400
Kinit = 2.0    # initial average kinetic energy of each particle
v0 = np.sqrt(2.*Kinit)    # initial average speed of each particle, m = 1
dt = 0.02

# Create an array to store the potential energy at each step.
PEnergy = np.zeros(Nsteps)

# Create an array to track the number of times we intervene by not allowing particles to get too close.
rounded = np.zeros(Nsteps)

mindist = 100
avdist = 0

# Now define all the variable arrays.  For now, do not keep track of forces.
x  = np.zeros( (Natoms,Nsteps),    float)               #  x position of atoms
y  = np.zeros( (Natoms,Nsteps),    float)               #  y position
vx = np.zeros( (Natoms,Nsteps),    float)               #  x vel. x of atoms
vy = np.zeros( (Natoms,Nsteps),    float)               #  y component velocity atoms

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

	accx = np.zeros((Natoms,Natoms), float)
	accy = np.zeros((Natoms,Natoms), float)

	# Now loop over all atoms to fill in the lower triangular portion of  the acceleration arrays
	for n in range(0, Natoms):
		for m in range(n+1, Natoms):

			# calculate the minimum x distance
			dx = x[n,ns-1]-x[m,ns-1]
			dy = y[n,ns-1]-y[m,ns-1]

			if np.abs(dx) > L/2.:
				dx = dx  -  sign(L, dx)    #  interact with closer image

			# now get the minimum y distance
			if np.abs(dy) > L/2.:
				dy = dy  -  sign(L, dy)

			rmn = np.sqrt(dx*dx+dy*dy)

			if rmn < mindist:
				mindist = rmn

			PEnergy[ns] += -4.*(1./rmn**12 - 1./rmn**6)

			if rmn > 6.0:
				continue      # if the particle is beyond some max dist, ignore

			elif rmn < 0.001:
				rmn = 0.001  # limit the approach of particles, including the rmn = 0 case
				rounded[ns] += 1

			if ns == Nsteps-1:
				avdist += rmn

			fmn = 24.*(2./rmn**13 - 1./rmn**7)  # force on n from m
			
			thetamn = np.arctan2(dy,dx)
			accx[m,n] = fmn*np.cos(thetamn)   # accelerations, remember m = 1 otherwise divide f by m
			accy[m,n] = fmn*np.sin(thetamn)

	# Since each array is 0 everywhere but in the lower triangle we can just subtract the transpose to copy the opposite force into the upper triangle.
	accx = accx - np.transpose(accx)
	accy = accy - np.transpose(accy)

	for n in range(0,Natoms):
		# Verlet formula, new position depends on previous two and acceleration term
		x[n,ns] = 2.*x[n,ns-1] - x[n,ns-2] + np.sum(accx[:,n])*dt**2
		y[n,ns] = 2.*y[n,ns-1] - y[n,ns-2] + np.sum(accy[:,n])*dt**2

		# could calculate speed later, but go ahead and use central difference formula
		vx[n,ns-1] = (x[n,ns] - x[n,ns-2])/(2.*dt)
		vy[n,ns-1] = (y[n,ns] - y[n,ns-2])/(2.*dt)

# This is to check how close particles are getting, turns out not very.
print('The closest two particles got was ' + str(mindist))

# Plot the initial positions
plt.scatter(x[:,0],y[:,0])
plt.title('Initial atom positions')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig(filename='Plot1.png')
plt.show()

# Plot the final positions
plt.scatter(x[:,-1],y[:,-1])
plt.title('Final atom positions')
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(ymin=0,ymax=L)
plt.xlim(xmin=0,xmax=L)
plt.savefig(filename='Plot2.png')
plt.show()

# particle square velocity
vel = np.square(vx) + np.square(vy)

# Plot a histogram of the square velocity.
plt.hist(vel[:,-2],32)
plt.title('Histogram of particle square velocity')
plt.xlabel('square velocity')
plt.ylabel('number of particles')
plt.savefig(filename='Plot3.png')
plt.show()

# Create an array of velocities.
velmap = np.zeros((int(L),int(L)))
for p in range(Natoms):
	velmap[int(x[p,-2]),int(y[p,-2])] = vel[p,-2]

# Plot the particles and display how fast they are moving using a heat map.
# This aligns the particles to a rigid grid, to correct that we could increase the 'resolution' by just multiplying every number by some scaling factor.
# This in turn makes the tiny dot sizes too small to see.  I can't find anything to make the dot size larger as a simple command or flag, but this is solvable by setting adjacent blocks of cells the same as the target cell
# This code for example sets a square 40x40 pixels centered on the particle location to make it easy to see, but the codealso take a longer time to run so when we do this.
# velmap = np.zeros((int(100*L),int(100*L)))
# for p in range(Natoms):
# 	velmap[int(100*x[p,-2])-20:int(100*x[p,-2])+20,int(100*y[p,-2])-20:int(100*y[p,-2])+20] = vel[p,-2]

plt.imshow(velmap,cmap = plt.cm.hot_r,origin='lower')
plt.title('Heat map of particle speed')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig(filename='Plot4.png')
plt.show()

# Calculate kiinetic energy for each stpe using the square velocity.
KEnergy = 0.5*vel
Klist = np.zeros(Nsteps)

for step in range(Nsteps):
	Klist[step] = np.sum(KEnergy[:,step])

# Find the total energy at each step.
Tlist = Klist + PEnergy

# Plot the energy at each step.  Energy does not appear to be conserved s there is some flaw in the code.
plt.plot(range(Nsteps),Tlist,'k-',label='Total Energy')
plt.plot(range(Nsteps),PEnergy,'b-',label='Potential Energy')
plt.plot(range(Nsteps),Klist,'r-',label='Kinetic Energy')
plt.title('Energy over time')
plt.legend(loc='center')
plt.xlabel('step')
plt.ylabel('energy')
plt.savefig(filename='Plot5.png')
plt.show()

# This plot is to keep track of the number of times the solution had to be rounded up because the particles were too close.  This doesn't actually appear to ever happen normally however.
# This was added to check if the rounding was causing the energy fluctuations.
plt.plot(range(Nsteps),rounded,'ko')
plt.title('Number of times the script prevented two \n particles from \'colliding\' by rounding')
plt.xlabel('step')
plt.ylim(ymin=0,ymax=5)
plt.ylabel('number of times rounded')
plt.savefig(filename='Plot6.png')
plt.show()

# The histograms do look like a boltzmann distribution.
# Energy seems to fluctuate around a value.  the fluctuations are not due to rounding as rounding simply doesn't appear to actually happen.
# This code was modified to fill in the lower triangle of the force array, then the transpose is subtracted to avoid recalculating the forces between pairs of particles.