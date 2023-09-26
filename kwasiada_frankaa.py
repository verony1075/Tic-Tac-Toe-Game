######################################################################
# Authors: Veronica Agyapong, Jalin Jones88
# Username: Agyapongv, jjjonesj
#
# Assignment: P01
# Purpose:  Make the Kwasiada game
######################################################################
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import tkinter as tk
from tkinter import ttk
import random

# Create the application window



class Board: # creating the board for the game
    """
        A class to manufacture board for game.
        """

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Kwasiada Frankaa")
        self.computer = Computer()

        self.playerturn = True
        #self.game_stop= False
       # self.playerturn.configure(text='X')

        self.d = {0: self.b1,
             1: self.b2,
             2: self.b3,
             3: self.b4,
             4: self.b5,
             5: self.b6,
             6: self.b7,
             7: self.b8,
             8: self.b9,
             }

        self.board = [] #[None] *3 for _ in range(3)]
        for i in range(3):
            row_space=[]
            for j in range(3):
             #col_space=[]
                idx = i * 3 + j
                cell = tk.Button(self.window, text='', width=30, height=12, command=self.d[idx])
                cell.grid(row=i, column=j)
                row_space.append(cell)
            self.board.append(row_space)
        self.window.mainloop()

#while True:
    #self.player.cget(text= 'X')

    def check_player_won(self):

        rows = [(self.board[0][0].cget("text") == 'X' and self.board[0][1].cget("text")== 'X' and self.board[0][2].cget("text") == 'X' ),
                (self.board[1][0].cget("text") == 'X' and self.board[1][1].cget("text") == 'X' and self.board[1][2].cget("text") == 'X' ),
                (self.board[2][0].cget("text") == 'X' and self.board[2][1].cget("text") == 'X' and self.board[2][2].cget("text") == 'X' ), # for rows
                (self.board[0][0].cget("text") == 'X' and self.board[1][1].cget("text") == 'X' and self.board[2][2].cget("text") == 'X' ),# diagonal
                (self.board[0][2].cget("text") == 'X' and self.board[1][1].cget("text") == 'X' and self.board[2][0].cget("text") == 'X' ),  # diagonal
                (self.board[0][0].cget("text") == 'X' and self.board[1][0].cget("text") == 'X' and self.board[2][0].cget("text") == 'X' ),  # col
                (self.board[0][1].cget("text") == 'X' and self.board[1][1].cget("text") == 'X' and self.board[2][1].cget("text") == 'X' ),  # col
                (self.board[0][2].cget("text") == 'X' and self.board[1][2].cget("text") == 'X' and self.board[2][2].cget("text") == 'X'),# col
              ]
        print(rows)
        if any(rows):
            return True
        else:
            return False

    def check_computer_won(self):

        col = [(self.board[0][0].cget("text") == 'O' and self.board[0][1].cget("text") == 'O' and self.board[0][2].cget("text") == 'O'),
                (self.board[1][0].cget("text") == 'O' and self.board[1][1].cget("text") == 'O' and self.board[1][2].cget("text") == 'O'),
                (self.board[2][0].cget("text") == 'O' and self.board[2][1].cget("text") == 'O' and self.board[2][2].cget("text") == 'O'),  # for rows
                (self.board[0][0].cget("text") == 'O' and self.board[1][1].cget("text") == 'O' and self.board[2][2].cget("text") == 'O'),  # diagonal
                (self.board[0][2].cget("text") == 'O' and self.board[1][1].cget("text") == 'O' and self.board[2][0].cget("text") == 'O'),  # diagonal
                (self.board[0][0].cget("text") == 'O' and self.board[1][0].cget("text") == 'O' and self.board[2][0].cget("text") == 'O'),  # col
                (self.board[0][1].cget("text") == 'O' and self.board[1][1].cget("text") == 'O' and self.board[2][1].cget("text") == 'O'),  # col
                (self.board[0][2].cget("text") == 'O' and self.board[1][2].cget("text") == 'O' and self.board[2][2].cget("text") == 'O'),  # col
                ]
        print(col)
        if any(col):
            return True
        else:
            return False

    def check_both_Tie(self):
        for row in self.board:
            for cell in row:
                if cell.cget("text") == "":
                    # if any cell is still empty, game is not tied
                    return False
        # all cells are filled and no winner has been found
        return True

    def disable_check(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j].configure(state='disabled')


    def b1(self):
        if self.board[0][0].cget('text') in ['X','O']:
            return
        if self.playerturn:
           self.board[0][0].configure(text = 'X')
        else:
            self.board[0][0].configure(text='O')

            #self.playerturn = not self.playerturn
        if self.check_player_won():
            tk.Label(self.window, text="Player won").grid(row=3)
            self.disable_check()
        if self.check_both_Tie():
            tk.Label(self.window, text="Tie!").grid(row=3)
            self.disable_check()
           # print('PLAYER WON!')

        row,col =self.computer.get_move(self.board)
        self.board[row][col].configure(text ='O')
        if self.check_computer_won():
            tk.Label(self.window, text="Computer won").grid(row=3)
            self.disable_check()
        if self.check_both_Tie():
            tk.Label(self.window, text="Tie!").grid(row=3)
            self.disable_check()
        # roor.destroy


        # comp randomly chooses 2

       # rand_key=random.choice(list(self.d.keys()))


    def b2(self):
        if self.board[0][1].cget('text') in ['X', 'O']:
            return
        if self.playerturn:
            self.board[0][1].configure(text='X')
        else:
            self.board[0][1].configure(text='O')

       # self.playerturn = not self.playerturn
        if self.check_player_won():
            tk.Label(self.window, text="Player won").grid(row=3)
            self.disable_check()
        if self.check_both_Tie():
            tk.Label(self.window, text="Tie!").grid(row=3)
            self.disable_check()

        row, col = self.computer.get_move(self.board)
        self.board[row][col].configure(text='O')
        if self.check_computer_won():
            tk.Label(self.window, text="Computer won").grid(row=3)
            self.disable_check()
        if self.check_both_Tie():
            tk.Label(self.window, text="Tie!").grid(row=3)
            self.disable_check()
    def b3(self):
        if self.board[0][2].cget('text') in ['X', 'O']:
            return
        if self.playerturn:
            self.board[0][2].configure(text='X')
        else:
            self.board[0][2].configure(text='O')
        if self.check_player_won():
            tk.Label(self.window, text="Player won").grid(row=3)
            self.disable_check()
        if self.check_both_Tie():
            tk.Label(self.window, text="Tie!").grid(row=3)
            self.disable_check()

        #self.playerturn = not self.playerturn

        row, col = self.computer.get_move(self.board)
        self.board[row][col].configure(text='O')
        if self.check_computer_won():
            tk.Label(self.window, text="Computer won").grid(row=3)
            self.disable_check()
        if self.check_both_Tie():
            tk.Label(self.window, text="Tie!").grid(row=3)
            self.disable_check()
    def b4(self):
        if self.playerturn:
            self.board[1][0].configure(text = 'X')
        else:
            self.board[1][0].configure(text='O')
        if self.check_player_won():
            tk.Label(self.window, text="Player won").grid(row=3)
            self.disable_check()
        if self.check_both_Tie():
            tk.Label(self.window, text="Tie!").grid(row=3)
            self.disable_check()
       # self.playerturn = not self.playerturn
        row, col = self.computer.get_move(self.board)
        self.board[row][col].configure(text='O')
        if self.check_computer_won():
            tk.Label(self.window, text="Computer won").grid(row=3)
            self.disable_check()
        if self.check_both_Tie():
            tk.Label(self.window, text="Tie!").grid(row=3)
            self.disable_check()
    def b5(self):
        if self.playerturn:
            self.board[1][1].configure(text = 'X')
        else:
            self.board[1][1].configure(text='O')
        #self.playerturn = not self.playerturn
        if self.check_player_won():
            tk.Label(self.window, text="Player won").grid(row=3)
            self.disable_check()
        if self.check_both_Tie():
            tk.Label(self.window, text="Tie!").grid(row=3)
            self.disable_check()
        row, col = self.computer.get_move(self.board)
        self.board[row][col].configure(text='O')
        if self.check_computer_won():
            tk.Label(self.window, text="Computer won").grid(row=3)
            self.disable_check()
        if self.check_both_Tie():
            tk.Label(self.window, text="Tie!").grid(row=3)
            self.disable_check()
    def b6(self):
        if self.playerturn:
            self.board[1][2].configure(text = 'X')
        else:
            self.board[1][2].configure(text='O')
        if self.check_player_won():
            tk.Label(self.window, text="Player won").grid(row=3)
            self.disable_check()
        if self.check_both_Tie():
            tk.Label(self.window, text="Tie!").grid(row=3)
            self.disable_check()
        #self.playerturn = not self.playerturn
        row, col = self.computer.get_move(self.board)
        self.board[row][col].configure(text='O')
        if self.check_computer_won():
            tk.Label(self.window, text="computer won").grid(row=3)
            self.disable_check()
        if self.check_both_Tie():
            tk.Label(self.window, text="Tie!").grid(row=3)
            self.disable_check()
    def b7(self):
        if self.playerturn:
            self.board[2][0].configure(text = 'X')
        else:
            self.board[2][0].configure(text='O')
        if self.check_player_won():
            tk.Label(self.window, text="Player won").grid(row=3)
            self.disable_check()
        if self.check_both_Tie():
            tk.Label(self.window, text="Tie!").grid(row=3)
            self.disable_check()
        #self.playerturn = not self.playerturn
        row, col = self.computer.get_move(self.board)
        self.board[row][col].configure(text='O')
        if self.check_computer_won():
            tk.Label(self.window, text="Computer won").grid(row=3)
            self.disable_check()
        if self.check_both_Tie():
            tk.Label(self.window, text="Tie!").grid(row=3)
            self.disable_check()
    def b8(self):
        if self.playerturn:
            self.board[2][1].configure(text = 'X')
        else:
            self.board[2][1].configure(text='O')
        if self.check_player_won():
            tk.Label(self.window, text="player won").grid(row=3)
            self.disable_check()
        #self.playerturn = not self.playerturn
        row, col = self.computer.get_move(self.board)
        self.board[row][col].configure(text='O')
        if self.check_computer_won():
            tk.Label(self.window, text="Computer won").grid(row=3)
            self.disable_check()
        if self.check_both_Tie():
            tk.Label(self.window, text="Tie!").grid(row=3)
            self.disable_check()
    def b9(self):
        if self.playerturn:
           self.board[2][2].configure(text = 'X')
        else:
            self.board[2][2].configure(text='O')
        if self.check_player_won():
            tk.Label(self.window, text="Player won").grid(row=3)
            self.disable_check()
        if self.check_both_Tie():
            tk.Label(self.window, text="Tie!").grid(row=3)
            self.disable_check()
        #self.playerturn = not self.playerturn
        row, col = self.computer.get_move(self.board)
        self.board[row][col].configure(text='O')
        if self.check_computer_won():
            tk.Label(self.window, text="Computer won").grid(row=3)
            self.disable_check()
        if self.check_both_Tie():
            tk.Label(self.window, text="Tie!").grid(row=3)
            self.disable_check()

def play(self, row, col):
    if self.board.make_move(row, col, self.current_player):
        self.display_board()
        if self.check_win():
            print("Congratulations! Player", self.current_player, "wins!")
            self.game_over = True
        elif self.check_tie():
            print("The game is a tie!")
            self.game_over = True
        else:
            self.switch_player()
    else:
        print("Invalid move. Please try again.")


class player1:
    """
        A class to manufacture player role for user.
        """

    def __init__(self):
        self.name='player1'
    def get_move(self,board):# first player move
        while True:# loop untill a valid move
            row=player1(int(input(f"{self.name},please enter row number(0,2):")))# prompt user to input a row number
            col = player1(int(input(f"{self.name}, enter col number(0,2):")))# prompt user to input a  column number
            if board[row][col] is None: # check if the cell in the board is empty or occupied by the other opponent
                return row,col  # if the cell is empty, return the row and column number





class Computer:
    """
        A class to manufature player role for computer.
        """

    def __init__(self):
        pass

    def get_move(self, board):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j].cget('text') not in ['X', 'O']]
        if not empty_cells:
            return (-1, -1)  # No empty cells available
        row, col = random.choice(empty_cells)
        return row, col



def main():
  board=Board()





main()