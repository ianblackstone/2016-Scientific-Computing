import numpy as np
import scipy.integrate as inter
import matplotlib.pyplot as plt

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
Vsy0 = -0.0025
Vex0 = 0
Vey0 = 2*np.pi

r = [Pjx0,Pjy0,Pex0,Pey0,Psx0,Psy0,Vjx0,Vjy0,Vex0,Vey0,Vsx0,Vsy0]

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

times = np.linspace(0,100,1000000)

solve = inter.odeint(f,r,times)

plt.plot(solve[:,0],solve[:,1],'g')
plt.plot(solve[:,2],solve[:,3],'b')
plt.plot(solve[:,4],solve[:,5],'r')
plt.show()