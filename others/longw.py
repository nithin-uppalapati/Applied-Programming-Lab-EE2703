print("Enter a list of words...")
print("Please enter in this format (as shown below)...")
print(" [ ""word_1"", ""<word_2>"", ""<word_3>"" ] ")

def inputoflist():
    a=[]
    print('Enter the number of elements to be added in a list')
    n=int(input())
    print('Enter the elements of list, and then hit enter')
    for i in range(n):
        l=input()
        a.append(l)
    return a
    
u= inputoflist()

n=len(u)
k=0
for i in u:
    if( (len(i))>k ):
        k=len(i)
        z=u.index(i)
print(f"the longest word in the given list is - {u[z]} \n")


