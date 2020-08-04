from numpy import *
from pylab import *

I,R,X=[50000/2400,1.72,1.82]

def V_1(t):
	return abs( (Vs-I*(R*cos(t)+X*sin(t)) ) - 1j*(-I*R*sin(t)+X*cos(t)) )

def V_2(t):
	return Vs-I*( R*cos(t)+X*sin(t) )

t=linspace(-pi/2,pi/2,41)
Vs=array([2400]*len(t))

p=V_1(t)*cos(t)*I
#pow=p+I*I*R*


figure(0)
plot(t*180/pi,V_1(t)/10,color='g',label="exact")
plot(t*180/pi,V_2(t)/10,color='orange',label="apprx")
plot(t*180/pi,Vs/10,color='b',label="240")


xlabel("angle (+ve means lag)")
legend(loc="upper right")

figure(1)
plot(t*180/pi,p/500,color='m',label='Load power')
#plot(t*180/pi,pow/500,color='m',label='source power')
show()
