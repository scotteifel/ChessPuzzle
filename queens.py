#8x8
import time
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

    # rslt = find(b)
    # if not rslt:
    #     return True
    # else:
    #     row,col = rslt

    print_board(b)
    print('\n\n')
    time.sleep(.5)
    r,c = 0,0
    while r != 7 and c != 7:
            #Iterating through board.
            if valid(b, (r,c)):
                b[r][c] = 1
                #End of the row
                if c == 7:
                    c = 0
                    r += 1
                else:
                    c += 1
            else:
                b[r][c] = 0
                if c == 0 and r != 0:
                    r -= 1
                    c == 7
                    
                else:
                    c -= 1

                # solve(b)

    print("NOT SOLVE B")
    return True
            # if valid(b, (row,col)):
            #     b[row][col] = 1
            # else:
            #     b[row][col] = 0
            #
            # if solve(b):
            #     return True
            # print("NOT SOLVE B")


def valid(b, ans):
    row,col = ans
    print("Row is ",row)
    print("Column is ",col)

# check row
    for item in b[row]:
        if item == 1 and item != col:
            return False

# check column
    list = [x[col] for x in b]
    if 1 in list and b[row][col] != 1:
        print("False 2")
        return False

# check diagonal
    #Check if point is upper left:
    if row and col == 0:
        y = 1
        for _ in range(7):
            if b[_][y] == 1:
                print("False 3")

                return False
            y += 1
    #Point top right of board
    if row == 0 and col == 7:
        y = 6
        for _ in range(7):
            if b[_][y] == 1:
                print("False 4")

                return False
            y -= 1
    #Bottom right of board
    if row and col == 7:
        y = 6
        for _ in range(6,-1):
            if b[_][y] == 1:
                print("False 5")

                return False
            y -= 1
    #Bottom left
    if row == 7 and col == 0:
        y = 6
        for _ in range(6,-1):
            if b[_][y] == 1:
                print("False 6")

                return False
            y -= 1
    #Using x and y to span out for the diagonal search.
    if row == 0:
        x = col
        y = col
        print("Here i am.")
        for _ in range(6):
            print("TRYING")
            try:
                if b[_][y+1] == 1:
                    return False
            except:
                continue
            try:
                if b[_][x-1] == 1:
                    return False
            except:
                continue
            y += 1
            x -= 1

    print("And here too")
    if row == 7:
        x = col
        y = col
        for _ in range(6,-1):
            try:
                if b[_][y+1] == 0:
                    return False
            except:
                continue
            try:
                if b[_][x-1] == 0:
                    return False
            except:
                continue
            y += 1
            x -= 1
    print("Truth")
    return True

def find(b):
    for x in range(8):
        for y in range(8):
            if b[x][y] == 0:
                print("Returning x and y",x,", ",y)
                return (x,y)



def print_board(b):
    for row in b:
        print(row)

solve(board)
print(board)
