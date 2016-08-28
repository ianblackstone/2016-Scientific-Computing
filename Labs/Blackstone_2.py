import scipy.constants as consts

#User defined constants
a = float(input('Enter the bin width in meters:'))
n = int(input('Enter the quantum number n:'))

#scipy defined constants
hbar=consts.hbar
pi=consts.pi
Me=consts.physical_constants['electron mass energy equivalent'][0]

#Calculate energy level
E=n**2 * hbar**2 * pi**2 / (2*Me*a)
print('The energy is ' + str(E) + ' Joules')