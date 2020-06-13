import tkinter as tk
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
#NEG and TOP_ROW store spaces the queen cannot occupy
global NEG
global TOP_ROW
#XZ used to increment the space for the top row list in solve func
global XZ
NEG = []
TOP_ROW = []
XZ = 0


class Program(tk.Frame):

    def __init__(self,parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        row, col = 0, 0
        background = 'brown'
        for x in range(8):
            for y in range(8):
                self.row = tk.Label(self.parent,padx=35,pady=35,
                relief="groove",background=background)
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
                               command=self.start_solving)
        self.state.grid(row=9,column=4)


    def start_solving(self):
        print("Start solving")
        solve(board,0)

    def printy(self):
        print("hey")
        this = self.after(30,self.printy)
        if self.row["text"]== "yes":
            self.row["text"] = "no"
        else:
            self.row["text"] = "yes"
        # time.sleep(.3)
        # self.after_cancel(this)


    def make_queen(self,*args):

        ##Draw chessboard
        row, col = 0, 0
        background = 'brown'
        l = args[0]

        for x in range(8):
            for y in range(8):
                if (x,y) in l:
                    self.row = tk.Label(self.parent, text="Queen",
                    padx=17,pady=35,relief="groove",background=background,
                    font="bold")
                else:
                    self.row = tk.Label(self.parent,padx=35,pady=35,
                    relief="groove",background=background, font="bold")


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

#End of tkinter class

def solve(b,r):

    global XZ
    global NEG
    global TOP_ROW
    queen_total = 0
    # app.make_queen(queen_points(b))
    app.printy()


    for row in b:
        queen_total += row.count(1)

    for _ in range(8):

        if not invalid(b, (r,_)):

            if (r,_) not in TOP_ROW and (r,_) not in NEG:
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

                    return True


                return solve(b,r)


    if r == 0:
        TOP_ROW.append((0,XZ))
        XZ += 1
        #resetting all rows but the first one
        #to allow any space for a queen
        NEG = []

        return solve(b,0)
    else:
        x,y = find(b)
        b[x][y] = 0

        NEG.append((x,y))
        return solve(b,x)
####Check to see if a space can have a queen in it
def invalid(b, ans):
    row,col = ans

    # check column
    for x in b:
        if x[col] == 1:
            return True

    ##row by row, checks the upwards and downwards diagonal spaces.
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


def upwards_diagonals(b, column, lowest=6):
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
def downwards_diagonals(b, column, highest=1):
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
def find(b):
    for x in range(7,-1,-1):
        for y in range(7,-1,-1):
            if b[x][y] == 1:
                return (x,y)


def queen_points(b):
    count = []
    for row in range(8):
        for col in range(8):
            if b[row][col] == 1:
                count.append((row,col))
    return count


def print_board(b):
    for row in b:
        print(row)


root = tk.Tk()
root.title("Chessmaster")

app = Program(root)

root.mainloop()
