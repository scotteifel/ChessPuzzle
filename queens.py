import time
#Chessboard
board = [
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
]
#neg and top_row store spaces the queen cannot occupy
global neg
global top_row
#xz used to increment the space for the top row list in solve func
global xz
xz = 0
top_row = []
neg = []


def solve(b,r):
    global xz
    global neg
    global top_row
    queen_total = 0

    for row in b:
        queen_total += row.count(1)

    for _ in range(8):

        if not invalid(b, (r,_)):

            if (r,_) not in top_row and (r,_) not in neg:
                b[r][_] = 1

                ##clear attempts except for the lowest row.
                for item in neg:
                    if item[0] <= r:
                        continue
                    else:
                        neg.remove(item)

                r += 1
                if (queen_total + 1) == 8:
                    return True

                return solve(b,r)

    if r == 0:
        top_row.append((0,xz))
        xz += 1
        ##Resetting the lower rows to allow any space for a queen
        neg = []
        return solve(b,0)
    else:
        x,y = find(b)
        b[x][y] = 0

        neg.append((x,y))
        return solve(b,x)


####Check if space can have a queen in it
def invalid(b, ans):
    row,col = ans

    # check column
    for x in b:
        if x[col] == 1:
            return True

    ##row by row, checks upwards and downwards diagonal spaces.
    upwards = row-1
    #checks if the row is the first one
    if upwards != -1:
        if upwards_diagonals(b, col,lowest=upwards):
            return True

    downwards = row+1
    #check if the row is last one
    if downwards != 7:
        if downwards_diagonals(b, col,highest=downwards):
            return True

    return False


# def upwards_diagonals1(b, column, lowest=6):
#         #variables will count both to right and to left
#         r_bound = column+1
#         l_bound = column-1
#         #count rows moving upwards starting at the row above current
#         for _ in range(lowest,-1,-1):
#             if r_bound < 7:
#                 if b[_][r_bound] == 1:
#                     return True
#
#             r_bound += 1
#             if l_bound > -1:
#                 if b[_][l_bound] == 1:
#                     return True
#             l_bound -= 1
#         return False

def upwards_diagonals(b, column, lowest=6):
        #variables will count both to right and to left
        r_bound = column+1
        l_bound = column-1
        #count rows moving upwards starting at the row above current
        for _ in range(lowest,-1,-1):
            if r_bound < 7:
                if b[_][r_bound] == 1:
                    return True

            r_bound += 1
            if l_bound > -1:
                if b[_][l_bound] == 1:
                    return True
            l_bound -= 1
        return False


#seeks diagonals going down
def downwards_diagonals(b, column, highest=1):
        #variables will count both to the right and left
        l_bound = column
        r_bound = column
        #count rows moving downwards starting at row below current row
        for _ in range(highest,8):
            ##Using try/except to stop loop when a coord side end of board
            try:
                if b[_][r_bound+1] == 1:
                    return True
            except:
                pass
            try:
                if b[_][l_bound-1] == 1:
                    return True
            except:
                pass
            r_bound += 1
            l_bound -= 1
        return False


def find(b):
    for x in range(7,-1,-1):
        for y in range(7,-1,-1):
            if b[x][y] == 1:
                return (x,y)


def print_board(b):
    for row in b:
        print(row)


solve(board,0)
print_board(board)
