from numpy import *
from matplotlib.pyplot import *
rc('text', usetex = True)

def mad(n):
	v = 0.0
	for i in range(n):
		i = i+1
		v = v + ( (-1.0)**i / i )
	return v

x = arange(int(50)) + 1
y = zeros(len(x))

for i in range(len(x)):
	y[i] = mad(x[i])

plot(x,y)
title("Madelung constant for 1D NaCl lattice as function of nearest neighbour pairs")
xlabel("Number of neighbouring pairs accounted for")
ylabel("Electrical potential V with factor $\\frac{4\\pi\\epsilon_0 a}{2e}$ ")
show()