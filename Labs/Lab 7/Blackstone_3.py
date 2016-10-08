# Imports
import numpy as np
import scipy.integrate as inter
import matplotlib.pyplot as plt

# Constants and initial conditions
GMs = -4*np.pi**2
Gmj = -4*np.pi**2 * 9.5*10**(-1)
Gme = -4*np.pi**2 * 3*10**(-6)
Pjx0 = 5.455
Pjy0 = 0
Psx0 = 0
Psy0 = 0
Pex0 = 1
Pey0 = 0
Vjx0 = 0
Vjy0 = 2.62416
Vsx0 = 0
# The value of Vsy0 needed to make the net momentum of the system 0 is approximately -5, but this causes the sun to escape the system.
# Since that clearly doesn't work I'll stick with the value from exercises one and two and simply have to accept that the system
# has a net + y momentum throwing the movement off.
Vsy0 = -0.0025
Vex0 = 0
Vey0 = 2*np.pi

# Create a list of all initial conditions
r = [Pjx0,Pjy0,Pex0,Pey0,Psx0,Psy0,Vjx0,Vjy0,Vex0,Vey0,Vsx0,Vsy0]

# Define a function that returns the derivatives of the inputs
def f(PV,t):
	Pjx = PV[0]
	Pjy = PV[1]
	Pex = PV[2]
	Pey = PV[3]
	Psx = PV[4]
	Psy = PV[5]
	Vjx = PV[6]
	Vjy = PV[7]
	Vex = PV[8]
	Vey = PV[9]
	Vsx = PV[10]
	Vsy = PV[11]

	Rsj = (Pjx-Psx)**2 + (Pjy-Psy)**2
	Rse = (Pex-Psx)**2 + (Pey-Psy)**2
	Rej = (Pjx-Pex)**2 + (Pjy-Pey)**2

	Ajx = GMs*(Pjx-Psx)/(Rsj)**(3/2) + Gme*(Pjx-Pex)/(Rej)**(3/2)
	Ajy = GMs*(Pjy-Psy)/(Rsj)**(3/2) + Gme*(Pjy-Pey)/(Rej)**(3/2)
	Asx = Gmj*(Psx-Pjx)/(Rsj)**(3/2) + Gme*(Psx-Pex)/(Rse)**(3/2)
	Asy = Gmj*(Psy-Pjy)/(Rsj)**(3/2) + Gme*(Psy-Pey)/(Rse)**(3/2)
	Aex = GMs*(Pex-Psx)/(Rse)**(3/2) + Gmj*(Pex-Pjx)/(Rej)**(3/2)
	Aey = GMs*(Pey-Psy)/(Rse)**(3/2) + Gmj*(Pey-Pjy)/(Rej)**(3/2)

	return [Vjx,Vjy,Vex,Vey,Vsx,Vsy,Ajx,Ajy,Aex,Aey,Asx,Asy]

# Create a list of times
times = np.linspace(0,100,1000000)

# Call the ODE solver
solve = inter.odeint(f,r,times)

# Plot the data
plt.plot(solve[:,0],solve[:,1],'g', label='super-Jupiter')
plt.plot(solve[:,2],solve[:,3],'b', label='earth')
plt.plot(solve[:,4],solve[:,5],'r', label='the sun')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('3 body simulation: Earth, the sun, and super-Jupiter.')
plt.savefig(filename='Plot3.png')
plt.show()

# This graph doesn't work well, we would need to balance it to keep the net momentum of the system 0 but doing so nudges the system in ways
# that force it into a 'pleasing' look rather than being an actual representation of the system.  This code is very sensitive to very small
# changes, ejecting one body in nearly every setup and causing ODE warnings at certain configurations.