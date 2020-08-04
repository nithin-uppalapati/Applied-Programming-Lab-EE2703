from pylab import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
rcParams['axes.grid']=True
# N=2**8
# w_0=0.86
# t=linspace(-4*pi,4*pi,N+1);t=t[:-1]
# dt=t[1]-t[0];fmax=1/dt
# n=arange(N)
# wnd=fftshift(0.54+0.46*cos(2*pi*n/(N-1)))
# y=cos(w_0*t)**3
# y[0]=0
# Y=fftshift(fft(y))/N
# w=linspace(-pi*fmax,pi*fmax,N+1);w=w[:-1]
# figure()
# subplot(2,1,1)
# plot(w,abs(Y),'bo-')
# xlim([-5,5])
# ylabel(r"$|Y|$",size=16)
# title(r"Spectrum of $cos^3(W_0t)$")
# subplot(2,1,2)
# plot(w,angle(Y),'ro')
# xlim([-4,4])
# ylabel(r"Phase of $Y$",size=16)
# xlabel(r"$\omega$",size=16)
# ----windowing----
# y=(cos(w_0*t)**3)*wnd
# y[0]=0
# y=fftshift(y)
# Y=fftshift(fft(y))/N
# w=linspace(-pi*fmax,pi*fmax,N+1);w=w[:-1]
# figure()
# subplot(2,1,1)
# plot(w,abs(Y),'bo-')
# xlim([-5,5])
# ylabel(r"$|Y|$",size=16)
# title(r"Spectrum of $cos(W_0t)*w(t)$")
# subplot(2,1,2)
# plot(w,angle(Y),'ro')
# xlim([-5,5])
# ylabel(r"Phase of $Y$",size=16)
# xlabel(r"$\omega$",size=16)
# -----Problem 2-----
w0=0.84
delta=0.9
N=128
n=arange(N)
wnd_2=fftshift(0.54+0.46*cos(2*pi*n/N-1))
t=linspace(-pi,pi,N+1);t=t[:-1]
dt=t[1]-t[0];fmax=1/dt
w=linspace(-pi*fmax,pi*fmax,N+1);w=w[:-1]
y_2=cos(w0*t+delta)*wnd_2
y_2[0]=0
figure()
plot(t,y_2)
Y_2=fftshift(fft(y_2)/N)
figure()
subplot(2,1,1)
xlim([-4,4])
plot(w,abs(Y_2))
subplot(2,1,2)
xlim([-4,4])
plot(w,angle(Y_2),'ro')
w_2p = sum(abs(Y_2**1.7*w))/sum(abs(Y_2)**1.7)
del_p=angle(Y_2[::-1][argmax(abs(Y_2[::-1]))])
if del_p>=0:
	del_p=pi-del_p
else:
	del_p=pi+del_p
print('Actual Values : W={} Delta={}'.format(w0,delta))
print('Predicted Values : W= {} Delta= {}'.format(w_2p,del_p))
#-----Problem 3-----
y_3=y_2+0.1*randn(N)
Y_3=fftshift(fft(y_3)/N)
w_2p = sum(abs(Y_3**2.4*w))/sum(abs(Y_3)**2.4)
del_p=angle(Y_2[argmax(abs(Y_3))])
if del_p>=0:
	del_p=pi-del_p
else:
	del_p=pi+del_p
print('Predicted Values With Noise : W= {} Delta= {}'.format(w_2p,del_p))
#-----Problem 4-----
N=2**10
t=linspace(-pi,pi,N+1);t=t[:-1]
dt=t[1]-t[0];fmax=1/dt
y_4=cos(16*t*(1.5+t/(2*pi)))
y_4[0]=0
y_4=fftshift(y_4)
Y_4=fftshift(fft(y_4))/N
w=linspace(-pi*fmax,pi*fmax,N+1);w=w[:-1]
figure()
subplot(2,1,1)
plot(w,abs(Y_4),color='green')
xlim([-100,100])
subplot(2,1,2)
plot(w,angle(Y_4),'ro')
xlim([-100,100])
# -----Problem 5-----
Y=[]
for i in range(16):
	tlim_1= -pi + 2*pi*i/16
	tlim_2= -pi + 2*pi*(i+1)/16
	t=linspace(tlim_1,tlim_2,65);t=t[:-1]
	y=cos(16*t*(1.5+t/(2*pi)))
	y[0]=0
	Y.append((fftshift(fft(y))/64))

Yd=array(Y)
t1=linspace(-pi,pi,16)
w=linspace(-pi*fmax/2,pi*fmax/2,65);w=w[:-1]
t1 , w= meshgrid(t1,w)
ax= Axes3D(figure())
surf = ax.plot_surface(t1,w,abs(Yd).T, rstride=1, cstride=1, cmap='viridis')
xlabel('t')
ylabel('w')
show()
