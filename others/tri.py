print("Enter the three sides of a triangle")
print("a=")
a=int(input())
print("b=")
b=int(input())
print("c=")
c=int(input())
##  | (abs(a-c)>=b) | (abs(b-c)>=a) | (abs(a-b)>=c)
if( ((a+b)<=c) | ((c+b)<=a) | ((a+c)<=b) ):
    print("The given sides doesn't form a triangle")
elif(a==b & a==c):print("The trianlge is equilateral")
elif((a==b) | (a==c) | (b==c)):print("The trianlge is isosceles")
else:print("The trianlge is scalene")


    
    
