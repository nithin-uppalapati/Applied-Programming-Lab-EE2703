import sys
def listostr(l):
	str=""
	for i in l:
		str=str+i+" "
	return str


try:
	f = open(sys.argv[1])
	n=len(sys.argv)
	if n>2:
		print("Unnecessary arguments in the command line")
		exit()
	l = f.readlines()
#	print(l)
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
	m.reverse()
	print("\nThe reverse order of netlist is:")
	for i in m:
		j=i.split(" ")
		j.reverse()
		print(listostr(j))
	print("")
	m.reverse()
	for i in m:
		l=i.split(" ")
		l[0]
	
except IOError:
	print("File name DNE")
except IndexError:
	print("Please enter the name of netlist file")
