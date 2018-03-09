from numpy import *
from matplotlib.pyplot import *

N=int(1e4)
x = arange(N)+1

plot(x,ones(N)/(2*pi))
show()