from pylab import *

##example 1
#n=(2**9)
#x=linspace(-4*pi,4*pi,n+1)
#x=x[:-1]
#y=sin(5*x)
#Y=fftshift(fft(y))/n
#w=linspace(-64,63,n)
#figure(0)
#subplot(2,1,1)
#xlim([-10,10])
#plot(w,abs(Y),lw=2)
#ylabel(r"$|Y|$",size=16)
#title(r"Spectrum of $\sin(5t)$")
#grid(True)
#
#subplot(2,1,2)
#xlim([-10,10])
#plot(w,angle(Y),marker='o',linestyle='',markersize=1,color='orange')
#
#ii=where(abs(Y)>1e-3)
#
#plot(w[ii],angle(Y[ii]),marker='o',linestyle='',color='g')
#ylabel(r"Phase of $Y$",size=16)
#xlabel(r"$k$",size=16)
#grid(True)
#
#
###example 2
#
#n=(2**9)
#x=linspace(-4*pi,4*pi,n+1)
#x=x[:-1]
#y=(1+0.1*cos(x))*cos(10*x)
#Y=fftshift(fft(y))/n
#w=linspace(-64,63,n)
#figure(1)
#subplot(2,1,1)
#xlim([-15,15])
#plot(w,abs(Y),lw=2)
#ylabel(r"$|Y|$",size=16)
#title(r"Spectrum of $cos(10x)(1+0.1cos(x))$")
#grid(True)
#
#subplot(2,1,2)
#xlim([-15,15])
#plot(w,angle(Y),marker='o',linestyle='',markersize=1,color='orange')
#
#ii=where(abs(Y)>1e-3)
#
#plot(w[ii],angle(Y[ii]),marker='o',linestyle='',color='g')
#ylabel(r"Phase of $Y$",size=16)
#xlabel(r"$k$",size=16)
#grid(True)
##
##figure()
##plot(abs(Y),color='g',lw=3)
##
#
#
#
#### spectrum of sin^3 (t)
#n=(2**7)
#x=linspace(0,2*pi,n+1)
#x=x[:-1]
#y=(sin(x))**3
#Y=fftshift(fft(y))/n
#w=linspace(-64,63,n)
#figure()
#subplot(2,1,1)
#xlim([-10,10])
#plot(w,abs(Y),lw=2)
#ylabel(r"$|Y|$",size=16)
#title(r"Spectrum of $(sin(t))^3$")
#grid(True)
#
#subplot(2,1,2)
#xlim([-10,10])
#plot(w,angle(Y),marker='o',linestyle='',markersize=1,color='orange')
#
#ii=where(abs(Y)>1e-3)
#
#plot(w[ii],angle(Y[ii]),marker='o',linestyle='',color='g')
#ylabel(r"Phase of $Y$",size=16)
#xlabel(r"$k$",size=16)
#grid(True)
#
#
#### spectrum of cos^3 (t)
#n=(2**7)
#x=linspace(0,2*pi,n+1)
#x=x[:-1]
#y=(cos(x))**3
#Y=fftshift(fft(y))/n
#w=linspace(-64,63,n)
#figure()
#subplot(2,1,1)
#xlim([-10,10])
#plot(w,abs(Y),lw=2)
#ylabel(r"$|Y|$",size=16)
#title(r"Spectrum of $(cos(t))^3$")
#grid(True)
#
#subplot(2,1,2)
#xlim([-10,10])
#plot(w,angle(Y),marker='o',linestyle='',markersize=1,color='orange')
#
#ii=where(abs(Y)>1e-3)
#
#plot(w[ii],angle(Y[ii]),marker='o',linestyle='',color='g')
#ylabel(r"Phase of $Y$",size=16)
#xlabel(r"$k$",size=16)
#grid(True)


### spectrum of cos(20t+5cos(t))
n=(2**10)
x=linspace(-8*pi,8*pi,n+1)
x=x[:-1]
y=cos(20*x+5*cos(x))
Y=fftshift(fft(y))/n
w=linspace(-64,63,n)
figure()
subplot(2,1,1)
xlim([-30,30])
plot(w,abs(Y),lw=2)
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of $cos(20t+5cos(t))$")
grid(True)

subplot(2,1,2)
xlim([-30,30])
plot(w,angle(Y),marker='o',linestyle='',markersize=1,color='orange')

ii=where(abs(Y)>1e-3)

plot(w[ii],angle(Y[ii]),marker='o',linestyle='',color='g')
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$k$",size=16)
grid(True)

### spectrum of exp(-t^2/2)
#n=(2**10)
#x=linspace(-8*pi,8*pi,n+1)
#x=x[:-1]
#y=exp(-1*(x**2)/2)
#Y=fftshift(fft(y))/n
#w=linspace(-64,63,n)
#figure()
#subplot(2,1,1)
#xlim([-20,20])
#plot(w,abs(Y),lw=2)
#ylabel(r"$|Y|$",size=16)
#title(r"Spectrum of $exp(-t^2/2)$")
#grid(True)
#
#subplot(2,1,2)
#xlim([-20,20])
#plot(w,angle(Y),marker='o',linestyle='',markersize=1,color='orange')
#
#ii=where(abs(Y)>1e-3)
#
#plot(w[ii],angle(Y[ii]),marker='o',linestyle='',color='g')
#ylabel(r"Phase of $Y$",size=16)
#xlabel(r"$k$",size=16)
#grid(True)

#print(ii)
show()
