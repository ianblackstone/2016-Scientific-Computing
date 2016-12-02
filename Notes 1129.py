# xi,yi = position of the particle
# n+1th step:
# xi(h+1) = 2*xi(h) - xi(h-1) + aix(h)*dt**2
# yi(h+1) = 2*yi(h) - yi(h-1) + aiy(h)*dt**2
# aix, aiy = sum of acceleration components from every other particle

# This will be three nested for loops, one to move each particle, one to calculate the acceleration for each particle, one for each time step.

# Ideal gas of argon atoms
# Lennard-Jones potential
# V(r) = 4*E * ((sigma/n)**12 - (sigma/n)**6)
# 4E is the characteristic energy, ^12 term is hard scattering core, ^6 term is van der waals.
# F = - dV/dr

# Units: E = 1, sigma = 1.
# real units: E/k = 120K, sigma = 3.4 Angstroms.
# Time unit: from Energy = mass * (distance/time)^2, we solve for t.  From that we get the units of t as t = sqrt(m*sigma^2 / E)
# t = 1.8*10**-12 s, t = 1.8E-12.

# V = 4*(r**(-12) - r**(-6))
# F = 24 * ((2/r**13) - r**(-7)) in the rhat direction.  This is the force between two particles, this will need to be summed up for every particle.

# for pairs of particles k,j using m=1.
# aj,x = sum k!=j, Fkj * cos(thetakj)
# aj,y = sum k!=j, Fkj * sin(thetakj)
# Fkj is the magnitude of the force from particle k on particle j.
# thetakj is the angle of the line from j to k with respect to the x axis.

