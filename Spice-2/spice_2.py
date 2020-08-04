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
except IOError:
	print("File name DNE")
	exit()
except IndexError:
	print("Please enter the name of netlist file")
	exit()

######################################################### the above is spice_1copy #######
one_port={'R','L','C','V','I'}
two_port={'G','E','H','F'}
import numpy as np
import cmath as cm
import scipy as sp

ac=False
for i in n:
	if i[0:3]==".ac":
		ac=True
		i=i.split(' ')
		w=float(i[2])
		w=2*w*(np.pi)# w is frequency in RadSec-1 [units]
nodes_ele_dict={}
elements={}
J=complex(1j)
i_vs={}# i through v-sources
l=[]
for i in m: #m is a list of lines from the file{between .circuit and .end}
	l.append(i.split(' '))
	#l is a list of lists which has the words from each line //// variables used
	n=0
if not ac:
	for i in l:
		if i[0][0] in {'V','I'}:
			i.remove('dc')
		if i[0][0]=='V':
			n+=1
		if i[0][0] in one_port:
			elements.update({i[0]:[[i[1],i[2]],(float(i[3]))]})
			if i[1] not in nodes_ele_dict.keys():
				nodes_ele_dict.update({i[1]:{i[0]}})
			else:
				nodes_ele_dict[i[1]].add(i[0])
			if i[2] not in nodes_ele_dict.keys():
				nodes_ele_dict.update({i[2]:{i[0]}})
			else:
				nodes_ele_dict[i[2]].add(i[0])
				
	c=len(nodes_ele_dict)+n-1
	G=np.array([np.zeros(c)]*c)
	I=np.array(np.zeros(c))
	vs_i={}
	row=0
	clm=0
	cord_i=len(nodes_ele_dict)-1
	nodes_ele_dict.pop('GND')
	print(elements)
	print(nodes_ele_dict)
#	for i in elements:
#		if i[0] in {}
		
	
	
if ac:
	for i in l:
		if i[0][0] in {'V','I'}:
			i.remove('ac')
			t=np.deg2rad(float(i[4]))
			t=cm.rect((float(i[3])),t)
			t=t/2
			elements.update({i[0]:[[i[1],i[2]],t]})
			if i[1] not in nodes_ele_dict.keys():
				nodes_ele_dict.update({i[1]:{i[0]}})
			else:
				nodes_ele_dict[i[1]].add(i[0])
			if i[2] not in nodes_ele_dict.keys():
				nodes_ele_dict.update({i[2]:{i[0]}})
			else:
				nodes_ele_dict[i[2]].add(i[0])
		if i[0][0]=='V':
			n+=1
		if i[0][0]=='L':
			t=(float(i[3]))*J*w
			elements.update({i[0]:[[i[1],i[2]], t]})
			if i[1] not in nodes_ele_dict.keys():
				nodes_ele_dict.update({i[1]:{i[0]}})
			else:
				nodes_ele_dict[i[1]].add(i[0])
			if i[2] not in nodes_ele_dict.keys():
				nodes_ele_dict.update({i[2]:{i[0]}})
			else:
				nodes_ele_dict[i[2]].add(i[0])
		if i[0][0] == 'C':
			t=(float(i[3]))*J*w
			t=1/t
			elements.update({i[0]:[[i[1],i[2]], t]})
			if i[1] not in nodes_ele_dict.keys():
				nodes_ele_dict.update({i[1]:{i[0]}})
			else:
				nodes_ele_dict[i[1]].add(i[0])
			if i[2] not in nodes_ele_dict.keys():
				nodes_ele_dict.update({i[2]:{i[0]}})
			else:
				nodes_ele_dict[i[2]].add(i[0])
		if i[0][0] == 'R':
			elements.update({i[0]:[[i[1],i[2]], (float(i[3]))]})
			if i[1] not in nodes_ele_dict.keys():
				nodes_ele_dict.update({i[1]:{i[0]}})
			else:
				nodes_ele_dict[i[1]].add(i[0])
			if i[2] not in nodes_ele_dict.keys():
				nodes_ele_dict.update({i[2]:{i[0]}})
			else:
				nodes_ele_dict[i[2]].add(i[0])

	c=len(nodes_ele_dict)+n-1
	G=np.array([np.zeros(c)]*c,dtype=complex)
	I=np.array(np.zeros(c),dtype=complex)
	vs_i={}
	row=0
	clm=0
	cord_i=len(nodes_ele_dict)-1
	nodes_ele_dict.pop('GND')

for k in nodes_ele_dict:
	for j in nodes_ele_dict:
		if row==clm:
			for i in nodes_ele_dict[k]:
				if i[0] in {'R','C','L'}:
					G[row,clm]+=1/(elements[i][1])
				else:
					if i[0]=='V' and i not in vs_i:
						if elements[i][0][0]==k:
							G[row,cord_i]=1
							G[cord_i,row]=1
							I[cord_i]=elements[i][1]
						elif elements[i][0][0]!='GND':
							G[row,cord_i]=-1
							G[cord_i,row]=-1
							I[cord_i]=-1*(elements[i][1])
						elif elements[i][0][0]=='GND':
							G[row,cord_i]=-1
							G[cord_i,row]=1
							I[cord_i]=-1*(elements[i][1])
						vs_i.update({i:cord_i})
						cord_i+=1
					elif i[0]=='V' and i in vs_i:
						if elements[i][0][0]==k:
							G[row,vs_i[i]]=1
						else:
							G[row,vs_i[i]]=-1
				if i[0]=='I':
					if elements[i][0][0]==k:
						I[row]+=elements[i][1]
					else:
						I[row]+=-1*(elements[i][1])
			if clm < len(nodes_ele_dict)-1 :
				clm+=1
			elif row < len(nodes_ele_dict)-1 :
				clm=0
				row+=1
		if row!=clm and j!=k:

			for p in nodes_ele_dict[k].intersection(nodes_ele_dict[j]):
				if p[0] in {'R','C','L'}:
					G[row,clm]+=-1/(elements[p][1])
			if clm < len(nodes_ele_dict)-1 :
				clm+=1
			elif row < len(nodes_ele_dict)-1 :
				clm=0
				row+=1

solution=np.linalg.solve(G,I)

print(G,'\n')
print(I,'\n')
print(solution)
print(nodes_ele_dict)
print(elements)
#print(elements)
#print(nodes_ele_dict)
count=0
vol_dic={}
for i in nodes_ele_dict:
	print("The voltage at node",i,"is",solution[count])
	vol_dic.update({i:solution[count]})
	count+=1
for i in vs_i:
	print("The current passing against the voltage source",i,"is",solution[vs_i[i]])
vol_dic.update({'GND':0})
for i in elements:
	if i[0] not in {'V','I'}:
		t=((vol_dic[elements[i][0][0]])-(vol_dic[elements[i][0][1]]))
		t=t/(elements[i][1])
		print("The current passing through",i,"from",elements[i][0][0],"to",elements[i][0][1],"is",t)

##################################### SAVE -- ...final...
#DOUBTS:
#is the phase in degrees? I'm assuming it to be in degrees
####### the speed of this program is proportional to n**3, where n is no. of nodes ########
