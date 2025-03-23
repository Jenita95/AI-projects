import random

def initialize_board():
    return [' ' for _ in range(9)] 

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_win(board, player):
    win_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), 
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)             
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

def is_board_full(board):
    return ' ' not in board

def minimax(board, depth, is_maximizing):
    if check_win(board, 'O'):
        return 1
    if check_win(board, 'X'):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best = max(best, score)
        return best
    else:
        best = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best = min(best, score)
        return best

def ai_move(board):
    best_val = -float('inf')
    best_move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            move_val = minimax(board, 0, False)
            board[i] = ' '
            if move_val > best_val:
                best_move = i
                best_val = move_val
    return best_move

def play_game():
    board = initialize_board()
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        while True:
            try:
                player_move = int(input("Enter your move (0-8): "))
                if 0 <= player_move <= 8 and board[player_move] == ' ':
                    board[player_move] = 'X'
                    break
                else:
                    print("Invalid move! The cell is already occupied or out of range.")
            except (ValueError, IndexError):
                print("Invalid input! Please enter a number between 0 and 8.")

        print_board(board)
        if check_win(board, 'X'):
            print("Congratulations, you win!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break
        
        print("AI's turn...")
        ai_move_position = ai_move(board)
        board[ai_move_position] = 'O'
        print_board(board)

        if check_win(board, 'O'):
            print("AI wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
