board = [" " for _ in range(9)]

def show():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check(player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for w in wins:
        if all(board[i] == player for i in w):
            return True
    return False

player = "X"

for turn in range(9):
    show()
    move = int(input(f"Player {player}, enter position (1-9): ")) - 1

    if move < 0 or move > 8 or board[move] != " ":
        print("Invalid move! Try again.")
        continue

    board[move] = player

    if check(player):
        show()
        print(f"🎉 Player {player} Wins!")
        break

    player = "O" if player == "X" else "X"
else:
    show()
    print("🤝 It's a Draw!")