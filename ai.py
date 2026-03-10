import random
from game import check_winner, check_draw

def minimax(board, is_maximizing):

    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if check_draw(board):
        return 0

    if is_maximizing:
        best_score = -100
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score

    else:
        best_score = 100
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score


def best_move(board, difficulty="hard"):

    if difficulty == "easy":
        choices = [i for i,v in enumerate(board) if v == " "]
        return random.choice(choices)

    best_score = -100
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move