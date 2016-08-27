import scipy.constants

#User defined constants
a = float(input('Enter the bin width in meters:'))
n = int(input('Enter the quantum number n:'))

#scipy defined constants
hbar=scipy.constants.hbar
pi=scipy.constants.pi
Me=scipy.constants.electron_mass

#Calculate energy level
E=n**2 * hbar**2 * pi**2 / (2*Me*a)
print('The energy is ' + str(E) + ' Joules')