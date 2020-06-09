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
not_poss = []
global xz
xz = 0
def solve(b,r):
    print("running solve")
    global xz
    #check for base case
    queen_total = 0
    for row in b:
        queen_total += row.count(1)
    if queen_total == 8:
        print("Correct amount of queens")
        return True

    time.sleep(1)

    #Iterating through board.
    for _ in range(8):
        neg = []

        if not invalid(b, (r,_)):
            print("Not invalid", r,_)
            print(not_poss)

            if (r,_) not in not_poss and (r,_) not in neg:
                b[r][_] = 1
                print('\n\n\n')
                print_board(b)
                print('\n\n\n')
                r += 1
                solve(b,r)
        else:
            if r == 0:
                not_poss.append((0,xz))
                xz += 1

                solve(b,r)
            else:
                x,y = find(b)
                b[x][y] = 0
                neg.append((x,y))
                solve(b,r-1)

        print("here")

        #Look for previous queen space and remove queen
    # r,c = find(b)
    # for row in b:
    #     if 1 not in row:
    #         primary_q.append((r,c))
    #         solve(b,r)
    # not_poss.append((r,c))
    # b[r][c] = 0


    return True




####Check if space can have a queen in it
def invalid(b, ans):
    row,col = ans

    # check row
    # for num in b[row]:
    #     if num == 1:
    #         return True

    # check column
    for x in b:
        if x[col] == 1:
                return True
    ##### check diagonal #####
    #check if point is top left
    if row == 0 and col == 0:
        y = 1
        for _ in range(1,8):
            if b[_][y] == 1:
                return True

            y += 1
    #point top right of board
    if row == 0 and col == 7:
        y = 6
        for _ in range(1,8):
            if b[_][y] == 1:
                return True

            y -= 1
    #bottom right of board
    if row and col == 7:
        y = 6
        for _ in range(6,-1,-1):
            if b[_][y] == 1:
                return True

            y -= 1
    #bottom left

    if row == 7 and col == 0:
        y = 1
        for _ in range(6,-1,-1):
            if b[_][y] == 1:
                return True

            y += 1

    if row == 0:
        if downwards_diagonals(b,col):
            return True


    if row == 7:
        if upwards_diagonals(b,col):
            return True

    ##Going row by row, checking upwards and downwards diagonals.
    upwards = row-1
    if upwards != -1:
        if upwards_diagonals(b, col,lowest=upwards):
            return True


    downwards = row+1
    if downwards != 7:

        if downwards_diagonals(b, col,highest=downwards):
            return True

    return False


####use variables to span out for the diagonal search.####

#seeks diagonals going up
def upwards_diagonals(b, column, lowest=6):
        #variables will count both to right and to left
        r_bound = column
        l_bound = column
        #count rows moving upwards starting at the row above current
        for _ in range(lowest,-1,-1):
            try:
                if b[_][r_bound+1] == 1:
                    return True
            except:
                pass
            r_bound += 1
        for _ in range(lowest,-1,-1):
            try:
                if b[_][l_bound-1] == 1:
                    return True
            except:
                pass
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
                continue
            try:
                if b[_][l_bound-1] == 1:
                    return True
            except:
                continue
            r_bound += 1
            l_bound -= 1
        return False




def find(b):
    for x in range(8):
        for y in range(8):
            if b[x][y] == 1:
                return (x,y)



def print_board(b):
    for row in b:
        print(row)

solve(board,0)
print_board(board)
