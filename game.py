
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
            print(row[0], end='')
            return row[0]
        else:
            return False

def vertical_winner(map):
    for col in range(3):
        if (map[0][col] == map[1][col] == map[2][col]) and map[0][col] != 0:
            print(map[0][col], end='')
            return map[0][col]
        else:
            return False

def diagonal_winner(map):
    if map[1][1] != 0:
        if map[0][0] == map[1][1] == map[2][2]:
            print(map[0][0], end='')
            return map[0][0]
        elif map[2][0] == map[1][1] == map[0][2]:
            print(map[2][0], end='')
            return map[2][0]
        else:
            return False

def is_valid_game(map):
    if horizontal_winner(map) or vertical_winner(map) or diagonal_winner(map):
        print(" is the winner!")
        return False
    else:
        return True

print("Welcome to tic-tac-toe")

game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
game = make_move(game)
player = 1

game = make_move(game, player=2, row=2, col = 0)
game = make_move(game, player=2, row=1, col = 0)
game = make_move(game, player=2, row=0, col = 0)
is_valid_game(game)

'''
while is_valid_game(game) :
    print("Player ", player)
    coordinates = input("enter coordinates: ")
    row_move = int(coordinates[0])
    col_move = int(coordinates[2])
    game = make_move(game, player, row_move, col_move)
    player = 2 if player == 1 else 1'''
