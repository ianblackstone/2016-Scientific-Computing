# Imports
import math

# Define the function f to be integrated.
def f(x):
	return math.sin(x) * math.exp(-x)

# Set the numer of bins, the start and end points, and the width of each bin.
n = 10
a = 0
b = math.pi
w = (b-a)/n

# Define s
s = (f(a) + f(b))/2

# Sum each bin
for k in range(1,n):
	s += f(a+k*w)

# Print the output
print('The approximation using 10 bins is ' + str(w*s))


# Redeclare the number of bins and their width
n = 100
w = (b-a)/n

# Set s back to the default value
s = (f(a) + f(b))/2

# Sum each bin
for k in range(1,n):
	s += f(a+k*w)

# Print the output
print('The approximation using 100 bins is ' + str(w*s))