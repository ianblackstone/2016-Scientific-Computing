# imports
import numpy.random as random
import matplotlib.pyplot as plt

# Set number of random numbers and number of loops.
m = 1000
b = 11
x = range(1,b)

# Generate a list of random numbers.
n = random.rand(m)

# Create three empty lists, average, target, and product.
nav = []
tar = []
npr = []

# calculate n^k for each value of k as well as the expected value of the average.
for k in x:
	nk = n**k
	nav.append(sum(nk)/m)
	tar.append(1/(k+1))
	# create an empty list for this value of k.
	ni = []
	# fill the empty list ni with the products of each cell of n and its kth neighbor.
	for i in range(0,m-1):
		# Avoid calling for values of n that don't exist by checking that our indexes are not out of range.
		if i+k > m-1:
			s = i-2*k
		else:
			s = i+k
		# append the product of n and its kth neighbor (or -2*kth neighbor for the last k values of n)
		ni.append(n[i]*n[s])
	npr.append(sum(ni)/m)

# Plot the average value
plt.plot(x,nav,'b-',label='Average')
plt.plot(x,tar,'ro',label='Expected')
plt.xlabel('K')
plt.ylabel('average value of n^k')
plt.title('average n^k by k')
plt.legend()
plt.savefig('plot1.png')
plt.show()

# plot the average product
plt.plot(x,npr,'b-',label='Average product')
plt.plot([1,x[-1]],[0.25,0.25],'--',label='Expected')
plt.xlabel('K')
plt.ylabel('average product')
plt.title('average product of n and its kth neighbor')
plt.ylim(ymax = 0.5,ymin = 0)
plt.legend()
plt.savefig('plot2.png')
plt.show()

# Both of these test show that the random numbers being generated are
# independent and well distributed within the range.