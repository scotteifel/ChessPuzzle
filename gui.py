import tkinter as tk
from tkinter import messagebox
import time
from PIL import Image, ImageTk

from settings import *

board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]


class Program:
    def __init__(self, parent):
        """
        Initialize the main window and the chessboard.

        Parameters:
        parent (tk.Tk): The parent window where the chessboard will be displayed.

        Attributes:
        parent (tk.Tk): The parent window.
        board (list): The 8x8 chessboard represented as a 2D list.
        attempts (list): A list to store the coordinates of the queens that have been attempted to be placed.
        plotted_queens (list): A list to store the GUI labels representing the queens on the chessboard.
        top_cols (int): A counter to keep track of the topmost column to start the next attempt.
        light_squares (list): A list to store the coordinates of the light squares on the chessboard.
        light_queen (ImageTk.PhotoImage): The image of a light-colored queen.
        dark_queen (ImageTk.PhotoImage): The image of a dark-colored queen.
        start (tk.Button): The button to start solving the 8 queens problem.
        """

        self.parent = parent
        self.parent.title("8 Queens")
        self.board = board
        self.attempts = []
        self.plotted_queens = []
        self.top_cols = 0

        # Helps add the queen with the correctly-colored bg to board.
        self.light_squares = []

        # Place window near the center of the screen
        mon_width = self.parent.winfo_screenwidth()
        mon_height = self.parent.winfo_screenheight()
        x = (mon_width/2-300)
        y = (mon_height/2-300)
        self.parent.geometry("%dx%d+%d+%d" % (664, 680, x, y))

        queen_light = Image.open('Img/Queen_lighter.png')
        self.light_queen = ImageTk.PhotoImage(queen_light)
        queen_dark = Image.open('Img/Queen_darker.png')
        self.dark_queen = ImageTk.PhotoImage(queen_dark)

        # Convert the light queen image to an icon image file
        queen_light.save('light_queen_icon.ico')

        # Set the icon for the taskbar
        self.parent.wm_iconbitmap('light_queen_icon.ico')

        background = DARK_BROWN
        row, col = 0, 0
        for x in range(8):
            for y in range(8):

                self.row = tk.Label(self.parent, width=11, pady=30,
                                    relief="groove", background=background)
                self.row.grid(row=row, column=col)

                col += 1

            # Draw the chessboard
                if background == DARK_BROWN:
                    background = LIGHT_BROWN
                else:
                    background = DARK_BROWN
                    self.light_squares.append((x, y))

            if background == DARK_BROWN:
                background = LIGHT_BROWN
            else:
                background = DARK_BROWN
            col = 0
            row += 1

        self.start = tk.Button(self.parent, text="Solve",
                            command=self.start_solving)
        self.start.grid(row=10, column=3, columnspan=2, pady=6)
        print(self.light_squares)

  
    def start_solving(self):   # A new function is created to pass in 0 for first iteration
        self.start['state'] = 'disabled'
        # This is triggered if it is not the first attempt to solve.
        if len(self.plotted_queens) > 0:
            x, y = self.find()
            self.board[x][y] = 0
            self.attempts.append((x, y))
            self.plotted_queens[-1].destroy()
            self.plotted_queens.pop()
            self.solve(7)

        else:
            self.solve(0)
        self.start['state'] = 'normal'
        self.start['text'] = 'Solve again'

    def solve(self, r):
        self.parent.update()
        time.sleep(.02)
        queen_total = 0

        for row in self.board:
            queen_total += row.count(1)
        # Iterate through a row to find a space for the queen
        for _ in range(8):

            if not self.invalid((r, _)):

                if (r, _) not in self.attempts:
                    self.board[r][_] = 1

                    # Clear attempts except for row 0.
                    for item in self.attempts:
                        if item[0] <= r:
                            continue
                        else:
                            self.attempts.remove(item)

                    # Get a new variable for each placed queen on gui
                    queen_index = "queen"+str(r)

                    # Find the squares bg color and add queen img accordingly
                    if ((r, _) in self.light_squares):
                        queen_index = tk.Label(
                            self.parent, image=self.light_queen, bg=LIGHT_BROWN)
                    else:
                        queen_index = tk.Label(
                            self.parent, image=self.dark_queen, bg=DARK_BROWN)

                    queen_index.grid(row=r, column=_)
                    self.plotted_queens.append(queen_index)
                    r += 1

                    # Check for the base case
                    if (queen_total + 1) == 8:
                        return True
                    return self.solve(r)

        if r == 0:
            self.attempts.append((0, self.top_cols))
            self.top_cols += 1
            try:
                self.plotted_queens[0].destroy()
            except:
                ok = messagebox.askokcancel(message="Last solution reached.  Click OK to continue or cancel to quit.")
                if ok:
                    pass
                else:
                    root.destroy()
                self.start.configure(text='Quit', command=self.parent.destroy)
                return True
            return self.solve(0)

        else:
            x, y = self.find()
            self.board[x][y] = 0
            self.attempts.append((x, y))
            self.plotted_queens[-1].destroy()
            self.plotted_queens.pop()
            return self.solve(x)


    def invalid(self, ans):    # Check to see if a space can have a queen
        row, col = ans

        # Check column
        for x in self.board:
            if x[col] == 1:
                return True

        # Checks if row is the first one
        if row != 0:

            # Count the rows moving upwards, starting
            # on the above row
            r_bound = col+1
            l_bound = col-1

            for _ in range(row-1, -1, -1):
                if r_bound < 8:
                    if self.board[_][r_bound] == 1:
                        return True
                r_bound += 1

                if l_bound > -1:
                    if self.board[_][l_bound] == 1:
                        return True
                l_bound -= 1

        return False

    # Find the furthest down queen on the board and returns it's
    # coordinates.
    def find(self):
        for x in range(7, -1, -1):
            for y in range(7, -1, -1):
                if self.board[x][y] == 1:
                    return (x, y)

    # Print the board to the console.
    def print_board(self):
        for row in self.board:
            print(row)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("8 Queens")

    app = Program(root)
    root.mainloop()
