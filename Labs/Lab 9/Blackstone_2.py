# Imports
import numpy as np
import matplotlib.pyplot as plt

# determine the number of walkers and steps
nwalk = 100
nsteps = 100

# generate random directions for each step and generate a list of zeros for the x and y positions
steps = 2*np.pi*np.random.rand(nwalk,nsteps,2)
xsteps = np.zeros((nwalk,nsteps))
ysteps = np.zeros((nwalk,nsteps))

# for each walker calculate the position after each step.
for i in range(nwalk):
    for j in range(1,nsteps):
      xsteps[i,j]=xsteps[i,j-1] + np.cos(steps[i,j,0])
      ysteps[i,j]=ysteps[i,j-1] + np.sin(steps[i,j,1])

# Plot the first 10 walkers
for k in range(10):
    plt.plot(xsteps[k,:],ysteps[k,:])    
plt.xlabel('x positions');
plt.ylabel('y position');
plt.title('Paths of the first 10 walkers')
plt.tight_layout()
plt.savefig('plot3.png')
plt.show()

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
plt.savefig('plot4.png')
plt.show()

# The histogram does not necissarily peak at the expected value, but the actual average is close to the expected value.