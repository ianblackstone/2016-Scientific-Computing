# Imports
import numpy.random as random
import numpy as np
import matplotlib.pyplot as plt

# Generate a list of N values and a list of zeros.
N = range(1,1000)
estimates = np.zeros(N[-1])

# Create a function that estimates pi.
def estimatepi(N):
	# generate an xy position with -1 to 1 and find the distance to the point.
	xpos = 2*random.rand(N) - 1
	ypos = 2*random.rand(N) - 1
	dist = np.sqrt(np.square(xpos)+np.square(ypos))

	# Count the points in and out of a circle of radius 1.
	incircle = sum([i for i in dist <= 1])
	outcircle = sum([i for i in dist > 1])

	# Prevent division by 0.
	if outcircle == 0:
		outcircle = 1
	return incircle/outcircle

# Estimate pi for N points.
for n in N:
	estimates[n-1] = estimatepi(n)

# Plot the estimates and the known value of pi.
plt.plot(N,estimates,'b-',label='estimate')
plt.plot(N,np.pi*np.ones(N[-1]),'r-',label='pi',linewidth=2)
plt.ylabel('pi estimate')
plt.xlabel('N')
plt.title('estimate of pi using the circle method for N points')
plt.legend()
plt.tight_layout()
plt.savefig('plot_3.png')
plt.show()