import tkinter as tk


class Program(tk.Frame):

    def __init__(self,parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        ##Draw chessboard
        row, col = 0, 0
        background = 'brown'
        for x in range(8):
            for y in range(8):
                self.row = tk.Label(self.parent, text="Space", padx=10,pady=20,
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


root = tk.Tk()
root.title("Chessmaster")

app = Program(root)


root.mainloop()
