# Imports
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as inter

# G * the sun's mass in kg.
M = 1.477

# Define wobble and critical radius.  u is defined as 1/r.
w0 = 0.177
rc = 57.9E9
uc = 1/rc

# number of orbits and the number of data points per orbit.
orbits = 1
res = orbits*1000

# Create a list of times, the orbital period is 8.
angles = np.linspace(0,orbits*2*np.pi,res)

# Calculate the wobble as a function of phi.
w = w0*np.cos((1-6*M*uc)*angles)

# Change from u to r.
upoints = uc*(1+w)
rpoints = 1/upoints

# Plot the data, the data range it to plot a single orbit, a second plot could be added to show later orbits but the precession is very small per orbit.
plt.plot(np.cos(angles[0:res])*rpoints[0:res],np.sin(angles[0:res])*rpoints[0:res])
plt.plot(0,0,'ro')
plt.title('Simulated orbit using perturbation calculation')
plt.xlabel('meters')
plt.ylabel('meters')
plt.axes().set_aspect('equal', 'datalim')
plt.savefig('Schwarz_plot_wobble.png')
plt.show()