# Imports
import numpy as np
import scipy.integrate as inter
import matplotlib.pyplot as plt

# Constants and initial conditions
GM = -4*np.pi**2
Gm = -4*np.pi**2 * 9.5*10**(-4)
Pjx0 = 5.455
Pjy0 = 0
Psx0 = 0
Psy0 = 0
Vjx0 = 0
Vjy0 = 2.62416
Vsx0 = 0
Vsy0 = -0.0025

# Create a list of all initial conditions
r = [Pjx0,Pjy0,Psx0,Psy0,Vjx0,Vjy0,Vsx0,Vsy0]

# Define a function that returns the derivatives of the inputs
def f(PV,t):
	Pjx = PV[0]
	Pjy = PV[1]
	Psx = PV[2]
	Psy = PV[3]
	Vjx = PV[4]
	Vjy = PV[5]
	Vsx = PV[6]
	Vsy = PV[7]

	Ajx = GM*(Pjx-Psx)/((Pjx-Psx)**2 + (Pjy-Psy)**2)**(3/2)
	Ajy = GM*(Pjy-Psy)/((Pjx-Psx)**2 + (Pjy-Psy)**2)**(3/2)
	Asx = Gm*(Psx-Pjx)/((Pjx-Psx)**2 + (Pjy-Psy)**2)**(3/2)
	Asy = Gm*(Psy-Pjy)/((Pjx-Psx)**2 + (Pjy-Psy)**2)**(3/2)
	return [Vjx,Vjy,Vsx,Vsy,Ajx,Ajy,Asx,Asy]

# Create a list of times
times = np.linspace(0,100,1000000)

# Call the ODE solver
solve = inter.odeint(f,r,times)

# Plot the data
plt.plot(solve[:,0],solve[:,1],'g',label='Jupiter')
plt.plot(solve[:,2],solve[:,3],'r',label='The sun')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('2 body simulation: The sun and Jupiter.')
plt.savefig(filename='Plot1.png')
plt.show()