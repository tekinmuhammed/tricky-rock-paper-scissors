import random

def create_computer_choise():
    n = random.randint(1, 3)
    if  n == 1:
        return "rock"
    elif n == 2:
        return "paper"
    else:
        return "scissors"

def create_tricky_computer_choise(user_choise):
    if user_choise == "rock":
        return "paper"
    elif user_choise == "paper":
        return "scissors"
    else:
        return "rock"
    
score_user = 0
score_computer = 0

while True:
    user_choise = input(" rock? paper? scissors? ")
    n = random.randint(1,2)
    if n == 1:
        computer_choise = create_computer_choise
    else:
        computer_choise = create_tricky_computer_choise(user_choise)
    print("Computer:", computer_choise)

    if user_choise == computer_choise:
        print("Draw")
    elif computer_choise == "rock" and user_choise == "paper":
        score_user += 1
    elif computer_choise == "paper" and user_choise == "scissors":
        score_user += 1
    elif computer_choise == "scissors" and user_choise == "rock":
        score_user += 1
    else:
        score_computer += 1
    print("You:", score_user, " VS PC:", score_computer)

    if score_user == 3 or score_computer == 3:
        break
if score_computer > score_user:
    print("You Lost..")
else:
    print("You Won!")
