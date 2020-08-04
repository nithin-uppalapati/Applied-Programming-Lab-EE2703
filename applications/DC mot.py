import pylab as p

x=p.linspace(10,100,100000)
n=len(x)



#for i in range(10,15):
c=p.array([10]*n)
y=c+1/(p.sqrt(x))


p.figure("Series")
p.plot(x,y)

p.title("DC Motor analysis")
p.xlabel("Torque")
p.ylabel("Speed")
p.show()

p.figure("Shunt")
p.plot(x,y)

p.title("DC Motor analysis")
p.xlabel("Torque")
p.ylabel("Speed")
p.show()
