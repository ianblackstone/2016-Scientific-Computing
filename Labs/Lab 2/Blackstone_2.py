# Imports
import math

# Define the function f to be integrated.
def f(x):
	return math.sin(x) * math.exp(x)

# Set the numer of bins, the start and end points, and the width of each bin.
n = 100
a = 0
b = 1
w = (b-a)/n

# Define s
s = (f(a) + f(b))/2

# Sum each bin
for k in range(1,n):
	s += f(a+k*w)

# Print the output
print(w*s)