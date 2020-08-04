from __future__ import division
from sympy import *
import pylab as p
import scipy.signal as sp


#def sym_to_lti(c):
#	s=c.free_symbols
#	c=simplify(c).as_numer_denom()
#	s=list(s)
#	s=s[0]
#	num=c[0]
#	den=c[1]
#	n=[]
#	d=[]
#	for i in p.arange(0,degree(num)+1):
#		a=div(num,s)
#		num=a[0]
#		n.append(a[1])
#	for i in p.arange(0,degree(den)+1):
#		b=div(den,s)
#		den=b[0]
#		d.append(b[1])
#
#	n.reverse()
#	d.reverse()
#	n=p.array(n, dtype=float)
#	d=p.array(d, dtype=float)
#	y=sp.lti(n,d)
#	return [n,d]

def sympy_to_lti(xpr, s=Symbol('s')):
	""" Convert Sympy transfer function polynomial to Scipy LTI """
	num, den = simplify(xpr).as_numer_denom()  # expressions
	p_num_den = poly(num, s), poly(den, s)  # polynomials
	c_num_den = [expand(p).all_coeffs() for p in p_num_den]  # coefficients
	l_num, l_den = [lambdify((), c)() for c in c_num_den]  # convert to floats
	return sp.lti(l_num, l_den)

#init_printing(use_unicode=True)

def lowpass(R1,R2,C1,C2,G,Vi):
	s=symbols("s")
	A=Matrix([ [0,0,1,-1/G], [-1/(1+s*R2*C2),1,0,0] , [0,-1*G,G,1], [(-1/R1)-(1/R2)-(s*C1),1/R2,0,s*C1] ])
	b=Matrix([0,0,0,Vi/R1])
	V=A.inv()*b
	return (A,b,V)
	
def highpass(R1,R3,C1,C2,G,Vi):
	s=symbols("s")
	A=Matrix([ [1,-G,0,0] ,[-1,-G,G,0] ,[0,0,s*C2+(1/R3),-C2*s] ,[-1/R1,0,-C2*s,s*(C1+C2)+1/R1] ])
	B=Matrix([0,0,0,s*C1*Vi])
	V=A.inv()*B
	return (A,B,V)


s=symbols("s")

###~~~~~~~~1~~~~~~~~###
A,b,V=lowpass(10000,10000,1e-11,1e-11,1.586,1)
Vo=V[3]
ww=p.logspace(0,8,801)
ss=1j*ww
hf=lambdify(s,Vo,'numpy')
v=hf(ss)
p.figure(0)
p.title("Transfer function of the circuit from sympy")
p.loglog(ww,abs(v),lw=2)
p.grid(True)



Y=sympy_to_lti(Vo)
t=p.linspace(0,10,10000)

p.figure(1)
p.title("Plots for Problem_1, step response")

#t,y=sp.step(Y,None,t)
t,y=sp.impulse(Y,None,t)

p.plot(y,t)



###~~~~~~~~2~~~~~~~~###
w_1=2e3*p.pi
w_2=2e6*p.pi
vin=(w_1/(s**2+w_1**2))*(s/(s**2+w_2**2))

a_1,b_1,V_1=highpass(10000,10000,1e-9,1e-9,1.586,vin)
V1=V_1[0]
ww=p.logspace(0,8,801)
ss=1j*ww
hf=lambdify(s,V1,'numpy')
v=hf(ss)

print(V_1)
Y=sympy_to_lti(V1)
t=p.linspace(30,30.07,100000)

p.figure(2)
p.title("Plots for Problem_2")
u= p.sin(w_1*t)+p.cos(w_2*t)
t,y,svec=sp.lsim(Y,u,t)
#t,y=sp.impulse(Y,None,t)
#p.plot(t,u,color='g')
p.plot(t,y,color='orange')
#________





########## test for the defined function
#Y=sym_to_lti(Vo)
#print(Y[0])
#print(Y[1])
#print(type(Y[1]))
########## endtest


#print(type(H))





####~~~~~~~~~3~~~~~~~~~

p.figure(3)
p.title("Transfer function of the circuit for pro_2")
#p.loglog(ww,abs(v),lw=2)
a,b,c=Y.bode()
p.semilogx(a,b,color='g')


####~~~~~~~~~4~~~~~~~~~

p.figure(4)

a_4,b_4,V_4=highpass(10000,10000,1e-9,1e-9,1.586,1)
V_4=V_4[0]
V_4=sympy_to_lti(V_4)
a=0.5 #damping factor
u= p.sin(w_1*t)*p.exp(-a*t)
t,y_4,svec=sp.lsim(V_4,u,t)

p.title("Response of the circuit to a damped sinusoid")
p.plot(t,y_4)


####~~~~~~~~~5~~~~~~~~~

p.figure(5)

p.title("Response of the circuit to a unit step")
t=p.linspace(0,30.07,100000)

a_5,b_5,V_5=highpass(10000,10000,1e-9,1e-9,1.586,1/s)
V_5=V_5[0]
Y_5=sympy_to_lti(V_5)

t,y_5=sp.impulse(Y_5,None,t)
p.plot(t,y_5)


p.show()


