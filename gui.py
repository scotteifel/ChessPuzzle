import tkinter as tk

import threading

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
global NEG
global XZ
NEG = []
XZ = 0


class Program:
    def __init__(self,parent):
        self.parent = parent

        row, col = 0, 0
        background = 'brown'
        self.vars = []

        for x in range(8):
            for y in range(8):

                # var =  "var" + str(row)+str(col)
                var = tk.StringVar()
                self.vars.append(var)
                self.row = tk.Label(self.parent,padx=25,pady=25,
                            relief="groove",background=background,
                                textvariable=var)
                self.row.grid(row=row,column=col)
                col += 1
                if background == 'brown':
                    background = 'white'
                else:
                    background = 'brown'
            if background == 'brown':
                background = 'white'
            else:
                background = 'brown'
            col = 0
            row += 1

        self.state = tk.Button(self.parent,text="Start",
command = self.start_solving)
        self.state.grid(row=9,column=4)


    def start_solving(self):
        print("Start solving")
        self.solve(board,0)
        self.print_board(board)


    def place_queens(self,*args):

        #Draw chessboard
        row, col = 0, 0
        z = 0
        background = 'brown'
        l = args[0]
        for item,z in enumerate(vars):
            index_ = str(vars[z])
            if index_[6:] in l:
                print("Yes ", index_[6:])

        for x in range(8):
            for y in range(8):
                self.var = tk.StringVar()
                # self.row = tk.Label(self.parent,padx=17,pady=25,
                # relief="groove",background=background, font="bold"
                # ,textvariable=self.var)
                if (x,y) in l:
                    self.row = tk.Label(self.parent, text="Q",
                    padx=17,pady=25,relief="groove",background=background,
                    font="bold",textvariable="Q")
                    # var[]
                self.row.grid(row=row,column=col)
                col += 1
                if background == 'brown':
                    background = 'white'
                else:
                    background = 'brown'
            if background == 'brown':
                background = 'white'
            else:
                background = 'brown'
            col = 0
            row += 1
        self.parent.update()


    def solve(self, b, r):
        print("Running")
        this = str(self.vars[9])
        if this[6:] == str(9):
            print("Yes")
        print(this[6:])

        global XZ
        global NEG
        queen_total = 0

        self.place_queens(self.queen_points(b))

        for row in b:
            queen_total += row.count(1)

        for _ in range(8):

            if not self.invalid(b, (r,_)):

                if (r,_) not in NEG:
                    b[r][_] = 1

                    ##clear attempts except for the lowest row.
                    for item in NEG:
                        if item[0] <= r:
                            continue
                        else:
                            NEG.remove(item)

                    r += 1
                    if (queen_total + 1) == 8:
                        print("Yes it's true")
                        self.print_board(b)
                        print("________________________\n")

                        return True
                    return self.solve(b,r)

        if r == 0:
            NEG.append((0,XZ))
            XZ += 1
            #resetting all rows but the first one
            #to allow any space for a queen
            return self.solve(b,0)
        else:
            x,y = self.find(b)
            b[x][y] = 0
            NEG.append((x,y))
            return self.solve(b,x)


    ####Check to see if a space can have a queen in it
    def invalid(self, b, ans):
        row,col = ans

        # check column
        for x in b:
            if x[col] == 1:
                return True

        ##row by row, checks the upwards and downwards diagonal spaces.
        upwards = row-1
        #checks if the row is the first one
        if upwards != -1:
            if self.upwards_diagonals(b, col,lowest=upwards):
                return True

        downwards = row+1
        #check if the row is last one
        if downwards != 7:
            if self.downwards_diagonals(b, col,highest=downwards):
                return True

        return False


    def upwards_diagonals(self, b, column, lowest=6):
            #variables will count both to the right and left
            r_bound = column+1
            l_bound = column-1
            #count rows moving upwards starting at the row above
            #the current one
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
    def downwards_diagonals(self, b, column, highest=1):
            #variables will count both to the right and left
            l_bound = column
            r_bound = column
            #count rows downwards starting at the row below the current one
            for _ in range(highest,8):
                #Using try/except to return True
                #when a coord hits the the side of the board
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


    #Finds the furthest down queen on the board and returns it's coords.
    def find(self, b):
        for x in range(7,-1,-1):
            for y in range(7,-1,-1):
                if b[x][y] == 1:
                    return (x,y)


    def queen_points(self, b):
        count = []
        x=0
        for row in range(8):
            for col in range(8):
                if b[row][col] == 1:
                    # count.append((row,col))
                    count.append(x)
        return count

    def print_board(self,b):
        for row in b:
            print(row)


#End of tkinter class


root = tk.Tk()
root.title("Chessmaster")

app = Program(root)

root.mainloop()
