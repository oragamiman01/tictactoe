game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def make_move(map, player=0, row=0, col=0):
    try:
        if player != 0:
            map[row][col] = player
        print("   0  1  2")
        for count, row in enumerate(map):
            print(count, row) #print row index and row item
        return map #avoid mutability errors
    except IndexError as e:
        print("Error: make sure you enter position as 0 1 or 2")


def horizontal_winner(map):
    for row in map:
        if (row[0] == row[1] == row[2]) and row[0] != 0:
            return row[0]
        else:
            return False

def vertical_winner(map):
    for col in range(3):
        if (map[0][col] == map[1][col] == map[2][col]) and map[0][col] != 0:
            return map[0][col]
        else:
            return False

def diagonal_winner(map):
    if map[1][1] != 0:
        if map[0][0] == map[1][1] == map[2][2]:
            return map[0][0]
        elif map[2][0] == map[1][1] == map[0][2]:
            return map[2][0]
        else:
            return False

#def is_valid_game(map):
    

game = make_move(game)
game = make_move(game, player=1, row=2, col = 2)
game = make_move(game, player=1, row=1, col = 1)
game = make_move(game, player=1, row=0, col = 0)
if vertical_winner(game):
    print(vertical_winner(game))
if horizontal_winner(game):
    print(horizontal_winner(game))
if diagonal_winner(game):
    print(diagonal_winner(game))