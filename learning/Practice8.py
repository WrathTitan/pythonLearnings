print("Welcome to a rock paper scissors game!")
player1=input("Enter the name of player 1: ")
player2=input("Enter the name of player 2: ")
print(player1,"Please play your turn. Enter R for rock, P for paper and S for scissors")
ch1=input().upper()
print(player2,"Please play your turn. Enter R for rock, P for paper and S for scissors")
ch2=input().upper()
if(ch1=='R' and ch2=='S'):
    print("Player 1",player1,"wins!")
elif(ch1=='S' and ch2=='P'):
    print("Player 1",player1,"wins!")
elif(ch1=='P' and ch2=='R'):
    print("Player 1",player1,"wins!")
elif(ch2=='R' and ch1=='S'):
    print("Player 2",player2,"wins!")
elif(ch2=='S' and ch1=='P'):
    print("Player 2",player2,"wins!")
elif(ch2=='P' and ch1=='R'):
    print("Player 2",player2,"wins!")
else:
    print("Draw Match")
