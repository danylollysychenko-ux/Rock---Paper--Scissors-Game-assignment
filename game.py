import random
player_score = 0
ai_score = 0
def convert_letter_to_word(letter):
    """Converts letter to word and return the full word"""

    if letter == "r":
        return "rock"
    elif letter == "s":
        return "scissors"
    elif letter == "p":
        return "paper"
    
def print_series_results(user_wins, comp_wins):
    """Prints who won the full series of 5 rounds"""

    print(f"AI won {comp_wins} rounds.")
    print(f"You won {user_wins} rounds.\n")

    if comp_wins > user_wins:
        print(f"AI won the series.")
    elif comp_wins < user_wins:
        print("You won the series.")
    else:
        print("It's a tie.\nNobody won.")

def determine_outcome(user, comp):
    """ determines the outcome and returns the result of whatever condition(s) it falls under """

    if comp == "rock" and user == "rock" or comp == "scissors" and user == "scissors" or comp == "paper" and user == "paper":
        return "tie"
    elif comp == "rock" and user == "scissors" or comp == "scissors" and user == "paper" or comp == "paper" and user == "rock":
        return "AI won"
    elif comp == "rock" and user == "paper" or comp == "scissors" and user == "rock" or comp == "paper" and user == "scissors":
        return "you won"

def print_round_results(user, comp, result):
    """Makes the variables global so the whole program can use it and prints the round result after checking conditions from determine outcome"""

    global player_score , ai_score

    if result == "tie":
        print(f"You played \" {user} \" the computer played \" {comp} \" it's a tie.\n")

    elif result == "AI won":
        print(f"You played \" {user} \" the computer played \" {comp} \" ai won.\n")
        ai_score += 1

    elif result == "you won":
        print(f"You played \" {user} \" the computer played \" {comp} \" you won.\n")
        player_score += 1

def get_valid_input():
    """Get the valid from the user and returns player_move"""
    """
    while True:
    -get move
    if move is valid in comp_moves
    return move
    print invalid move

    """
    
    while True:
        player_move = input(f"Enter r, p, s: ").strip().lower()
        print()

        if player_move in comp_moves:
            return player_move
        
        print("Invalid input.")

global comp_moves
comp_moves = ["r", "s", "p"]

def main():
    for i in range(5):
        print(f"Round {i+1}")

        player_move = get_valid_input()

        ai_choice = random.choice(comp_moves)
        ai_choice = convert_letter_to_word(ai_choice)
        player_move = convert_letter_to_word(player_move)
        
        
            
        result = determine_outcome(player_move, ai_choice)
        print_round_results(player_move, ai_choice, result)

    print_series_results(player_score, ai_score)

if __name__ == "__main__":
    main()