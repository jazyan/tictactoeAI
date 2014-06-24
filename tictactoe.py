import copy
import random

#initializing
board = ['-' for i in range(9)]
occ_board = [0 for i in range(9)]
ctr = 0
turn = 0

#check if game is over
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

# check if node n is the winning move
def winningMove (n, b, p):
    cp = copy.deepcopy(b)
    if p:
        cp[n] = 'o'
    else:
        cp[n] = 'x'
    return gameover (cp)

def printboard (board):
    print "********"
    print board[0], board[1], board[2]
    print board[3], board[4], board[5]
    print board[6], board[7], board[8]

def minmax (node, depth, maxPlayer, board, occ_board, m):
    # check if node is terminal
    if (depth == (m-1)) or winningMove(node, board, maxPlayer):
        if winningMove(node, board, maxPlayer) and (maxPlayer == True):
            return (10 - depth)
        elif winningMove(node, board, maxPlayer) and (maxPlayer == False):
            return (depth - 10)
        else:
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
    # min the max value if you're maxPlayer
    if maxPlayer:
        bestValue = float("inf")
        for i in pos_moves:
            value = minmax(i, depth+1, False, n_board, n_occ_board, m)
            bestValue = min(bestValue, value)
        return bestValue
    # max the min value if you're not maxPlayer
    else:
        bestValue = -float("inf")
        for i in pos_moves:
            value = minmax(i, depth+1, True, n_board, n_occ_board, m)
            bestValue = max(bestValue, value)
        return bestValue

# execute below until game over (won or 9 spaces filled)
while (not(gameover (board))):
    if (ctr == 9):
        break;
    # * uncomment below to play against bot, 0 to go first, 1 for second *
    #if turn == 1:
    #    node = int(raw_input())
    #else:
    # ** indent below to play bot **
    pos_moves = [i for i, j in enumerate(occ_board) if j == 0]
    # *** if playing bot and 1, change bestVal to float("inf") ***
    bestVal = -float("inf")
    node = float("inf")
    for i in pos_moves:
        new_board = copy.deepcopy(board)
        new_occ_board = copy.deepcopy(occ_board)
        # *** if playing bot and 1, change to False
        val = minmax(i, 0, True, new_board, new_occ_board, len(pos_moves))
        # *** if playing bot and 1, change to (val < bestVal) ***
        if (val > bestVal):
            node = i
            bestVal = val
        if (val == bestVal):
            rand = random.randint(1,20)
            if rand <= 10:
                node = i
    # ** end indent **
    for i in range(9):
        if node == i:
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
    printboard(board)
