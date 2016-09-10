# Imports
import numpy as np

# Set the numer of bins, the start and end points, and the width of each bin.
a = 0
b = np.pi
approx = []


# Define the function f to be integrated.
def f(x):
	return np.sin(x) * np.exp(-x)

# Sum each bin
def trap(n):
	h = (b-a)/n
	s = (f(a) + f(b))/2
	for k in range(1,n):
		s += f(a + k*h)
	s = s*h
	return s

def simp(n):
	h = (b-a)/n
	s = (f(a) + f(b))
	for k in range(1,int(n/2)):
		s += 4*f(a + h*(2*k-1))
	for k in range(1,int(n/2-1)):
		s += 2*f(a + 2*k*h)
	s = s*h/3
	return s

for n in range(2,21,2):
	approx.append([n,trap(n),simp(n)])

savefile = np.savetxt(fname='data.txt',X=approx,fmt='%.f %.8f %.8f',header ='bins trapazoidal simpsons')