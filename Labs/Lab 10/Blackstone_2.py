import numpy.random as random
import numpy as np
import matplotlib.pyplot as plt

N = range(1,1000)
estimates = np.zeros(N[-1])

def estimatepi(N):
	xpos = 2*random.rand(N) - 1
	ypos = 2*random.rand(N) - 1
	dist = np.sqrt(np.square(xpos)+np.square(ypos))
	incircle = sum([i for i in dist <= 1])
	outcircle = sum([i for i in dist > 1])
	if outcircle == 0:
		outcircle = 1
	return incircle/outcircle

for n in N:
	estimates[n-1] = estimatepi(n)

plt.plot(N,estimates,'b-',label='estimate')
plt.plot(N,np.pi*np.ones(N[-1]),'r-',label='pi',linewidth=2)
plt.ylabel('pi estimate')
plt.xlabel('N')
plt.title('estimate of pi using the circle method for N points')
plt.legend()
plt.tight_layout()
plt.savefig('plot_2.png')
plt.show()