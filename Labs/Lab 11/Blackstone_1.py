# Imports
import numpy as np
import matplotlib.pyplot as plt

ncells=20  #number of sites to fill
nside=20    #width of the grid
r = 15

body=np.zeros((nside,nside))-1  #array holding the cell occupancy counter (-1=empty; 0 = candidate; 1=filled)
age=np.zeros((nside,nside))    #make an array that holds the step number for which the cell is occupied

nsteps = 10
neighbors=np.array([
	(0, 1), 
	(0, -1), 
	(1, 0), 
	(-1, 0)
])

ctr=int(nside/2)
body[ctr,ctr] = 1
for near in neighbors:
	body[ctr+near[0],ctr+near[1]] = 0

for i in range(ncells-1):
	flag = 0
	while flag == 0:
		theta = 2*np.pi*np.random.rand()
		position = [int(round(r*np.cos(theta))),int(round(r*np.sin(theta)))]
		for j in range(1,nsteps):
			# Randomly choose a step and add the result of that step to our position list.
			step = neighbors[np.random.randint(4)]
			propstep = [ position[0] + step[0] , position[1] + step[1] ]
			if j == nsteps:
				break
			elif propstep[0] <= 0 or propstep[0] >= nside or propstep[1] <= 0 or propstep[1] >= nside:
				break
			elif body[ propstep[0], propstep[1] ] == 0:
				flag = 1
				break
			else:
				position = propstep 
	# if i < 237:
	# 	r += 1
	# 	nsteps += 1
	body[ position[0], position[1] ] = 1
	for near in neighbors:    #now check the neighbors, and if -1 change to 0
		if body[ position[0] + near[0], position[1] + near[1] ] == -1:
			body[ position[0] + near[0], position[1] + near[1] ] = 0
	age[position[0],position[1]]= ncells-i   #record the age for the filled site at the end of the run
	


unfilled=np.where(body == -1)  #find non-filled/non-candidate sites
body[unfilled] = 0             #set them equal to zero

plt.imshow(age,cmap=plt.cm.spectral)
plt.show()