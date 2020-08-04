from pylab import *
import numpy as np

####  D-dist. bw nodes       h-height of dielectric   ------- analog quantities ************
#k-index coeersponding to h
#d-accuracy
#n_0- actually carried out
#Niter-iterations to complete
# M- rows (vertical nodes)
# N- columns (horizontal nodes)

ans=input('Enter Y/N for default values: ')
if ans=='Y' or ans=='y':
	M=60
	N=60
	D = 5
	k = 15
	d=0.00000001
	Niter=10000000
elif ans=='N' or ans=='n':
    M=int(input("Number of nodes in y(M): "))
    N=int(input("Number of nodes in x(N): "))
    D=float(input("Width between two nodes "))
    k=int(input("Index height of liquid: "))
    d=float(input("Accuracy: "))
    Niter=int(input("Max number of iterations: "))
else:
    print('Invalid Input')
    quit()

##calc values based on the user inputs
Lx=D*(N-1)
Ly=D*(M-1)
h =Ly-k*D
#############

e_r = 2 #dielectric constant
eps=8.85e-12  ##  Electric permittivity of Free Space


def expo(x,A,B): return A*exp(B*x);

def pot(M,N,D,k,d,Niter):

	phi=array([zeros(N)]*M)
	phi[0]=1
	
	errore=ones(Niter+1) #np.
	n_0=0

	for i in range(1,Niter+1):
		if errore[i-1] >= (d) :
			oldphi=phi.copy()
			
			#calculating phi

			phi[1:-1,1:-1]=0.25*(phi[1:-1,0:-2] + phi[1:-1,2:] + phi[0:-2,1:-1] +  phi[2:,1:-1])
			phi[k,1:-1] = ( (e_r)*(phi[k+1,1:-1]) + phi[k-1,1:-1] )/(1+e_r)

			
			#asserting boundary conditions
			# how to assure that E field is perpendicular at walls...?
			
			phi[-1]=0
			phi[:,0]=0
			phi[:,-1]=0
			phi[0]=1

			#error
			
			errore[i]=(abs(phi-oldphi)).max()

			n_0=i+1
		
		else: break
	
	errore=errore[2:n_0]
	
	E_x=array([zeros(N)]*M)
	E_y=array([zeros(N)]*M)
	
	E_x[1:-1,1:-1]=0.5*(1/D)*(phi[1:-1,0:-2]-phi[1:-1,2:])
	E_y[1:-1,1:-1]=0.5*(1/D)*(phi[0:-2,1:-1]-phi[2:,1:-1])
	E_y[-1]=(phi[-2])*(1/D)
	E_x[:,0]=-1*phi[:,1]*(1/D)
	E_x[:,-1]=phi[:,-2]*(1/D)

	#calculation of charge:

	q_top=(sum(E_y[1]))*eps*D
	q_fluid= ((sum(E_x[k:,0])-(sum(E_x[k:,-1]))-(sum(E_y[-1]))))*eps*D
	return [phi,n_0,errore,E_x,E_y,q_top,q_fluid]
	


#### calling the function

x=pot(M,N,D,k,d,Niter)
phi  =  x[0]
Nit  =  x[1]
err  =  x[2]
E_x  =  x[3]
E_y  =  x[4]
q_top=  x[5]
q_fluid=x[6]

############ extrapolating error to infinity

samples=array([zeros(2)]*(Nit-2))
samples[:,0]=1
iter=arange(1,Nit-1,1)
samples[:,1]=iter

err_coeff_300=lstsq( samples[300:] , log(err[300:]) ,rcond=-1)[0]
A_300=exp(err_coeff_300[0])
B_300=err_coeff_300[1]



######### e-part in the question, in this case g=10 #################################


def charges(g): # g is the no. of divisions required

	points=linspace(M,0,g+1)
	points=points[1:-1].round()
	Q_TP  = zeros(g-1)
	Q_FL  = zeros(g-1)
	HEIGHT= zeros(g-1)

	for i in range(0,g-1):
		tmp=int(points[i])
		z=pot(M,N,D,tmp,d,Niter)
		Q_TP[i]  = z[5]
		Q_FL[i]  = z[6]
		HEIGHT[i]= Ly-tmp*D
		
	return [Q_TP,Q_FL,HEIGHT]
	




########## f-part ###  Proving that D_n is continuous at the centre of the tank #######

Ef_y1=E_y[k-1][int(N/2)]			###Finding D normal components on both sides
Ef_y2=E_y[k+1][int(N/2)]*e_r

Ef_x1=E_x[k-1][int(N/2)]			###Finding E parallel components on both sides
Ef_x2=E_x[k+1][int(N/2)]


print('The normal components of vector D',Ef_y1,Ef_y2,'\n','The parallel components of vector E',Ef_x1,Ef_x2,'\n')






########## g-part ###################################################

inci=arctan(E_x[k-1]/E_y[k-1])
refra=arctan(E_x[k+1]/E_y[k+1])

ratio=tan(inci)/tan(refra) 	###this should be approximately ~ 0.5 from the derived equation in report
diff=inci-refra


#######################    PLOTS    #######################################


y=linspace(0,M,M)
x=linspace(0,N,N)

figure(0)
title('Vector plot of E-Field and Potential')
q=quiver(x,-y,E_x,-E_y, scale=0.2, scale_units='inches',label="E - Vectors")


cp = plt.contour(x,-y, phi, linestyles='-')#,label="Potential Contours") ####here is the problem******************
clabel(cp, inline=True,fontsize=10)
xlabel('Ground',size=15)
title(r'Contour plot of $V_{ij}$ ' )
plot(x,linspace(-1*k,-1*k,N),color='orange', label="Dielectric Boundary")
legend(loc="lower center")




figure(1)
title('Errors with Iterations in semilogy')
n=arange(1,Nit-1,1)
semilogy(n,err,label="Error with each iteration")
semilogy(n,expo(n,A_300,B_300),label="Function fitted with Errors")
ylabel("Error"   '$\longrightarrow$')
xlabel("Iterations"   '$\longrightarrow$')
legend(loc="best")



#plot e part
g=charges(10)
H_funcoeff = polyfit(g[0],g[2],5)
H_func=poly1d(H_funcoeff)
H_est=H_func(g[0])
figure(2)
title('Q top vs h')
plot(g[2],g[0],'o',color='orange', label="q_top")
plot(H_est,g[0],':',color='green',label="q_top with polyfit")
xlabel("Height"   '$\longrightarrow$')
ylabel("Charge"   '$\longrightarrow$')
legend(loc="best")

figure(3)
title('Q fluid vs h')
plot(g[2],(g[1]),':',color='green', label="q_fluid")
plot(g[2],(g[1]),'o',color='green')
xlabel("Height"   '$\longrightarrow$')
ylabel("Charge"   '$\longrightarrow$')
legend(loc="best")


#inputs

show()


########## b-part ###################################################

#### estimation of h algorithm


#w=charges(40)
#
#H_funcoeff = polyfit(w[0],w[2],5)
#H_func=poly1d(H_funcoeff)

#L=100
#W=1
#C=1/(L*W*W)

#H_est=H_func(C)

##

######################################################################
