import sys

try:
	f = open(sys.argv[1])
	n=len(sys.argv)
	l = f.readlines()
	count=0
	for i in l:
		t=i.partition("#")
		i=t[0].strip()
		l[count]=i
		count+=1
	f.close()
	end=None
	begin=None
	count=0
	for i in l:
		if i==".circuit":
			begin=count+1
		if i==".end":
			end=count
			break
		count=count+1
	if ( (begin==None) or (end==None) ):
		print("Invalid description of circuit")
		exit()
	m=l[begin:end]
	n=l[end+1:]
#	print(m)
#	m.reverse()
#	print("\nThe reverse order of netlist is:")
#	for i in m:
#		print(i)


except IOError:
	print("File name DNE")
except IndexError:
	print("Please enter the name of netlist file")
