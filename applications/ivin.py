from pylab import *

x=linspace(0,10,1000)

a=cos(pi*x)
b=a*(e**(-0.2*x))
d=e**(-0.2*x)
f=-1*e**(-0.2*x)
c=e**(-0.5*x)

figure("Comparision of oscillations")

plot(x,a,color='orange',label="Free oscillations")
plot(x,b,color='green',label="underdamped oscillations")
plot(x,d,color='green', linestyle="--")
plot(x,f,color='green', linestyle="--")
plot(x,c,color='blue',label="overdamped oscillations")
xlabel("Time")
ylabel("Amplitude")
legend(loc='upper right')

show()
