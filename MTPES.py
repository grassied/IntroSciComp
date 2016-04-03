#Dylan Grassie

import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#constants
k = 1.0         #spring constant
m = 1.0         #mass
ti = 0.0        #initial time
tf = 5.0        #final time
dt = 0.01       #change in time

#starting positions
x = 1.0
y = 1.0

#variables
vx = 0.0        #x velocity
vy = 0.0        #y velocity
Fx = 0.0        #x force
Fy = 0.0        #y force

#lists
xL = []
yL = []
TL = []
VL = []
EL = []

#Functions
def updFor(a): #Force
        Fa = -k * a #F(x) = -dV(x)/dx
        return Fa

def updVel(va, Fa): #Velocity
        va = va + dt * (Fa / m) #vx = vx + dt * (f(x) / m)
        return va

def updPos(a, va): #Position
        a = a + dt * va # x = x + dt * v(x)
        return a

def updPot(a, b): #Potential Energy
        Vab = (1.0/2.0) * k * (a**2 + b**2) #V(xy) =  Vx + Vy
        return Vab

def updKin(va, vb): #Kinetic Energy
        Tab = (m/2.0) * (va**2 + vb**2) #T(xy) = Tx + Ty
        return Tab

def outStr(n, z):
        zMin = str(min(z))
        zMax = str(max(z))
        xLoc = str(xL[z.index(min(z))])
        yLoc = str(yL[z.index(min(z))])
        zAve = str(np.mean(z))
        myStr = "Lowest %s is %s and is located at (%s, %s)\nAverage %s is %s" %(n, zMin, xLoc, yLoc, n, zAve)
        print myStr

def map(tA, z):
	plt.plot(tA, z)
	plt.show()

for i in np.arange(ti, tf, dt):
        x = updPos(x, vx)
	y = updPos(y, vy)
        Fx = updFor(x)
	Fy = updFor(y)
        vx = updVel(vx, Fx)
	vy = updVel(vy, Fy)
	Vxy = updPot(x, y)
	Txy = updKin(vx, vy)
	xL.append(x)
	yL.append(y)
	VL.append(Vxy)
	TL.append(Txy)
	EL.append(Txy + Vxy) #E = T(xy) + V(xy)

outStr("Potential Energy", VL)
outStr("Kinetic energy", TL)
print "Average Total Energy is: " + str(np.mean(EL))
map(xL, yL, VL, "Potential Energy Surface")
map(xL, yL, TL, "Kinetic Energy Surface")
map(xL, yL, EL, "Energy Surface")
raw_input("press enter to continue")
