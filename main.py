from tkinter import *   
from tkinter import messagebox

# -------------------------------------------------

window  = Tk()
window.geometry("273x259")
window.title("Tic-Tac-Toe")
icon = PhotoImage(file="C:\\Users\\Youssef\\Desktop\\Python\\Projects\\Tic-Tac-Toe Game\\icon.png")
window.iconphoto(True , icon)

# -------------------------------------------------

# Create Buttons 

# -------------------------------------------------

def Ask_User(player):
    if (player == 0) : answer = messagebox.askretrycancel("GAME END", "GAME ENDED WITH DRAW")
    else : answer = messagebox.askretrycancel("GAME END" , f"PLAYER WITH {Current_Player} HAS WIN")
    if (answer == True) : Restart_Game()
    else : window.destroy()

def Restart_Game():
    for row in buttons :
        for button in row :
            button.config(text="", state=NORMAL)

    global Current_Player

    Current_Player = "X"

frame = Frame(window)
frame.pack()

Current_Player = "X"

def click(button):

    global Current_Player

    if (Current_Player == "X") :

        button.config(text="X")
        button.config(state=DISABLED)

        if check_winner(buttons , "X") : Ask_User(1)

        if check_draw(buttons) : Ask_User(0)

        Current_Player = "O"

    else :
        button.config(text="O")
        button.config(state=DISABLED)

        if check_winner(buttons , "O") : Ask_User(2)

        if check_draw(buttons) : Ask_User(0)

        Current_Player = "X"


def check_winner(board,mark):
    # Check rows, columns, and diagonals
    return (
        (board[0][0].cget("text") == mark and board[0][1].cget("text") == mark and board[0][2].cget("text") == mark) or  # Row 1
        (board[1][0].cget("text") == mark and board[1][1].cget("text") == mark and board[1][2].cget("text") == mark) or  # Row 2
        (board[2][0].cget("text") == mark and board[2][1].cget("text") == mark and board[2][2].cget("text") == mark) or  # Row 3
        (board[0][0].cget("text") == mark and board[1][0].cget("text") == mark and board[2][0].cget("text") == mark) or  # Column 1
        (board[0][1].cget("text") == mark and board[1][1].cget("text") == mark and board[2][1].cget("text") == mark) or  # Column 2
        (board[0][2].cget("text") == mark and board[1][2].cget("text") == mark and board[2][2].cget("text") == mark) or  # Column 3
        (board[0][0].cget("text") == mark and board[1][1].cget("text") == mark and board[2][2].cget("text") == mark) or  # Diagonal 1
        (board[0][2].cget("text") == mark and board[1][1].cget("text") == mark and board[2][0].cget("text") == mark)     # Diagonal 2
    )

def check_draw(board):
    for row in board : 
        for button in row :
            if button.cget("text") == "" : return False
    return True

# Initialize a 3x3 matrix (list of lists) to store buttons
buttons = [[None for _ in range(3)] for _ in range(3)]

# Create buttons and place them in the matrix
button1 = Button(frame, height=4, width=9, font=35, command=lambda: click(button1))
button1.grid(row=0, column=0)
buttons[0][0] = button1  # Append button to the correct position in the matrix

button2 = Button(frame, height=4, width=9, font=35, command=lambda: click(button2))
button2.grid(row=0, column=1)
buttons[0][1] = button2

button3 = Button(frame, height=4, width=9, font=35, command=lambda: click(button3))
button3.grid(row=0, column=2)
buttons[0][2] = button3

button4 = Button(frame, height=4, width=9, font=35, command=lambda: click(button4))
button4.grid(row=1, column=0)
buttons[1][0] = button4

button5 = Button(frame, height=4, width=9, font=35, command=lambda: click(button5))
button5.grid(row=1, column=1)
buttons[1][1] = button5

button6 = Button(frame, height=4, width=9, font=35, command=lambda: click(button6))
button6.grid(row=1, column=2)
buttons[1][2] = button6

button7 = Button(frame, height=4, width=9, font=35, command=lambda: click(button7))
button7.grid(row=2, column=0)
buttons[2][0] = button7

button8 = Button(frame, height=4, width=9, font=35, command=lambda: click(button8))
button8.grid(row=2, column=1)
buttons[2][1] = button8

button9 = Button(frame, height=4, width=9, font=35, command=lambda: click(button9))
button9.grid(row=2, column=2)
buttons[2][2] = button9


window.mainloop()