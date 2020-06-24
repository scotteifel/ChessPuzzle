
import tkinter as tk
from tkinter import messagebox
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
global NEG
global XZ
NEG = []
XZ = 0

class Program:
    def __init__(self,parent):

        self.parent = parent
        self.vars = []
        row, col = 0, 0
        background = 'brown'

        for x in range(8):
            for y in range(8):

                var = tk.StringVar()
                self.vars.append(var)
                self.row = tk.Label(self.parent,width=11,pady=25,
                                    relief="groove",background=background,
                                    textvariable=var,font="bold")
                self.row.grid(row=row,column=col)
                col += 1
                #Draws the chessboard
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

        self.state = tk.Button(self.parent,text="Solve", pady=3,
                               command = self.start_solving)
        self.state.grid(row=10,column=3, columnspan=2)


    #A new function is created to pass in 0 for first iteration
    def start_solving(self):
        self.solve(board,0)
        ok = messagebox.askokcancel(
        message="Complete")

    def place_queens(self,*args):

        #Draw chessboard
        row, col = 0, 0
        z = 0
        background = 'brown'
        l = args[0]

        for item in self.vars:
            index_ = str(item)
            #Start at 6 to get the index of the variable eg. PYVAR01
            if index_[6:] in l:
                item.set("Q")
            else:
                item.set("")
        time.sleep(.4)
        self.parent.update()


    def solve(self, b, r):
        global XZ
        global NEG
        queen_total = 0

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
                    self.place_queens(self.queen_points(b))

                    if (queen_total + 1) == 8:
                        self.print_board(b)
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

        #checks if the row is the first one
        if row != 0:
            #count the rows moving upwards starting
            #on the above row
            if self.upwards_diagonals(b, col,row-1):
                return True

        return False


    def upwards_diagonals(self, b, column, row):
            #vars will count to the right and left
            r_bound = column+1
            l_bound = column-1

            for _ in range(row,-1,-1):
                if r_bound < 8:
                    if b[_][r_bound] == 1:
                        return True
                r_bound += 1

                if l_bound > -1:
                    if b[_][l_bound] == 1:
                        return True
                l_bound -= 1
            return False


    #Finds the furthest down queen on the board and returns it's coords.
    def find(self, b):
        for x in range(7,-1,-1):
            for y in range(7,-1,-1):
                if b[x][y] == 1:
                    return (x,y)


    def queen_points(self, b):
        #Returns the spaces containing a queen
        count = []
        x = 0

        for row in range(8):
            for col in range(8):
                if b[row][col] == 1:
                    count.append(str(x))
                x += 1
        return count

    def print_board(self,b):
        for row in b:
            print(row)


root = tk.Tk()
root.title("8 Queens")

app = Program(root)

root.mainloop()
