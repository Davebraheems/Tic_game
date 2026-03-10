from flask import Flask, render_template, request, jsonify
from ai import best_move
from game import check_winner, check_draw

app = Flask(__name__)

board = [" "] * 9


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/move", methods=["POST"])
def move():

    data = request.json
    player_move = data["move"]
    difficulty = data.get("difficulty", "hard")

    board[player_move] = "X"

    winner = check_winner(board, "X")
    if winner:
        return jsonify({"board": board, "result": "X", "combo": winner})

    if check_draw(board):
        return jsonify({"board": board, "result": "Draw", "combo":[]})

    ai = best_move(board, difficulty)
    board[ai] = "O"

    winner = check_winner(board, "O")
    if winner:
        return jsonify({"board": board, "result": "O", "combo": winner})

    if check_draw(board):
        return jsonify({"board": board, "result": "Draw", "combo":[]})

    return jsonify({"board": board, "result": "continue", "combo":[]})
@app.route("/reset")
def reset():
    global board
    board = [" "] * 9
    return jsonify({"board":board})


if __name__ == "__main__":
    app.run(debug=True)