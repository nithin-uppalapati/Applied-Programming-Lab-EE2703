from scipy.linalg import lstsq
from pylab import *

def f_1(s,z,w):
	s=1j*s
	v=abs(s**2+2*z*w*s+w**2)
	v=(w**2)/v
	v=20*log10(v)
	return v
	
def f_2(s,a):
	s=1j*s
	v=abs(s+a)
	v=1/v
	v=20*log10(v)
	return v
	
def f_3(s,a):
	s=1j*s
	v=abs(a**2+s**2)
	v=1/v
	v=20*log10(v)
	return v

def u_1(x,k):	return cos(k*x)*f_1(x)
def u_2(x,k):	return cos(k*x)*f_2(x)
def v_1(x,k):	return sin(k*x)*f_1(x)
def v_2(x,k):	return sin(k*x)*f_2(x)

n=5
a=20
s=logspace(0,n,10000)
z=1
w=100


figure(1)
grid(True)
title('Bode plot' )
plot(s,f_1(s,z,w),color='orange',label= 'Exact function')
z=0.2
w=100
plot(s,f_1(s,z,w),color='blue',label= 'Exact function')
z=5
w=100
plot(s,f_1(s,z,w),color='green',label= 'Exact function')
xscale('log')
z=0
w=100
plot(s,f_1(s,z,w),color='green',label= 'Exact function')
xscale('log')

figure(2)
for i in range(1,11):
	z=1/i
	plot(s,f_1(s,z,w),color='green',label= 'Exact function')
	xscale('log')
show()
#z=0.2
#w=100
#
#figure(2)
#grid(True)
#title('Bode plot' )
#plot(s,f_1(s,z,w),color='orange',label= 'Exact function')
#xscale('log')
#
#
#z=5
#w=100
#
#figure(3)
#grid(True)
#title('Bode plot' )
#plot(s,f_1(s,z,w),color='orange',label= 'Exact function')
#xscale('log')
#show()
#legend(loc="upper right")
#ylabel('$e^{t}$' '$\longrightarrow$')
#xlabel('t ' '$\longrightarrow$')

#
#figure(2)
#title('$cos(cos({t}))$'  ' along with the fitting model')
#plot(t,f_2(t),color='orange',label= 'Exact function')
#plot(x,matmul(A,p_coeff_2),color='green',label= 'fitting to the data')
#legend(loc="upper right")
#ylabel('$cos(cos({t}))$' '$\longrightarrow$')
#xlabel('t ' '$\longrightarrow$')
#
#
#figure(3)
#title('coefficients of ' '$e^{t}$' ' by Fourier and Least Square method__semilogy')
#grid(True)
#semilogy(x_axis,coeff_1,color='orange',label= 'Fourier', marker='o', linestyle='')
#semilogy(x_axis,p_coeff_1,color='green',label= 'Lstsq', marker='o', linestyle='')
#legend(loc="upper right")
#ylabel('$e^{t}$' '$\longrightarrow$')
#xlabel('t ' '$\longrightarrow$')
#
#figure(4)
#title('coefficients of ' '$e^{t}$' ' by Fourier and Least Square method__loglog')
#grid(True)
#loglog(x_axis,coeff_1,color='orange',label= 'Fourier', marker='o', linestyle='')
#loglog(x_axis,p_coeff_1,color='green',label= 'Lstsq', marker='o', linestyle='')
#legend(loc="upper right")
#ylabel('$e^{t}$' '$\longrightarrow$')
#xlabel('n ' '$\longrightarrow$')
#
#
#figure(5)
#title('coefficients of ' '$cos(cos({t}))$' 'by Fourier and Least Square method__semilogy')
#grid(True)
#ylabel('$cos(cos({t}))$' '$\longrightarrow$')
#xlabel('t ' '$\longrightarrow$')
#semilogy(x_axis,coeff_2,color='orange',label= 'Fourier', marker='o', linestyle='')
#semilogy(x_axis,p_coeff_2,color='green',label= 'Lstsq', marker='o', linestyle='')
#legend(loc="upper right")
#
#
#figure(6)
#grid(True)
#title('coefficients of ' '$cos(cos({t}))$' 'by Fourier and Least Square method__loglog')
#loglog(x_axis,coeff_2,color='orange',label= 'Fourier', marker='o', linestyle='')
#loglog(x_axis,p_coeff_2,color='green',label= 'Lstsq', marker='o', linestyle='')
#legend(loc="upper right")
#ylabel('$cos(cos({t}))$' '$\longrightarrow$')
#xlabel('n ' '$\longrightarrow$')
#
#
############ finding the deviation of coefficients
#
#figure(7)
#grid(True)
#title('Deviation of lstsq coeff. with fourier coeff.')
#plot(x_axis, abs(coeff_1-p_coeff_1), color='red', label=  'deviation for ' '$e^{t}$', marker='o', linestyle='')
#plot(x_axis, abs(coeff_2-p_coeff_2),color='blue', label= 'deviation for ' '$cos(cos({t}))$', marker='o', linestyle='')
#legend(loc="center right")
#ylabel('$(fourier\_coeff.) - (lstsq\_coeff.)$' '$\longrightarrow$')
#xlabel('n ' '$\longrightarrow$')
#
#show()
#
#print("The largest deviation in the coeff. for e^{t} is ",amax(abs(coeff_1-p_coeff_1)))
#print("The largest deviation in the coeff. for cos(cos({t}))$ is ",amax(abs(coeff_2-p_coeff_2)))

#figure(8)
#grid(True)
#title('Deviation of lstsq coeff. with fourier coeff. for ' '$cos(cos({t}))$')
#plot(x_axis, abs(coeff_2-p_coeff_2),color='brown', marker='o', linestyle='')
#ylabel('(fourier coeff.) - (lstsq coeff.) ' '$\longrightarrow$')
#xlabel('n ' '$\longrightarrow$')

#print(coeff_1,p_coeff_1)
