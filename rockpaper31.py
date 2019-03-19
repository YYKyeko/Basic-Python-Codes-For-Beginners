print("*****rock*****")
print("*****paper*****")
print("*****scissors*****")


from random import randint

player = input("write your choice player: ").lower()
rand_num = randint(0, 2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print(f"Computer plays: {computer}")

if player and computer:
    if player == "rock":
        if computer == "scissors":
            print("player  wins!!!")
        if computer == "paper":
            print("computer wins!!!")
    if player == "paper":
        if computer == "rock":
            print("player  wins!!!")
        if computer == "scissors":
            print("computer wins!!!")
    if player == "scissors":
        if computer == "rock":
            print("computer wins!!!")
        if computer == "paper":
            print("player  wins!!!")
    if player == computer:
        print("it is a tie!")
    else:
        print("please enter a valid move!")

else:
    print("I said write something!!!")
