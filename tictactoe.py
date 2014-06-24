import copy

board = ['-' for i in range(9)]
occ_board = [0 for i in range(9)]
ctr = 0
turn = 0

def gameover (b):
    # rows for p1
    if (b[0]=='x' and b[1]=='x' and b[2]=='x') or (b[3]=='x' and b[4]=='x' and b[5]=='x') or (b[6]=='x' and b[7]=='x' and b[8]=='x'):
        return True
    # columns for p1
    elif (b[0]=='x' and b[3]=='x' and b[6]=='x') or (b[1]=='x' and b[4]=='x' and b[7]=='x') or (b[2]=='x' and b[5]=='x' and b[8]=='x'):
        return True
    # diagonals for p1
    elif (b[0]=='x' and b[4]=='x' and b[8]=='x') or (b[2]=='x' and b[4]=='x' and b[6]=='x'):
        return True
    # rows for p2
    if (b[0]=='o' and b[1]=='o' and b[2]=='o') or (b[3]=='o' and b[4]=='o' and b[5]=='o') or (b[6]=='o' and b[7]=='o' and b[8]=='o'):
        return True
    # columns for p2
    elif (b[0]=='o' and b[3]=='o' and b[6]=='o') or (b[1]=='o' and b[4]=='o' and b[7]=='o') or (b[2]=='o' and b[5]=='o' and b[8]=='o'):
        return True
    # diagonals for p2
    elif (b[0]=='o' and b[4]=='o' and b[8]=='o') or (b[2]=='o' and b[4]=='o' and b[6]=='o'):
        return True
    else:
        return False

def winningMove (n, b, p):
    cp = copy.deepcopy(b)
    if p:
        cp[n] = 'o'
    else:
        cp[n] = 'x'
    return gameover (cp)

def printboard (board):
    print board[0], board[1], board[2]
    print board[3], board[4], board[5]
    print board[6], board[7], board[8]

def minmax (node, depth, maxPlayer, board, occ_board, m):
    #print node
    if (depth == (m-1)) or winningMove(node, board, maxPlayer):
        printboard (board)
        if winningMove(node, board, maxPlayer) and (maxPlayer == True):
            print "you win! move:", node, "value", (10-depth)
            return (10 - depth)
        elif winningMove(node, board, maxPlayer) and (maxPlayer == False):
            print "you lose! move:", node, "value:", (depth-10)
            return (depth - 10)
        else:
            print "hi"
            return 0

    # copy board and occ_board
    n_board = copy.deepcopy(board)
    n_occ_board = copy.deepcopy(occ_board)
    # update copy of board and occ_board
    if maxPlayer:
        n_board[node] = 'o'
    else:
        n_board[node] = 'x'
    n_occ_board[node] = 1

    # list of possible nodes
    pos_moves = [i for i, j in enumerate(n_occ_board) if j == 0]

    # want to max the min value if you're maxPlayer
    if maxPlayer:
        bestValue = float("inf")
        for i in pos_moves:
            value = minmax(i, depth+1, False, n_board, n_occ_board, m)
            bestValue = min(bestValue, value)
        return bestValue
    # min the max value if you're not maxPlayer
    else:
        bestValue = -float("inf")
        for i in pos_moves:
            value = minmax(i, depth+1, True, n_board, n_occ_board, m)
            print "move:", i, "value:", value
            bestValue = max(bestValue, value)
        print bestValue
        return bestValue

board = ['x', '-', 'x',
         '-', 'x', '-',
         'o', '-', 'o']
occ_board = [1, 0, 1,
             0, 1, 0,
             1, 0, 1]

moves = [i for i, j in enumerate(occ_board) if j == 0]

for i in moves:
    new_board = copy.deepcopy(board)
    new_occ_board = copy.deepcopy(occ_board)
    val = minmax(i, 0, True, new_board, new_occ_board, 4)
    print "MOVE AND VALUE:", i, val
'''
while (not(gameover (board))):
    if (ctr == 9):
        break;
    if turn == 0:
        x = int(raw_input())
    else:
        (x, val) = minmax(x, 1, False, board, occ_board)
    for i in range(9):
        if x == i:
            if not(occ_board[i]):
                ctr += 1
                occ_board[i] = 1
                if turn == 0:
                    board[i] = 'x'
                    turn = 1
                else:
                    board[i] = 'o'
                    turn = 0
            else:
                print "Occupied, please choose a valid move!"
    print board[0], board[1], board[2]
    print board[3], board[4], board[5]
    print board[6], board[7], board[8]
'''
