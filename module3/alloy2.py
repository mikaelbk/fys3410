from math import*
from numpy import*
from matplotlib.pyplot import *

L = 1
N = 1
c = linspace(0,1,1e3)

def kF(x):
	Z = (1-x)+2*x
	e1 = (6*pi**2)**(1/3.)
	e2 = (Z*N)**(1/3.)/(N*L)
	return e1*e2

kBZ = ones(len(c))*pi/L

C = kF(c)

for i in range(len(c)):
	if(kBZ[i]-C[i] > 0):
		print(i)
		print(C[i])
		break

print(kF(5))

plot(c*100,kF(c)/kBZ)
plot(c*100,kBZ/kBZ)
show()
#savefig("alloy.pdf")