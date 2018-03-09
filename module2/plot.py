from numpy import *
from matplotlib.pyplot import *

N=int(1e2)
x = arange(N)+1

def dos(w,w0):
	return N/(pi*sqrt(w0**2-w**2))

figure()
plot(x,dos(x,N))
xlabel("$\omega$")
ylabel("DOS")
savefig("2b.pdf")

figure()
plot(x,ones(N)/(2*pi))
xlabel("k")
ylabel("DOS[L]",rotation=0)
grid()
savefig("2a.pdf")