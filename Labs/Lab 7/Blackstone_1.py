import numpy as np
import scipy.integrate as inter
import matplotlib.pyplot as plt

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

r = [Pjx0,Pjy0,Psx0,Psy0,Vjx0,Vjy0,Vsx0,Vsy0]

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

times = np.linspace(0,100,1000000)

solve = inter.odeint(f,r,times)

plt.plot(solve[:,0],solve[:,1],'r')
plt.plot(solve[:,2],solve[:,3],'b')
plt.show()