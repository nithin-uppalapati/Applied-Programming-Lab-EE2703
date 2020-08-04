from pylab import *
import mpl_toolkits.mplot3d.axes3d as p3
import sys

#print(sys.argv.count('poissionseq.py'))

def e(x,A,B): return A*exp(B*x);

Niter=1500	#number of iterations to perform

if len(sys.argv)==1:
	Nx=25   		#size along x
	Ny=25 			# size along y
	radius=8 	#radius of central lead
	Niter=1500	#number of iterations to perform

else:
#print("Enter the value for Nx")
#Nx=int(input())
#print("Enter the value for Ny")
#Ny=int(input())
	Nx=int(sys.argv[1])
	Ny=int(sys.argv[2])
	radius=int(sys.argv[3])
	Niter=int(sys.argv[4])
#	radius=0.3*min(Nx,Ny)
	

phi = array([zeros(Ny)]*Nx)
j_x = array([zeros(Ny)]*Nx)
j_y = array([zeros(Ny)]*Nx)

x=linspace(-int(Nx/2),int(Nx/2),Nx)
y=linspace(int(Ny/2),-int(Ny/2),Ny)

Y,X=meshgrid(y,x)

ii=where((X*X+Y*Y)<=(radius**2))			#extracting the points where radius< ~8
phi[ii]=1.0
oldphi=phi.copy()


errors=zeros(Niter)

samples=array([zeros(2)]*Niter)
samples[:,0]=1
iter=arange(1,Niter+1,1)
samples[:,1]=iter


for i in range(0,Niter):
	oldphi=phi.copy()
	phi[1:-1,1:-1]=0.25*(phi[1:-1,0:-2] + phi[1:-1,2:] + phi[0:-2,1:-1] +  phi[2:,1:-1])#calculating phi and errors
	phi[ii]=1.0
	phi[-1]=0
	phi[1:-1,0]=phi[1:-1,1]										#asserting boundary conditions
	phi[1:-1,-1]=phi[1:-1,-2]
	phi[0]=phi[1]
	errors[i]=(abs(phi-oldphi)).max()



err_coeff=lstsq( samples , log(errors) ,rcond=-1)[0]
A=exp(err_coeff[0])
B=err_coeff[1]

err_coeff_500=lstsq( samples[500:] , log(errors[500:]) ,rcond=-1)[0]
A_500=exp(err_coeff[0])
B_500=err_coeff_500[1]


j_x[:,1:-1]=0.5*(phi[:,0:-2]-phi[:,2:])
j_y[1:-1,:]=0.5*(-phi[0:-2,:]+phi[2:,:])					###calculating currrent density
j_y[-1]=(-phi[-2])



n=arange(0,Niter,50)

										####plotting graphs


figure(0)
title('Semilog plot of errors with no. of Iterations')
semilogy(n,errors[::50],color='blue',label= 'Errors') #, marker='o', linestyle=''
semilogy(n,e(n,A,B),color='green',label= 'Fit of Errors', marker='o', linestyle='') #, marker='o', linestyle=''
xlabel(r'$N_{iter}$' ' ' '$\longrightarrow$',size=15)
#legend(loc="upper right")

#figure(1)
#title('Semilog plot of errors with no. of Iterations after 500')
#semilogy(n[10:],errors[500::50],color='blue',label= 'Errors') #, marker='o', linestyle=''
semilogy(n,e(n,A_500,B_500),color='orange',label= 'Fit of Errors after 500',markersize=3, marker='o', linestyle='') #, marker='o', linestyle=''
#xlabel(r'$N_{iter}$' ' ' '$\longrightarrow$',size=15)
legend(loc="upper right")


figure(2)
title('Loglog plot of errors with no. of iterations')
loglog(n,errors[n],color='blue',label= 'Errors')
loglog(n,e(n,A,B),color='green',label= 'Fit of Errors', marker='o', linestyle='') #, marker='o', linestyle=''
xlabel(r'$N_{iter}$' ' ' '$\longrightarrow$',size=15)
#legend(loc="upper right")

#figure(3)
#title('Loglog plot of errors with no. of iterations  after 500')
#loglog(n,errors[n],color='green',label= 'Errors', marker='o', linestyle='')
loglog(n,e(n,A_500,B_500),color='orange',label= 'Fit of Errors after 500',markersize=3 , marker='o', linestyle='') #, marker='o', linestyle=''
#xlabel(r'$N_{iter}$' ' ' '$\longrightarrow$',size=15)
legend(loc="upper right")

fig4=figure(4) # open a new figure
ax=p3.Axes3D(fig4) # Axes3D is the means to do a surface plot
title('The 3-D surface plot of the potential')
surf = ax.plot_surface(-Y, -X, phi, rstride=1, cstride=1, cmap=cm.jet)

figure(5)
cp = plt.contour(Y, -X, phi, linestyles='-')
clabel(cp, inline=True,fontsize=10)
xlabel('Ground',size=15)
title(r'Contour plot of $V_{ij}$ ' )

figure(6)
title('Vector plot of Current Density')
q=quiver(-y,-x,j_x,j_y, scale=1.2, scale_units='inches',label="J - Vectors")
scatter(X[ii],Y[ii],color='red',label="1 Volt Region")
legend(loc="upper right")
show()


#print(errors[::50])
#print(phi)
