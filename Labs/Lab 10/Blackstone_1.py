# Imports
import numpy as np
import matplotlib.pyplot as plt

# determine the number of walkers and steps
nwalk = 1
nsteps = 10

# generate random directions for each step and generate a list of zeros for the x and y positions
# steps = 2*np.pi*np.random.rand(nwalk,nsteps,2)
# xsteps = np.zeros((nwalk,nsteps))
# ysteps = np.zeros((nwalk,nsteps))

# xy[walker,step,x or y]
xy = np.zeros((nwalk,nsteps,2))


for i in range(nwalk):
	for j in range(nsteps):
		steps = []
		# step = steps[np.random.randint(4)]
		if [xy[i,j-1,0] + 1,xy[i,j-1]] is not in xy[i,:]
		a = [xy[i,j-1,0] + step[0],xy[i,j-1,1] + step[1]]
		xy[i,j] = a



# step = steps[np.random.randint(4)]
# print(step)

# xy[0,1] = xy[0,0] + step

# print(xy)

# for each walker calculate the position after each step.
# for i in range(nwalk):
# 	for j in range(1,nsteps):
# 		flag = 0
# 		while flag < 10:
# 			step = steps[np.random.randint(4)]
# 			a = [xy[i,j-1,0] + step[0],xy[i,j-1,1] + step[1]]
# 			print(a)
# 			if a in xy[i]:
# 				flag += 1
# 				print('2')
# 			else:
# 				xy[i,j] = a
# 				flag = 0
# 				print('3')
      # xsteps[i,j]=xsteps[i,j-1] + np.cos(steps[i,j,0])
      # ysteps[i,j]=ysteps[i,j-1] + np.sin(steps[i,j,1])

print(xy)
# # Plot the first 10 walkers
# for k in range(10):
#     plt.plot(xsteps[k,:],ysteps[k,:])    
# plt.xlabel('x positions');
# plt.ylabel('y position');
# plt.title('Paths of the first 10 walkers')
# plt.tight_layout()
# plt.savefig('plot3.png')
# plt.show()

# # Calculate the distance moved by each walker
# dist = np.sqrt(np.square(xsteps[:,-1]) + np.square(ysteps[:,-1]))

# # Create a histogram of the distance traveled for each walker.
# plt.hist(dist)
# plt.axvline(np.sqrt(nsteps),color='r',label='Expected average')
# plt.axvline(np.sqrt(np.mean(np.square(dist))),color='g',label='Average')
# plt.xlim(xmin=0,xmax=max(dist))
# plt.xlabel('Distance traveled')
# plt.ylabel('Number of walkers')
# plt.title('Number of walkers to travel a given distance')
# plt.legend()
# plt.tight_layout()
# plt.savefig('plot4.png')
# plt.show()

# The histogram does not necissarily peak at the expected value, but the actual average is close to the expected value.