# Imports
import numpy as np
import matplotlib.pyplot as plt

# determine the number of walkers and steps
nwalk = 100
nsteps = 100

# generate random directions and step sizes for each step and generate a list of zeros for the x and y positions
steps = 2*np.pi*np.random.rand(nwalk,nsteps,2)
augstep = np.random.normal(1,0.2,[nwalk,nsteps])
xsteps = np.zeros((nwalk,nsteps))
ysteps = np.zeros((nwalk,nsteps))

# for each walker calculate the position after each step.
for i in range(nwalk):
    for j in range(1,nsteps):
      xsteps[i,j]=xsteps[i,j-1] + augstep[i,j]*np.cos(steps[i,j,0])
      ysteps[i,j]=ysteps[i,j-1] + augstep[i,j]*np.sin(steps[i,j,1])

# Calculate the distance moved by each walker
dist = np.sqrt(np.square(xsteps[:,-1]) + np.square(ysteps[:,-1]))

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
plt.savefig('plot5.png')
plt.show()

# The histogram has the same average as we expect, same as the excersize 2, but now the
# distribution is more reliably grouped around the expected average.