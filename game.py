import random

def convert_letter_to_word(letter):
    if letter == "r":
        return "rock"
    elif letter == "s":
        return "scissors"
    elif letter == "p":
        return "paper"

def get_valid_input():
    pass

player_score = 0
ai_score = 0

for i in range(5):
    comp_moves = ["r", "s", "p"]
    ai_choice = random.choice(comp_moves)
    while True:
        print(f"Round {i+1}")
        player_move = input("Enter r, p, s: ").strip().lower()
        print()
        if player_move not in comp_moves:
            print("Invalid input.")
            player_move = input("Enter r, p, s: ").strip().lower()
        else:
            break

    
    ai_choice = convert_letter_to_word(ai_choice)
    player_move = convert_letter_to_word(player_move)

    if ai_choice == "rock" and player_move == "rock" or ai_choice == "scissors" and player_move == "scissors" or ai_choice == "paper" and player_move == "paper":
        print(f"You played \" {player_move} \" the computer played \" {ai_choice} \" it's a tie.\n")

    elif ai_choice == "rock" and player_move == "scissors" or ai_choice == "scissors" and player_move == "paper" or ai_choice == "paper" and player_move == "rock":
        print(f"You played \" {player_move} \" the computer played \" {ai_choice} \" ai won.\n")
        ai_score += 1

    elif ai_choice == "rock" and player_move == "paper" or ai_choice == "scissors" and player_move == "rock" or ai_choice == "paper" and player_move == "scissors":
        print(f"You played \" {player_move} \" the computer played \" {ai_choice} \" you won.\n")
        player_score += 1

print(f"AI won {ai_score} rounds.")
print(f"You won {player_score} rounds.\n")

if ai_score > player_score:
    print(f"AI won.")
elif ai_score < player_score:
    print("You won.")
else:
    print("It's a tie.")