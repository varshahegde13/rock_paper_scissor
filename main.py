import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]


while True:
    user_input = input("Type Rock/Paper/Scissors or q to Quit:").lower()
    if user_input == "q":
        break

    if user_input not in ["rock","paper","scissors"]:
        continue

    random_number =  random.randint(0,2)
#     rock :0, paper:1, scissors:2

    computer_pick = options[random_number]
    print("computer picked", computer_pick + ".")


    if user_input =="rock" and computer_pick == "paper":
        print("You won!!")
        user_wins+=1
        continue

    elif user_input == "rock" and computer_pick == "scissors":
        print("You won!!")
        user_wins += 1
        continue
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!!")
        user_wins += 1
        continue
    else:
        print("You Lost!")
        computer_wins+=1

print("You won",user_wins, "times")
print("computer wins", computer_wins, "times")
print("Good Bye")

