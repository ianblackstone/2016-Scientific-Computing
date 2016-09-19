import numpy as np
import matplotlib.pyplot as plt

def f(r,t):
	x = r[0]
	y = r[1]
	fx = x*y - x
	fy = y -x*y + np.sin(t)
	return np.array([fx,fx],float)

a = 0.0
b = 10.0
N = 10
h = (b-a)/N

tpoints = np.arange(a,b,h)
xpoints = []
ypoints = []

r = np.array([1.0,1.0],float)

for t in tpoints:
	xpoints.append(r[0])
	ypoints.append(r[1])
	k1 = h*f(r,t)
	k2 = h*f(r+0.5*k1,t+0.5*h)
	r += 

print(xpoints)
print(ypoints)

plt.plot(tpoints,xpoints)
plt.plot(tpoints,ypoints)
plt.xlabel("t")
plt.show()