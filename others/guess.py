#Guess the number Game

import random
b=random.randint(1,10)
for i in range(1,10000):
	print("Please guess a number in the range {1,10} including 1 and 10...!!")
	a=int(input())
	if(a<b):
		print("You've under guessed it")
	elif(a>b):
		print("You've over guessed it")
	elif(a==b):
		print(f"You've guessed the correct number in {i} attempts !!")
		break
		
	print("Do you want to quit..? Bored of guessing the numbers..? Please enter (Y/N)")
	z=input()
	z=z.lower()
	if z=='n' :
		continue
	elif z=='y' :
		print("bye")
		break
