# Imports
import matplotlib.pyplot as plt
import numpy as np

# define mean lifetime (half life * ln(2)) and step size in days
tau = 3.82*1.44
h = 0.0001
flag = 0

def f(N):
	return -N/tau

# Create a list with the initial value in the first cell
Nlist = [250]
tlist = np.arange(0,30,h)

# Calculate the next value of N using the previous value of N
for t in range(0,len(tlist)):
	N = Nlist[t]
	k = h*f(N)
	k2 = h*f(N + k/2)
	Nlist.append(N + (k+k2)/2)
	if N < 100 and flag == 0:
		print(tlist[t])
		flag = 1
