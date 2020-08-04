import pylab as p
pi=p.pi


def third(n):
	x=p.cos(0.2*pi*n)+p.cos(0.85*pi*n)
	return x
#n=p.arange(1,(2**10)+1)
n=p.arange(1,(2**10))
p.stem(n,third(n),use_line_collection=True)
p.xlabel("n" '$\longrightarrow$')
p.ylabel("Value" '$\longrightarrow$')

p.show()
