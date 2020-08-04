from scipy.integrate import *
from scipy.linalg import lstsq
from pylab import *

def f_1(t):		return exp(t)
def f_2(t):		return cos(cos(t))
def u_1(x,k):	return cos(k*x)*f_1(x)
def u_2(x,k):	return cos(k*x)*f_2(x)
def v_1(x,k):	return sin(k*x)*f_1(x)
def v_2(x,k):	return sin(k*x)*f_2(x)


####################### finding fourier coefficients

coeff_1=zeros(51)
coeff_2=zeros(51)

for i in range(0,26):
	if i:
		coeff_1[2*i-1]=(quad(u_1,0,2*pi,args=(i))[0])*(1/pi)
		coeff_2[2*i-1]=(quad(u_2,0,2*pi,args=(i))[0])*(1/pi)
		coeff_1[2*i]=(quad(v_1,0,2*pi,args=(i))[0])*(1/pi)
		coeff_2[2*i]=(quad(v_2,0,2*pi,args=(i))[0])*(1/pi)
	else:
		coeff_1[0]=(quad(u_1,0,2*pi,args=(0))[0])*(0.5/pi)
		coeff_2[0]=(quad(u_2,0,2*pi,args=(0))[0])*(0.5/pi)
		
####################### fitting the functions

x=linspace(0,2*pi,401)
A=zeros((400,51))
A[:,0]=1
x=x[:-1]
b_1=f_1(x)
b_2=f_2(x)
for k in range(1,26):
	A[:,2*k-1]=cos(k*x)
	A[:,2*k]=sin(k*x)

p_coeff_1=lstsq(A,b_1,rcond=-1)[0]
p_coeff_2=lstsq(A,b_2,rcond=-1)[0]

######################## plotting graphs
t=linspace(-4,2,700)*pi
x_axis=linspace(0,50,51)
x_axis_=linspace(1,25,25)
x_point=linspace(0,0,1)
figure(1)
grid(True)
title('$e^{t}$'  ' along with the fitting model' )
semilogy(t,f_1(t),color='orange',label= 'Exact function')
semilogy(x,matmul(A,p_coeff_1),color='green',label= 'fitting to the data')
legend(loc="upper right")
ylabel('$e^{t}$' '$\longrightarrow$')
xlabel('t ' '$\longrightarrow$')


figure(2)
title('$cos(cos({t}))$'  ' along with the fitting model')
plot(t,f_2(t),color='orange',label= 'Exact function')
plot(x,matmul(A,p_coeff_2),color='green',label= 'fitting to the data')
legend(loc="upper right")
ylabel('$cos(cos({t}))$' '$\longrightarrow$')
xlabel('t ' '$\longrightarrow$')


figure(3)
title('coefficients of ' '$e^{t}$' ' by Fourier and Least Square method__semilogy')
grid(True)
#semilogy(x_axis,coeff_1,color='orange',label= 'Fourier', marker='o', linestyle='')
#semilogy(x_axis,p_coeff_1,color='green',label= 'Lstsq', marker='o', linestyle='',markersize='5')

semilogy(x_axis_,coeff_1[1::2],color='orange',label= '$a_n$', marker='o', linestyle='')
semilogy(x_point,coeff_1[0],color='orange', marker='o', linestyle='')
semilogy(x_axis_,abs(coeff_1[2::2]),color='blue',label= '$b_n$', marker='o', linestyle='',markersize='5')
#semilogy(x_axis,abs(p_coeff_1),color='green',label= 'Lstsq', marker='o', linestyle='')

semilogy(x_axis_,abs(p_coeff_1[1::2]),color='red', marker='o', linestyle='',markersize='3')
semilogy(x_point,abs(p_coeff_1[0]),color='red', marker='o', linestyle='',markersize='3')
semilogy(x_axis_,abs(p_coeff_1[2::2]),color='red',label= 'lstsq', marker='o', linestyle='',markersize='3')

legend(loc="upper right")
ylabel('$e^{t}$' '$\longrightarrow$')
xlabel('n ' '$\longrightarrow$')

figure(4)
title('coefficients of ' '$e^{t}$' ' by Fourier and Least Square method__loglog')
grid(True)
#loglog(x_axis,coeff_1,color='orange',label= 'Fourier', marker='o', linestyle='')
#loglog(x_axis,p_coeff_1,color='green',label= 'Lstsq', marker='o', linestyle='')
loglog(x_axis_,coeff_1[1::2],color='orange',label= '$a_n$', marker='o', linestyle='')
loglog(x_point,coeff_1[0],color='orange', marker='o', linestyle='')
loglog(x_axis_,abs(coeff_1[2::2]),color='blue',label= '$b_n$', marker='o', linestyle='',markersize='5')

