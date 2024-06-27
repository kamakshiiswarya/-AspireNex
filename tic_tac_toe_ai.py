# Tic-Tac-Toe game with Minimax AI

import random

# Game constants
BOARD_SIZE = 3
X = "X"
O = "O"
EMPTY = " "

# Game board representation
board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, alpha, beta, is_maximizing):
    if has_won(board, X):
        return -10 + depth
    elif has_won(board, O):
        return 10 - depth
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == EMPTY:
                    board[i][j] = O
                    score = minimax(board, depth + 1, alpha, beta, False)
                    board[i][j] = EMPTY
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = float('inf')
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == EMPTY:
                    board[i][j] = X
                    score = minimax(board, depth + 1, alpha, beta, True)
                    board[i][j] = EMPTY
                    best_score = min(best_score, score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score

# AI makes a move
def ai_move():
    best_score = -float('inf')
    best_move = None
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == EMPTY:
                board[i][j] = O
                score = minimax(board, 0, -float('inf'), float('inf'), False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    board[best_move[0]][best_move[1]] = O

# Human makes a move
def human_move():
    while True:
        move = input("Enter your move (row and column, separated by space): ")
        row, col = map(int, move.split())
        if board[row][col] == EMPTY:
            board[row][col] = X
            break
        else:
            print("Invalid move, try again!")

# Check if a player has won
def has_won(board, player):
    for i in range(BOARD_SIZE):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(BOARD_SIZE)]):
            return True
    if all([board[i][i] == player for i in range(BOARD_SIZE)]):
        return True
    if all([board[i][BOARD_SIZE - i - 1] == player for i in range(BOARD_SIZE)]):
        return True
    return False

# Check if the board is full
def is_board_full(board):
    return all([cell != EMPTY for row in board for cell in row])

# Print the game board
def print_board():
    for row in board:
        print(" | ".join(row))
        print("---------")

# Game loop
while True:
    print_board()
    human_move()
    if has_won(board, X):
        print("Human wins!")
        break
    ai_move()
    if has_won(board, O):
        print("AI wins!")
        break
    if is_board_full(board):
        print("It's a draw!")
        break
