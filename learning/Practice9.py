import random as random
mynum=random.randrange(1,10)
guess=input("Let's play the guessing game. Enter a number: ")
while(guess!="exit"):
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