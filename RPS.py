import random
wins = 0
losses = 0

def cpu_choice(rps_list):
    global cpu_save
    cpu_num = random.randint(1,3)
    if cpu_num == 1:
        cpu_save = (str(rps_list[0]))
    elif cpu_num == 2:
        cpu_save = (str(rps_list[1]))
    elif cpu_num == 3:
        cpu_save = (str(rps_list[2]))

    return cpu_save

def fite_me(cpu_save):
    playerwins = 0
    cpuwins = 0
    list = []
    if choice == "rock" and cpu_save == "rock":
        print("The computer chose rock!")
        print("It's a tie!")
    elif choice == "rock" and cpu_save == "paper":
        print("The computer chose paper!")
        print("The computer wins!")
        cpuwins = cpuwins + 1
    elif choice == "rock" and cpu_save == "scissors":
        print("The computer chose scissors!")
        print(name + " wins!")
        playerwins = playerwins + 1
    elif choice == "paper" and cpu_save == "rock":
        print("The computer chose rock!")
        print(name + " wins!")
        playerwins = playerwins + 1
    elif choice == "paper" and cpu_save == "paper":
        print("The computer chose paper!")
        print("It's a tie!")
    elif choice == "paper" and cpu_save == "scissors":
        print("The computer chose scissors!")
        print("The computer wins!")
        cpuwins = cpuwins + 1
    elif choice == "scissors" and cpu_save == "rock":
        print("The computer chose rock!")
        print("The computer wins!")
        cpuwins = cpuwins + 1
    elif choice == "scissors" and cpu_save == "paper":
        print("The computer chose paper!")
        print(name + " wins!")
        playerwins = playerwins + 1
    elif choice == "scissors" and cpu_save == "scissors":
        print("The computer chose scissors!")
        print("It's a tie!")
    list = []
    list.append(playerwins)
    list.append(cpuwins)
    return list



name = input("What's your name?")
print("Let's play rock paper scissors, " + name + "!")


rps_list = ["rock", "paper", "scissors"]


answer = "y"

while answer == "y":
    otherList = [0]
    choice = input("Rock, paper, or scissors? (Type in lowercase)")

    if choice == "rock":
        print("Thank you for entering a valid choice")
    elif choice == "paper":
        print("Thank you for entering a valid choice")
    elif choice == "scissors":
        print("Thank you for entering a valid choice")
    else:
        while choice != "rock" or choice != "paper" or choice != "scissors":
            print("Invalid choice, please input a valid one")
            choice = input("rock, paper, or scissors? (Type in lowercase)")
            if choice == "rock" or choice == "paper" or choice == "scissors":
                print("Thank you for entering a valid choice")
                break

    cpu_choice(rps_list)
    otherList = fite_me(cpu_save)
    wins = wins + otherList[0]
    losses = losses + otherList[1]
    answer = input("Wanna play again? (y or n in lowercase)")

if wins > losses: 
    print("You won " + str(wins) + " time(s)")
    print("The computer won " + str(losses) + " time(s)")
    print("You won the most times against the computer!")
elif wins < losses:
    print("You won " + str(wins) + " time(s)")
    print("The computer won " + str(losses) + " time(s)")
    print("The computer won the most times against you!")
else:
    print("You won " + str(wins) + " time(s)")
    print("The computer won " + str(losses) + " time(s)")
    print("You tied with the computer!")

print("Thanks for playing!")
