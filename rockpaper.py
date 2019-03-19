print("*****rock*****")
print("*****paper*****")
print("*****scissors*****")

player1 = input("write your choice player 1: ")
print("NO CHEATİNG!!!\n\n" * 20)
player2 = input("write your choice player 2: ")
if player1 and player2:
    if player1 == "rock" and player2 == "scissors":
        print("player 1 win!!!")
    elif player1 == "rock" and player2 == "paper":
        print("player 2 win!!!")
    elif player1 == "paper" and player2 == "rock":
        print("player 1 win!!!")
    elif player1 == "paper" and player2 == "scissors":
        print("player 2 win!!!")
    elif player1 == "scissors" and player2 == "rock":
        print("player 2 win!!!")
    elif player1 == "scissors" and player2 == "paper":
        print("player 1 win!!!")
    elif player1 == player2:
        print("it is a tie!")
else:
    print("i said write something!!!")
