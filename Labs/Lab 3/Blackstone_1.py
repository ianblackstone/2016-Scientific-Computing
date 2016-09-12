# Imports
import numpy as np

# Set the range to be integrated over and initialize an empty list
a = 0
b = np.pi
approx = []


# Define the function f to be integrated.
def f(x):
	return np.sin(x) * np.exp(-x)

# Define a function for the trapazoidal rule
def trap(n):
	h = (b-a)/n
	s = (f(a) + f(b))/2
	for k in range(1,n):
		s += f(a + k*h)
	s = s*h
	return s

# Define a function for the simpson rule, n must be even so the function checks that n is even.
def simp(n):
	if n % 2 == 0:
		h = (b-a)/n
		s = (f(a) + f(b))
		for k in range(1,int(n/2)):
			s += 4*f(a + h*(2*k-1))
		for k in range(1,int(n/2-1)):
			s += 2*f(a + 2*k*h)
		s = s*h/3
		return s
	else:
		return None

# calculate the trapazoidal and simpsons rule for each even value of n.  Append the data for both to the empty list.
for n in range(2,21,2):
	approx.append([n,trap(n),simp(n)])

# Save the list at data.txt with 8 decimal points of precision and a header row
savefile = np.savetxt(fname='data.txt',X=approx,fmt='%.f %.8f %.8f',header ='bins trapazoidal simpsons')