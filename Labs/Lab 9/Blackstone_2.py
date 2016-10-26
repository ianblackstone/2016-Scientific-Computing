import numpy as np
import matplotlib.pyplot as plt

nwalk = 100
nsteps = 100

steps = 2*np.pi*np.random.rand(nwalk,nsteps,2)
xsteps = np.zeros((nwalk,nsteps))
ysteps = np.zeros((nwalk,nsteps))

for i in range(nwalk):          # loop over walkers
    for j in range(1,nsteps):        # loop over steps all start at 0,0
      xsteps[i,j]=xsteps[i,j-1] + np.cos(steps[i,j,0])
      ysteps[i,j]=ysteps[i,j-1] + np.sin(steps[i,j,1])

for k in range(10):
    plt.plot(xsteps[k,:],ysteps[k,:])
    
plt.xlabel('x positions');
plt.ylabel('y position');
plt.savefig('plot3.png')
plt.show()

dist = np.sqrt(np.square(xsteps[:,-1]) + np.square(ysteps[:,-1]))

plt.hist(dist)
plt.show()