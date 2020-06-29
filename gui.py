
import tkinter as tk
from tkinter import messagebox
import time
from PIL import Image, ImageTk
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

class Program:
    def __init__(self,parent):

        self.parent = parent
        self.vars = []
        self.attempts = []
        self.placed_queens = []
        self.XZ = 0
        img = Image.open('Chessqueen111.png')
        self.img = ImageTk.PhotoImage(img)

        queen_index = ""
        row, col = 0, 0
        background = 'brown'

        for x in range(8):
            for y in range(8):

                var = tk.StringVar()
                self.vars.append(var)
                self.row = tk.Label(self.parent,width=11,pady=30,
relief="groove",background=background,textvariable=var,font="bold")

                self.row.grid(row=row,column=col)
                col += 1

            #Draw the chessboard
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

    def solve(self, b, r):
        self.parent.update()
        time.sleep(.3)
        queen_total = 0

        for row in b:
            queen_total += row.count(1)
        #Iterate through a row to find a space for the queen
        for _ in range(8):

            if not self.invalid(b, (r,_)):

                if (r,_) not in self.attempts:
                    b[r][_] = 1

                    ##clear attempts except for row 0.
                    for item in self.attempts:
                        if item[0] <= r:
                            continue
                        else:
                            self.attempts.remove(item)
                    #Get a new variable for each placed queen on gui
                    queen_index = "queen"+str(r)
                    queen_index = tk.Label(self.parent, image=self.img)
                    queen_index.grid(row=r,column=_)
                    self.placed_queens.append(queen_index)
                    r += 1

                    if (queen_total + 1) == 8:
                        self.print_board(b)
                        return True
                    return self.solve(b,r)

        if r == 0:
            self.attempts.append((0,self.XZ))
            self.XZ += 1
            self.placed_queens[0].destroy()
            #resetting all tried spaces but the first rows
            #to allow any space for a queen
            return self.solve(b,0)

        else:
            x,y = self.find(b)
            b[x][y] = 0
            self.attempts.append((x,y))
            self.placed_queens[-1].destroy()
            self.placed_queens.pop()
            return self.solve(b,x)

    ####Check to see if a space can have a queen
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
            r_bound = col+1
            l_bound = col-1

            for _ in range(row-1,-1,-1):
                if r_bound < 8:
                    if b[_][r_bound] == 1:
                        return True
                r_bound += 1

                if l_bound > -1:
                    if b[_][l_bound] == 1:
                        return True
                l_bound -= 1

        return False


    #find the furthest down queen on the board and returns it's coords.
    def find(self, b):
        for x in range(7,-1,-1):
            for y in range(7,-1,-1):
                if b[x][y] == 1:
                    return (x,y)


    def queen_points(self, b):
        #return the coordinates of spaces containing a queen
        count = []
        for row in range(8):
            for col in range(8):
                if b[row][col] == 1:
                #the coords are in a tuple, index is joined for each entry
                    count.append([(str(row),str(col)),self.queen_index])
                self.queen_index += 1
        return count

    def print_board(self,b):
        for row in b:
            print(row)


root = tk.Tk()
root.title("8 Queens")

app = Program(root)
root.mainloop()
