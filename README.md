
#8 Queens Puzzle Solver
This application uses the backtracking algorithm to solve the 8 queens puzzle, a classic problem in computer science. The goal is to place 8 queens on an 8x8 chessboard in such a way that no two queens can attack each other.

Installation
To run this application, you need to have Python installed on your system. You can download Python from the official website: https://www.python.org/downloads/

Once Python is installed, follow these steps:

1.
Clone or download the repository from GitHub: https://github.com/YourUsername/ChessPuzzle
2.
Open a terminal or command prompt and navigate to the directory where you cloned the repository.
3.
Install the required dependencies by running the following command:
pip install -r requirements.txt


Usage
To start the application, run the following command in the terminal or command prompt:
python gui.py

This will open a graphical user interface (GUI) window displaying the chessboard. Click the "Solve" button to start solving the 8 queens puzzle. The application will place the queens on the board one by one, highlighting the valid positions with the correct queen image.

When the application finds a solution, it will display the queens on the board. 

To solve the puzzle again, click the "Again" button. To quit the application, click the "Quit" button.  After the last solution is found, it will display a message box asking if you want to continue and check the results or quit the program.

Code Structure
The code is organized into a class called Program which is responsible for initializing the main window, creating the chessboard, and solving the puzzle using the backtracking algorithm. The code also includes functions to check for invalid positions, find the furthest down queen on the board, and print the board to the console.

The GUI is created using the Tkinter library, which provides a simple way to create graphical user interfaces in Python. The code loads images of light and dark queens, creates labels for the squares on the chessboard, and places the queens on the board accordingly.

License
This project is licensed under the MIT License. See the LICENSE file for more information.