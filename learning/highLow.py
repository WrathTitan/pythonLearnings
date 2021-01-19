'''
	High and Low Game
	Importing Random Library
'''
import random as random		#importing random libraries
mynum=random.randrange(1,10)		#random.randrange() function to output random numbers between 1 and 9 (including 1 and 9)
guess=input("Let's play the guessing game. Enter a number: ")
while(guess!="exit"):		#using while loop to infinitely check the game
    n=int(guess)
    if(n>mynum):	
        print("Too High! Enter the number again...")
    elif(n<mynum):
        print("Too Low! Enter the number again...")
    elif(n==mynum):
        print("Correct Number Entered! You win the guessing game!")
        break
    else:
        print("Incorrect Input. Please Enter again...")
    guess=input()
print("Thanks for playing!")
