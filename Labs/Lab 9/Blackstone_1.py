import numpy.random as random
import matplotlib.pyplot as plt

m = 1000
b = 10
x = range(1,b)

n = random.rand(m)

nav = []
tar = []
npr = []

for k in x:
	nk = n**k
	nav.append(sum(nk)/m)
	tar.append(1/(k+1))
	ni = []
	for i in range(0,m-1):
		if i+k > m-1:
			s = i-k
		else:
			s = i+k
		ni.append(n[i]*n[s])
	npr.append(sum(ni)/m)

plt.plot(x,nav,'b-',x,tar,'ro')
plt.savefig('plot1.png')
plt.show()

plt.plot(x,npr,'b-')
plt.savefig('plot2.png')
plt.show()