import copy
import random

#initializing
board = ['-' for i in range(9)]
ctr = 0
turn = 0

def occupied(board):
    return [0 if space == '-' else 1 for space in board]

#check if game is over
def gameover (b):
    for player in ['x', 'o']:
        winning_threes = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
        for row in winning_threes:
            if all([b[ind] == player for ind in row]):
                return True
    return False

# check if node n is the winning move
def winningMove (n, b, p):
    if p:
        b[n] = 'o'
    else:
        b[n] = 'x'
    is_win = gameover(b)
    b[n] = '-'
    return is_win


def printboard (board):
    print "********"
    print board[0], board[1], board[2]
    print board[3], board[4], board[5]
    print board[6], board[7], board[8]

def minmax (node, depth, maxPlayer, board, m):
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
    # update copy of board and occ_board
    if maxPlayer:
        n_board[node] = 'o'
    else:
        n_board[node] = 'x'
    # list of possible nodes
    pos_moves = [i for i, j in enumerate(occupied(n_board)) if j == 0]
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
    pos_moves = [i for i, j in enumerate(occupied(board)) if j == 0]
    # *** if playing bot and 1, change bestVal to float("inf") ***
    bestVal = -float("inf")
    node = float("inf")
    for i in pos_moves:
        new_board = copy.deepcopy(board)
        # *** if playing bot and 1, change to False
        val = minmax(i, 0, True, new_board, len(pos_moves))
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
            if not(occupied(board)[i]):
                ctr += 1
                if turn == 0:
                    board[i] = 'x'
                    turn = 1
                else:
                    board[i] = 'o'
                    turn = 0
            else:
                print "Occupied, please choose a valid move!"
    printboard(board)
