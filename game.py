def make_move(map, player=0, row=0, col=0):
    try:
        if map[row][col] != 0:
            raise ValueError("invalid position")
        if player != 0:
            map[row][col] = player
        print("   0  1  2")
        for count, row in enumerate(map):
            print(count, row) #print row index and row item
        return map #avoid mutability errors
    except IndexError as e:
        print("Error: make sure you enter position as 0 1 or 2")

def stalemate(map):
    count = 0
    for row in map:
        for x in row:
            if x != 0:
                count += 1

    if count == (len(map))**2:
        print("Stalemate!")
        return True

def winner(map):
    #horizontal
    for row in map:
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f"Player {row[0]} is the winner! (horizontally)")
            return True

    #vertical
    for i in range(len(map)):
        vals = [] #holds values of each column
        for row in map:
            vals.append(row[i])
        if vals.count(vals[0]) == len(vals) and vals[0] != 0:
            print(f"Player {vals[0]} is the winner! (vertically)")
            return True

    #diagonals
    diag1 = [] #lower left to upper right
    for row,col in enumerate(reversed(range(len(map)))):
        diag1.append(map[row][col])

    diag2 = [] #upper left to bottom right
    for i in range(len(map)):
        diag2.append(map[i][i])

    if diag1.count(diag1[0]) == len(diag1) and diag1[0] != 0:
        print(f"Player {diag1[0]} is the winner! (diagonally /)")
        return True
    elif diag2.count(diag2[0]) == len(diag2) and diag2[0] != 0:
        print(f"Player {diag2[0]} is the winner! (diagonally \\)")
        return True
    else:
        return False


print("Welcome to tic-tac-toe")
playing = True

while playing:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    game = make_move(game)
    player = 1
    in_progress = True
    while in_progress:
        print("Player ", player)
        coordinates = input("enter coordinates: ")
        row_move = int(coordinates[0])
        col_move = int(coordinates[2])
        try:
            game = make_move(game, player, row_move, col_move)
            player = 2 if player == 1 else 1
        except ValueError as e:
            print("invalid position")
        if winner(game) or stalemate(game):
            play_again = input("Would you like to play again? (y/n): ")
            if play_again == "y":
                in_progress = False
            else:
                in_progress = False
                playing = False
