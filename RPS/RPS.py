import random

options = ["rock", "paper", "scissors"]

u_score = 0
c_score = 0

while True:
    u_input = input("Type Rock/Paper/Scissors/Q for Quit: ").lower()
    if u_input == "q":
        break

    if u_input not in options:
        continue

    r_number = random.randint(0, 2)
    # rock = 0, paper = 1, scissors = 2
    c_pick = options[r_number]
    print("Computer picked: ", c_pick)

    if (u_input == "rock" and c_pick == "scissors") or (u_input == "paper" and c_pick == "rock") or (u_input == "scissors" and c_pick == "paper"):
        print("You Won")
        u_score += 1
    elif (u_input == "scissors" and c_pick == "rock") or (u_input == "rock" and c_pick == "paper") or (u_input == "paper" and c_pick == "scissors"):
        print("You Lost")
        c_score += 1
    else:
        print("It is a Tie Game")
print("You won", u_score, "times")
print("Computer won", c_score, "times")
