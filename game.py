import random

comp_moves = ["r", "s", "p"]
ai_choice = random.choice(comp_moves)
player_move = input("Enter r, p, s: ").strip().lower()

if player_move not in comp_moves:
    print("Invalid input.")
else:
    pass

if player_move == "r":
    player_move = "rock"
elif player_move == "s":
    player_move = "scissors"
elif player_move == "p":
    player_move = "paper"

if ai_choice == "p":
    ai_choice = "paper"
elif ai_choice == "s":
    ai_choice = "scissors"
elif ai_choice == "r":
    ai_choice = "rock"


if ai_choice == "rock" and player_move == "rock" or ai_choice == "scissors" and player_move == "scissors" or ai_choice == "paper" and player_move == "paper":
    print(f"You played \" {player_move} \" the computer played \" {ai_choice} \" it's a tie.")

elif ai_choice == "rock" and player_move == "scissors" or ai_choice == "scissors" and player_move == "paper" or ai_choice == "paper" and player_move == "rock":
    print(f"You played \" {player_move} \" the computer played \" {ai_choice} \" ai won.")

elif ai_choice == "rock" and player_move == "paper" or ai_choice == "scissors" and player_move == "rock" or ai_choice == "paper" and player_move == "scissors":
    print(f"You played \" {player_move} \" the computer played \" {ai_choice} \" you won.")