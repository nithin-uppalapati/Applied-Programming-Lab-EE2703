a=input()
l=len(a)
a=list(a)

def listtostr(l):
    s=''
    for i in l:
        s=s+i

    return s

for i in range(l):
    if ( (ord(a[i])<91) & (ord(a[i])>64) ):
        a[i]=chr(ord(a[i])+32)
    elif( (ord(a[i])<123) & (ord(a[i])>96) ):
        a[i]=chr(ord(a[i])-32)

a=(listtostr(a))

print(a)

