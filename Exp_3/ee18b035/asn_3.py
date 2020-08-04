from pylab import *
import scipy.special as sp
from scipy.linalg import lstsq

A=1.05
B=-0.105
def g(t,A,B):  		# also see func_val=c_[sp.jn(2,t),t]
	y=(A*sp.jn(2,t))+B*t
	return y


f=open("fitting.dat")
dat=f.readlines()
N=len(dat)							# N=101, in the fit.data
k=len(dat[0].strip().split(' '))	#A=1.05
data=array([zeros(k)]*N)			#B=-0.105

for i in range(0,N):
	dat[i]=dat[i].strip()
	dat[i]=dat[i].split(' ')
	for j in range(0,k):
		data[i][j]=float(dat[i][j])
t=data[:,0]
y=g(t,A,B)
temp=data[:,1:]
y_data=array([zeros(N)]*(k-1))
stdev=array(zeros(k-1))
for i in range(0,k-1):
	y_data[i]=data[:,i+1]
	stdev[i]=std(g(t,A,B)-y_data[i]) ###  A Doubt here, shall i take the std for entire reading or the every 5th sample?
	
func_val=c_[sp.jn(2,t),t]  # same as g(t,A,B)
A_guess=linspace(0,2,21)
B_guess=linspace(-0.2,0,21)
appx_err_val=array([zeros(21)]*21)

for i in range(0,21):
	for j in range(0,21):
		appx_err_val[i][j] = (square( y_data[0]-g(t,A_guess[i],B_guess[j]) )).mean()

###########			plotting the outputs			##########

figure(0)
grid(True)
plot(t,g(t,A,B))
plot(t,temp)
xlabel(r'$t$',size=20)
ylabel(r'$f(t)+n$',size=20)
title(r'Plot of the data to be fitted')
grid(True)
#plot()


figure(1)
grid(True)
#subplots(3, 3, sharex='col')
errorbar(t[::5],y_data[0][::5],label="Errorbars",yerr=stdev[0],fmt="ro")
plot(t,y,label= "Exact function")
legend(loc="upper right")
xlabel(r'$t$' ' ' '$\longrightarrow$',size=15)
#ylabel(r'$f(t)+n$''$\longrightarrow$',size=15)
string=str(stdev[0])
string=string[0:5]
title("Data points for \u03C3="+string+" along with exact function")


figure(2)

scatter(A,B,color='red')
annotate('Exact Value',(A,B),color='blue')
cp = plt.contour(A_guess, B_guess, appx_err_val, linestyles='-')
clabel(cp, inline=True,fontsize=10)
xlabel('A  ''$\longrightarrow$',size=15)
ylabel('B  ''$\longrightarrow$',size=15)
title(r'Contour plot of ''$ε_{ij}$')

coeff=array([zeros(k-1)]*(2))
for i in range(0,k-1):
	p,resid,rank,sig=lstsq(func_val,y_data[i])
	coeff[0][i]=p[0]
	coeff[1][i]=p[1]

figure(3)
grid(True)
#######		'-', '--', '-.', ':', 'solid', 'dashed', 'dashdot', 'dotted'
plot(stdev,abs(A-coeff[0]),color='red',label= 'Aerr', marker='o', linestyle='--',linewidth=0.9)
plot(stdev,abs(B-coeff[1]),color='blue',label= 'Berr',marker='o', linestyle='--',linewidth=0.9)
xlabel('noise standard deviation  ''$\longrightarrow$',size=15)
ylabel('A and B error  ''$\longrightarrow$',size=15)
legend(loc="upper left")
title('Variation of error with noise__linear plot')

figure(4)
errorbar(stdev,abs(A-coeff[0]),yerr=stdev ,color='red', marker='o',linestyle=' ')
loglog(stdev,abs(A-coeff[0]) , label= 'A_err',color='red', marker='o',linestyle=' ')
errorbar(stdev,abs(B-coeff[1]),yerr=stdev ,color='blue', marker='o',linestyle=' ')
loglog(stdev,abs(B-coeff[1]), label= 'B_err',color='blue', marker='o',linestyle=' ')
xlabel('$\u03C3_n$' '  ' '$\longrightarrow$',size=15)
ylabel('A and B error  ''$\longrightarrow$',size=15)
title(r'Variation of error with noise__log plot')
legend(loc="upper left")
yscale('log', nonposy='clip')
xscale('log', nonposx='clip')

show()
