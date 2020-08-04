print("Enter the file name:")
a=input()
n=a.find('.')
l=a.split('.')
if(n==-1):
    print("Incorrect file format...!")

elif((len(l))>2): print("Incorrect file format...!")
else: print(f"The extension of the file is {l[1]}")

