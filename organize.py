def get_valid_input():
    comp_moves = ["r", "s", "p"]
    for i in range(5):
        while True:
            print(f"Round {i+1}")
            player_move = input("Enter r, p, s: ").strip().lower()
            print()
            if player_move not in comp_moves:
                print("Invalid input.")
                player_move = input("Enter r, p, s: ").strip().lower()
            else:
                break

get_valid_input()