print("Enter the sequence of numbers as a list")
#a=input()
a=[1,23,3,34,4,4,4,7,7,7]
a=set(a)
a=list(a)
a.sort()
l=len(a)

b=[]

for n in range (0,l-1):
    n_1=a[n]
    n_2=a[n+1]
    for i in range(n_1+1,n_2):
        b.append(i)

print(b)
