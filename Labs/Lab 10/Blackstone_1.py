# Imports
import numpy as np
import matplotlib.pyplot as plt

# determine the number of walkers and steps
nwalk = 100
nsteps = 100


# initialize a list.
xy = np.zeros((nwalk,nsteps,2))

# for each walker.
for i in range(nwalk):

	# for each step
	for j in range(1,nsteps):
		# clear the possible steps.
		steps = []
		# check if each step can be taken, if yes add it to the list of possible moves.
		if [ xy[i,j-1,0] + 1 , xy[i,j-1,1] ] not in np.ndarray.tolist(xy[i,:]):
			steps.append([1,0])

		if [ xy[i,j-1,0] - 1 , xy[i,j-1,1] ] not in np.ndarray.tolist(xy[i,:]):
			steps.append([-1,0])

		if [ xy[i,j-1,0] , xy[i,j-1,1] + 1 ] not in np.ndarray.tolist(xy[i,:]):
			steps.append([0,1])

		if [ xy[i,j-1,0] , xy[i,j-1,1] - 1 ] not in np.ndarray.tolist(xy[i,:]):
			steps.append([0,-1])
		# If no steps available abandon this walker.
		if steps == []:
			xy[i,j:nsteps] = xy[i,j-1]
			break
		# Randomly choose a step and add the result of that step to our position list.
		step = steps[np.random.randint(len(steps))]
		xy[i,j] = [ xy[i,j-1,0] + step[0] , xy[i,j-1,1] + step[1] ]

print(xy)
# Plot the first 10 walkers
for k in range(10):
	plt.plot(xy[k,:,0],xy[k,:,1])
plt.xlabel('x positions');
plt.ylabel('y position');
plt.title('Paths of the first 10 walkers')
plt.tight_layout()
plt.savefig('plot3.png')
plt.show()

# Calculate the distance moved by each walker
dist = np.sqrt(np.square(xy[:,-1,0]) + np.square(xy[:,-1,1]))

# Create a histogram of the distance traveled for each walker.
plt.hist(dist)
plt.axvline(np.sqrt(nsteps),color='r',label='Expected average')
plt.axvline(np.sqrt(np.mean(np.square(dist))),color='g',label='Average')
plt.xlim(xmin=0,xmax=max(dist))
plt.xlabel('Distance traveled')
plt.ylabel('Number of walkers')
plt.title('Number of walkers to travel a given distance')
plt.legend()
plt.tight_layout()
plt.savefig('plot4.png')
plt.show()

# The histogram does not necissarily peak at the expected value, but the actual average is close to the expected value.