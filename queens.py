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

def solve(b):

    if not find(b):
        r,c = 0,0

    #check for base case
    queen_total = 0
    for row in b:
        queen_total += row.count(1)
    if queen_total == 8:
        return True

    print_board(b)
    time.sleep(2)



    print("\n","Value of row is : ",r)
    print("Value of column : ",c)
    print('\n\n')
    #Iterating through board.
    if valid(b, (r,c)):
        b[r][c] = 1
        #End of the row
        r+=1
        if valid(b,(r,c+2)):
            b[r][c+2] = 1
            c += 2
        else:
            b[r][c-2] = 1
            c -= 2

    else:
        #Look for previous queen space and remove queen
        r,c = find(b)
        b[r][c] = 0

    solve(b)


####Check if space can have a queen in it
def valid(b, ans):
    row,col = ans
    print("Row is ",ans[0])
    print("Column is ",ans[1])

    # check row
    for num in b[row]:
        if num == 1:
            return False

    # check column
    list = [x[col] for x in b]
    if 1 in list:
        print("False 2")
        return False

    ##### check diagonal #####
    #check if point is top left
    if row == 0 and col == 0:
        y = 1
        for _ in range(1,8):
            if b[_][y] == 1:
                print("False 3")
                return False

            y += 1

    #point top right of board
    if row == 0 and col == 7:
        y = 6
        for _ in range(1,8):
            if b[_][y] == 1:
                print("False 4")
                return False

            y -= 1

    #bottom right of board
    if row and col == 7:
        y = 6
        for _ in range(6,-1,-1):
            if b[_][y] == 1:
                print("False 5")
                return False

            y -= 1

    #bottom left
    if row == 7 and col == 0:
        y = 1
        for _ in range(6,-1,-1):
            if b[_][y] == 1:
                print("False 6")
                return False

            y += 1

    if row == 0:
        if not downwards_diagonals(col):
            return False

    if row == 7:
        if not upwards_diagonals(col):
            return False

    ##Going row by row, checking upwards and downwards diagonals.
    upwards = row-1
    downwards = row+1

    if not upwards_diagonals(col,lowest=upwards):
        return False

    if not downwards_diagonals(col,highest=downwards):
        return False

    return True


####use variables to span out for the diagonal search.####
#downwards seeks diagonals going down
def downwards_diagonals(column, highest=1):
        #variables will count both to the right and left
        l_bound = column
        r_bound = column
        #count rows moving downwards starting at row below current row
        for _ in range(highest,8):
            ##Using try/except to stop loop when a coord reaches end of board
            print("TRYING")
            try:
                if b[_][r_bound+1] == 1:
                    return False
            except:
                continue
            try:
                if b[_][l_bound-1] == 1:
                    return False
            except:
                continue
            r_bound += 1
            l_bound -= 1
        return True

#upwards seeks diagonals going up
def upwards_diagonals(column, lowest=6):
        #variables will count both to right and to left
        r_bound = column
        l_bound = column
        #count rows moving upwards starting at the row above current
        for _ in range(lowest,-1,-1):
            try:
                if b[_][r_bound+1] == 1:
                    return False
            except:
                continue
            try:
                if b[_][l_bound-1] == 1:
                    return False
            except:
                continue
            r_bound += 1
            l_bound -= 1
        return True


def find(b):
    for x in range(8):
        for y in range(8):
            if b[x][y] == 1:
                print("Returning x and y",x,", ",y)
                return (x,y)



def print_board(b):
    for row in b:
        print(row)

solve(board)
print_board(board)
