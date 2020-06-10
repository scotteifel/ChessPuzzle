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
##store spaces queen cannot have
global xz
global neg
global top_row
top_row = []
xz = 0
neg = []


def solve(b,r):
    global xz
    global neg
    global top_row
    queen_total = 0

    for row in b:
        queen_total += row.count(1)
    if queen_total == 8:
        print("Correct amount of queens")
        print_board(b)
        print("Nice one!")
        return True
    if queen_total == 7:
        print('\n')
        print_board(b)
        print('\n')
        print(r, " r is this")

    # print('\n')
    # print_board(b)
    # print('\n')
    # time.sleep(1)

    #Iterating through the board.
    for _ in range(8):

        if not invalid(b, (r,_)):

            #Check for base case.  Row 7 was solved.
            if r == 8:
                print("ROW 8 IS 8")
                time.sleep(5)
                return True

            if (r,_) not in top_row and (r,_) not in neg:
                b[r][_] = 1

                ##clear attempts except for the lowest row.

                for item in neg:
                    if item[0] <= r:
                        continue
                    else:
                        neg.remove(item)

                r += 1
                solve(b,r)


    if r == 0:
        top_row.append((0,xz))
        xz += 1
        ##Resetting the lower rows to allow any space for a queen
        neg = []
        solve(b,0)
    else:
        x,y = find(b)
        b[x][y] = 0

        neg.append((x,y))
        solve(b,x)

    return True


####Check if space can have a queen in it
def invalid(b, ans):
    row,col = ans

    # check column
    for x in b:
        if x[col] == 1:
            return True


    # if row == 0:
    #     if downwards_diagonals(b,col):
    #         return True

    if row == 7:
        if upwards_diagonals1(b,col):
            return True

    ##Going row by row, checking upwards and downwards diagonals.
    upwards = row-1
    #check if the row is the first one
    if upwards != -1:
        if upwards_diagonals(b, col,lowest=upwards):
            return True

    downwards = row+1
    #check if the row is last one
    if downwards != 7:
        if downwards_diagonals(b, col,highest=downwards):
            return True

    return False
# 7 4


def upwards_diagonals1(b, column, lowest=6):
        #variables will count both to right and to left
        r_bound = column+1
        l_bound = column-1
        print("This is left and right ",l_bound,r_bound)
        #count rows moving upwards starting at the row above current
        for _ in range(lowest,-1,-1):
            print("HERE")
            if r_bound < 7:
                if b[_][r_bound] == 1:
                    print("HERE 1: ",  _)
                    return True

            r_bound += 1
            if l_bound > -1:
                if b[_][l_bound] == 1:
                    print("B _ lbound is ",b[_][l_bound])
                    print("HERE 2: ",  _,l_bound)
                    return True
            print("Decrementing lbound", l_bound)
            l_bound -= 1
        return False

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
# def upwards_diagonals1(b, column, lowest=6):
#         #variables will count both to right and to left
#         r_bound = column
#         l_bound = column
#         print("This is left and right ",l_bound,r_bound)
#         #count rows moving upwards starting at the row above current
#         for _ in range(lowest,-1,-1):
#             try:
#                 if b[_][r_bound+1] == 1:
#                     print("HERE 1: ",  _)
#                     return True
#             except:
#                 pass
#             r_bound += 1
#             try:
#                 if b[_][l_bound-1] == 1:
#                     print("B _ lbound is ",b[_][l_bound-1])
#                     print("HERE 2: ",  _,l_bound-1)
#                     return True
#             except:
#                 pass
#             print("Decrementing lbound", l_bound)
#             l_bound -= 1
#         return False

#seeks diagonals going up




# def upwards_diagonals1(b, column, lowest=6):
#         #variables will count both to right and to left
#         r_bound = column
#         l_bound = column
#         #count rows moving upwards starting at the row above current
#         for _ in range(lowest,-1,-1):
#             try:
#                 if b[_][r_bound+1] == 1:
#                     print("HERE 1: ",  _)
#                     return True
#             except:
#                 pass
#             r_bound += 1
#         for _ in range(lowest,-1,-1):
#             try:
#                 if b[_][l_bound-1] == 1:
#                     print("HERE 2: ",  _,l_bound-1)
#                     return True
#             except:
#                 pass
#             print("Incrementing lbound", l_bound)
#             l_bound -= 1
#         return False

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
