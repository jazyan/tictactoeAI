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
    if p:
        b[n] = 'o'
    else:
        b[n] = 'x'
    return gameover (b)

def printboard (board):
    print board[0], board[1], board[2]
    print board[3], board[4], board[5]
    print board[6], board[7], board[8]

def minmax (node, depth, maxPlayer, board, occ_board, m):
    #print node
    print "what old board should be"
    printboard (board)
    if (depth == (m-1)) or winningMove(node, board, maxPlayer):
        printboard (board)
        if winningMove(node, board, maxPlayer) and (maxPlayer == True):
            print "you win!"
            return (10 - depth)
        elif winningMove(node, board, maxPlayer) and (maxPlayer == False):
            print "you lose!"
            return (depth - 10)
        else:
            print "hi"
            return 0
    n_board = copy.deepcopy(board)
    #print "such deep, such node:", depth, node
    if maxPlayer:
        n_board[node] = 'o'
    else:
        n_board[node] = 'x'
    n_occ_board = copy.deepcopy(occ_board)
    n_occ_board[node] = 1

    print "new board!"
    printboard (n_board)

    print "old board"
    printboard (board)

    pos_moves = [i for i, j in enumerate(n_occ_board) if j == 0]
    if maxPlayer:
        bestValue = -float("inf")
        for i in pos_moves:
            value = minmax(i, depth+1, False, n_board, n_occ_board, m)
            bestValue = max(bestValue, value)
        return bestValue
    else:
        bestValue = float("inf")
        for i in pos_moves:
            value = minmax(i, depth+1, True, n_board, n_occ_board, m)
            bestValue = min(bestValue, value)
        print "worst case", bestValue
        return bestValue

board = ['o', '-', '-',
         '-', 'o', '-',
         'x', '-', 'x']
occ_board = [1, 0, 0,
             0, 1, 0,
             1, 0, 1]

moves = [i for i, j in enumerate(occ_board) if j == 0]

#for i in moves:
new_board = board[:]
new_occ_board = occ_board[:]
val = minmax(1, 0, True, new_board, new_occ_board, 5)
print "move and its value:", 1, val
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
