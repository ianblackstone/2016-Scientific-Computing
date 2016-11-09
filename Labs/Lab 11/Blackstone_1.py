# Imports
import numpy as np
import matplotlib.pyplot as plt

ncells = 256  # number of sites to fill
nside = 256   # width of the grid

body = np.zeros((nside,nside)) - 1  # array holding the cell occupancy counter (-1=empty; 0 = candidate; 1=filled)
age = np.zeros((nside,nside))    # make an array that holds the step number for which the cell is occupied

# Maximum number of steps a walker should take.
nsteps = 100

# An array containing the relative coordinates of neighboring cells.
neighbors = np.array([
	(0, 1), 
	(0, -1), 
	(1, 0), 
	(-1, 0)
])

# Find the center and place a nucleation site there. 
ctr = int(nside/2)
body[ctr,ctr] = 1

# set the nieghboring cells as possible growth sites.
for near in neighbors:
	body[ctr+near[0],ctr+near[1]] = 0

# A loop that repeats until we reach ncells filled cells.
for i in range(ncells-1):
	# reset the flag for a found point.
	flag = 0
	# Try spawning random walkers until a cell is filled.
	while flag == 0:
		# Spawn a walker in a random location.
		position = [int(round(nside*np.random.rand())),int(round(nside*np.random.rand()))]
		for j in range(1,nsteps):
			# Randomly choose a step and add the result of that step to the previous position.
			step = neighbors[np.random.randint(4)]
			propstep = [ position[0] + step[0] , position[1] + step[1] ]
			# check if the walker has run out of steps, is out of bounds, or is in a candidate cell.
			if j == nsteps:
				break
			elif propstep[0] <= 0 or propstep[0] >= nside or propstep[1] <= 0 or propstep[1] >= nside:
				break
			elif body[ propstep[0], propstep[1] ] == 0:
				flag = 1
				break
			# If none of the above take the proposed step.
			else:
				position = propstep 
	# Set The candidate cell to filled.
	body[ position[0], position[1] ] = 1

	for near in neighbors:    # now check the neighbors, and if -1 change to 0
		if body[ position[0] + near[0], position[1] + near[1] ] == -1:
			body[ position[0] + near[0], position[1] + near[1] ] = 0
	age[position[0],position[1]] = ncells-i   # record the age for the filled site at the end of the run

unfilled = np.where(body == -1)  # find non-filled/non-candidate sites
body[unfilled] = 0             # set them equal to zero

# Plot the data.
plt.imshow(age,cmap = plt.cm.spectral)
plt.savefig("plot_1.png")
plt.show()