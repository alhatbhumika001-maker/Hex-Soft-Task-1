import random

board = [" " for _ in range(9)]

def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],   # rows
        [0,3,6], [1,4,7], [2,5,8],   # columns
        [0,4,8], [2,4,6]             # diagonals
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def user_move():
    while True:
        try:
            pos = int(input("Enter position (1-9): ")) - 1
            if board[pos] == " ":
                board[pos] = "X"
                break
            else:
                print("Position already taken!")
        except:
            print("Invalid input! Try again.")

def computer_move():
    empty_positions = [i for i in range(9) if board[i] == " "]
    pos = random.choice(empty_positions)
    board[pos] = "O"
    print(f"Computer chose position {pos+1}")

def is_draw():
    return " " not in board

# Game loop
while True:
    print_board()
    user_move()

    if check_winner("X"):
        print_board()
        print("🎉 You Win!")
        break

    if is_draw():
        print_board()
        print("It's a Draw!")
        break

    computer_move()

    if check_winner("O"):
        print_board()
        print("💻 Computer Wins!")
        break

    if is_draw():
        print_board()
        print("It's a Draw!")
        break