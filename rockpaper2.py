print("*****rock*****")
print("*****paper*****")
print("*****scissors*****")

player1 = input("write your choice player 1: ")
print("***NO CHEATİNG!!!***\n\n" * 20)
player2 = input("write your choice player 2: ")

if player1 and player2:
    if player1 == "rock":
        if player2 == "scissors":
            print("player 1 wins!!!")
        if player2 == "paper":
            print("player 2 wins!!!")
    if player1 == "paper":
        if player2 == "rock":
            print("player 1 wins!!!")
        if player2 == "scissors":
            print("player 2 wins!!!")
    if player1 == "scissors":
        if player2 == "rock":
            print("player 2 wins!!!")
        if player2 == "paper":
            print("player 1 wins!!!")
    if player1 == player2:
        print("it is a tie!")
    else:
        print("something went wrong!")

else:
    print("I said write something!!!")
