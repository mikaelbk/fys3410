from numpy import *
from matplotlib.pyplot import *
from scipy import constants


hbar = 1.0545718E-34 # Plancks reduced constant
m = 9.10938356E-31 # electron mass
kb = 1.38064852E-23 # Boltzmann constant
q = constants.e # elementary charge

def e(k):
	return (k*hbar)**2/(2*m)

def k(c):
	return (3*pi**2*c)**(1/3.0)

def v(k):
	return hbar*k/m

def t(e):
	return e/kb

c = 4.7E22*(1E6)
print(k(c)*1E-8*1E-2)
print(e(k(c))/q)
print(v(k(c))*1E-8*1E2)

elCon = 1E28*array( [4.7,2.65,1.4,1.15,0.91] )

subplot(2,2,1)
title("k vector $k_F$")
plot(k(elCon),'bo')
plot(k(elCon))

subplot(2,2,2)
title("energy $\epsilon_F$")
plot(e(k(elCon)),'bo')
plot(e(k(elCon)))

subplot(2,2,3)
title("velocity $v_F$")
plot(v(k(elCon)),'bo')
plot(v(k(elCon)))

subplot(2,2,4)
title("temperature $T_F$")
plot(t(e(k(elCon))),'bo')
plot(t(e(k(elCon))))
savefig("4plot.pdf")