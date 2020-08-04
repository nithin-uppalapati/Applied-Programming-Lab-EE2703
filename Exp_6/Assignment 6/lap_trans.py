from numpy import *
from pylab import *
import scipy.signal as sp

def trans(a,freq):
	num=array([1,a])
	den=polymul(num,num)
	den=polyadd(den,array([freq**2]))
	
	charac=array([1,0,2.25])
	den_final=polymul(den,charac)
	
	s=[num,den_final,den,charac]
	return s

def input(f,t):
	 return cos(f*t)*exp(-0.05*t)


t=linspace(0,50,501)
################################ 1 ~~~~~~~~~~~~

#r=range(1,10)
a=0.5 	## a is the decay
freq=1.5
s=trans(a,freq)
H_1=sp.lti(s[0],s[1])
w_1,S_1,phi_1=sp.bode(H_1) # w=r

##### plots for 1
subplots(3,1)

subplot(3,1,1).semilogx(w_1,S_1,color='orange')
title("Magnitude Plot")

subplot(3,1,2).semilogx(w_1,phi_1,color='green')
title("Phase Plot")

t_1,x_1=sp.impulse(H_1,None,t)
subplot(3,1,3).plot(t,x_1)
title("Time Response")

suptitle("Plots for Problem_1")


################################ 2 ~~~~~~~~~~~~
#t=linspace(0,150,500)
a=0.05
freq=1.5
s=trans(a,freq)
H_2=sp.lti(s[0],s[1])

w_2,S_2,phi_2=sp.bode(H_2) # w=r

subplots(3,1)

subplot(3,1,1).semilogx(w_2,S_2,color='orange')
title("Magnitude Plot")
xlabel(r'frequency ' '$\longrightarrow$')


subplot(3,1,2).semilogx(w_2,phi_2,color='g')
title("Phase Plot")
xlabel(r'frequency ' '$\longrightarrow$')


t_2,x_2=sp.impulse(H_2,None,t)
subplot(3,1,3).plot(t,x_2)
title("Time Response")
xlabel(r'time ' '$\longrightarrow$')
ylabel(r'Output' '$\longrightarrow$')

suptitle("Plots for Problem_2")

################################ 3 ~~~~~~~~~~~~

freq=arange(1.4,1.6,0.05)
freq=list(freq)
a=0.05
col=["y","b","g","orange","m"]
H_3=sp.lti(array([1]),array([1,0,2.25]))
figure(3)
for i in freq:
	t_3,x_3,svec=sp.lsim(H_3,input(i,t),t)
	plot(t,x_3,label="\u03C9 = "+str(i),color=col[freq.index(i)])#
	
title("Plots for Problem_3")
legend(loc="upper right")
xlabel(r'time ' '$\longrightarrow$')
ylabel(r'Output' '$\longrightarrow$')

#s=trans(a,1.5)
#H_3=sp.lti(array([1]),s[3])

#t_3,x_3,svec=sp.lsim(H_3,None,t)
#plot(t,x_3,label="\u03C9 = "+str(freq))



################################ 4 ~~~~~~~~~~~~
t=linspace(0,20,20001)

num_x=array([1,0,2,0])
den_x=polyadd( polymul(array([1,0,2]),array([1,0,1])) , array([-2]))
X=sp.lti(num_x,den_x)


num_y=polymul(num_x,array([2]))
den_y=polymul(den_x,array([1,0,2]))
Y=sp.lti(num_y,den_y)

t_x,x=sp.impulse(X,None,t)
t_y,y=sp.impulse(Y,None,t)
figure(4)
plot(t,x,label="x(t)")
plot(t,y,label="y(t)",color='orange')
title('Plot of x(t) and y(t)')
legend(loc="upper right")
suptitle("Plots for Problem_4")
xlabel(r'time ' '$\longrightarrow$')
ylabel(r'Position of particle ' '$\longrightarrow$')

################################ 5 ~~~~~~~~~~~~
R=100
L=1e-6
C=1e-6

num=array([1])
den=array([L*C,R*C,1])
H_5=sp.lti(num,den)
w_5,S_5,phi_5=sp.bode(H_5) # w=r

subplots(2,1)

subplot(2,1,1).semilogx(w_5,S_5,color='orange')
title("Magnitude Plot")
xlabel(r'frequency ' '$\longrightarrow$')
ylabel(r'$H_{db}$' '$\longrightarrow$')

subplot(2,1,2).semilogx(w_5,phi_5,color='g')
title("Phase Plot")
xlabel(r'frequency ' '$\longrightarrow$')
ylabel(r'$H_{phase}$' '$\longrightarrow$')
suptitle("Plots for Problem_5")

################################ 6 ~~~~~~~~~~~~
figure(6)
t=linspace(0,10e-3,20001)
u=cos((1e3)*t)-cos((1e6)*t)
t,y,svec=sp.lsim(H_5,u,t)
title("Plot for Problem_6 : Output of the system in Problem_5")
plot(t,y)
xlabel(r'time ' '$\longrightarrow$')
ylabel(r'Output' '$\longrightarrow$')




################################

show()