loglog(x_axis_,abs(p_coeff_1[1::2]),color='red', marker='o', linestyle='',markersize='3')
loglog(x_point,abs(p_coeff_1[0]),color='red', marker='o', linestyle='',markersize='3')
loglog(x_axis_,abs(p_coeff_1[2::2]),color='red',label= 'lstsq', marker='o', linestyle='',markersize='3')

legend(loc="upper right")
ylabel('$e^{t}$' '$\longrightarrow$')
xlabel('n ' '$\longrightarrow$')


figure(5)
title('coefficients of ' '$cos(cos({t}))$' 'by Fourier and Least Square method__semilogy')
grid(True)
ylabel('$cos(cos({t}))$' '$\longrightarrow$')
xlabel('n ' '$\longrightarrow$')
#semilogy(x_axis,coeff_2,color='orange',label= 'Fourier', marker='o', linestyle='')
#semilogy(x_axis,p_coeff_2,color='green',label= 'Lstsq', marker='o', linestyle='')
semilogy(x_axis_,coeff_2[1::2],color='orange',label= '$a_n$', marker='o', linestyle='')
semilogy(x_point,coeff_2[0],color='orange', marker='o', linestyle='')
semilogy(x_axis_,abs(coeff_2[2::2]),color='blue',label= '$b_n$', marker='o', linestyle='',markersize='5')

semilogy(x_axis_,abs(p_coeff_2[1::2]),color='red', marker='o', linestyle='',markersize='3')
semilogy(x_point,abs(p_coeff_2[0]),color='red', marker='o', linestyle='',markersize='3')
semilogy(x_axis_,abs(p_coeff_2[2::2]),color='red',label= 'lstsq', marker='o', linestyle='',markersize='3')
legend(loc="upper right")


figure(6)
grid(True)
title('coefficients of ' '$cos(cos({t}))$' 'by Fourier and Least Square method__loglog')
#loglog(x_axis,coeff_2,color='orange',label= 'Fourier', marker='o', linestyle='')
#loglog(x_axis,p_coeff_2,color='green',label= 'Lstsq', marker='o', linestyle='')
loglog(x_axis_,coeff_2[1::2],color='orange',label= '$a_n$', marker='o', linestyle='')
loglog(x_point,coeff_2[0],color='orange', marker='o', linestyle='')
loglog(x_axis_,abs(coeff_2[2::2]),color='blue',label= '$b_n$', marker='o', linestyle='',markersize='5')

loglog(x_axis_,abs(p_coeff_2[1::2]),color='red', marker='o', linestyle='',markersize='3')
loglog(x_point,abs(p_coeff_2[0]),color='red', marker='o', linestyle='',markersize='3')
loglog(x_axis_,abs(p_coeff_2[2::2]),color='red',label= 'lstsq', marker='o', linestyle='',markersize='3')

legend(loc="upper right")
ylabel('$cos(cos({t}))$' '$\longrightarrow$')
xlabel('n ' '$\longrightarrow$')


########### finding the deviation of coefficients

figure(7)
grid(True)
title('Deviation of lstsq coeff. with fourier coeff.')
plot(x_axis, abs(coeff_1-p_coeff_1), color='red', label=  'deviation for ' '$e^{t}$', marker='o', linestyle='')
plot(x_axis, abs(coeff_2-p_coeff_2),color='blue', label= 'deviation for ' '$cos(cos({t}))$', marker='o', linestyle='')
legend(loc="center right")
ylabel('$(fourier\_coeff.) - (lstsq\_coeff.)$' '$\longrightarrow$')
xlabel('n ' '$\longrightarrow$')

show()

print("The largest deviation in the coeff. for e^{t} is ",amax(abs(coeff_1-p_coeff_1)))
print("The largest deviation in the coeff. for cos(cos({t}))$ is ",amax(abs(coeff_2-p_coeff_2)))

#figure(8)
#grid(True)
#title('Deviation of lstsq coeff. with fourier coeff. for ' '$cos(cos({t}))$')
#plot(x_axis, abs(coeff_2-p_coeff_2),color='brown', marker='o', linestyle='')
#ylabel('(fourier coeff.) - (lstsq coeff.) ' '$\longrightarrow$')
#xlabel('n ' '$\longrightarrow$')

#print(coeff_1,p_coeff_1)
#print(len(p_coeff_1))
#
#print(len(p_coeff_2))
