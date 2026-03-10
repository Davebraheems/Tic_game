WIN_PATTERNS = [
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
]

def check_winner(board, player):

    for pattern in WIN_PATTERNS:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] == player:
            return pattern

    return None


def check_draw(board):
    return " " not in board