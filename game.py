game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def make_move(map, player=0, row=0, col=0):
    if player != 0:
        map[row][col] = player
    print("   0  1  2")
    for count, row in enumerate(map):
        print(count, row) #print row index and row item
    return map #avoid mutability errors

game = make_move(game)
game = make_move(game, player=1, row=2, col = 2)
