# Tic-Tac-Toe Game against Computer
# Uses random library

import random

board = [" " for _ in range(9)]

def print_board():
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-----")

def check_winner(symbol):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],  # rows
        [0,3,6],[1,4,7],[2,5,8],  # columns
        [0,4,8],[2,4,6]           # diagonals
    ]
    for cond in win_conditions:
        if all(board[i] == symbol for i in cond):
            return True
    return False

def is_full():
    return " " not in board

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] == " ":
            board[move] = "X"
        else:
            print("Invalid move, try again.")
            continue

        if check_winner("X"):
            print_board()
            print("🎉 You win!")
            break

        if is_full():
            print_board()
            print("It's a draw!")
            break

        # Computer move
        comp_move = random.choice([i for i in range(9) if board[i] == " "])
        board[comp_move] = "O"

        print_board()

        if check_winner("O"):
            print("💻 Computer wins!")
            break

play_game()
