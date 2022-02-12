from distutils import command
from tkinter import *
import random

root = Tk()
root.geometry("600x600")
root.title("TicTacToe")

buttons = [[0,0,0],
            [0,0,0],
            [0,0,0]]

startTurn = 1
currentPlayer = ""

gameComplete = False

#------------
# Functions needed 

def nextTurn(row, column):
    global startTurn

    if gameComplete == True:
        gameOver()
    elif buttons[row][column]['text'] == "" and startTurn == 1:
        buttons[row][column]['text'] = "x"
        heading['text'] = "0's Turn"
        playerWon()
        startTurn = 2
    elif buttons[row][column]['text'] == "" and startTurn == 2:
         buttons[row][column]['text'] = "o"
         heading['text'] = "X's Turn"
         playerWon()
         startTurn = 1 




# 00, 01, 02 X
# 10, 11, 12 X
# 20, 21, 22 X


def playerWon():
    global gameComplete
    if buttons[0][0]['text'] == "x" and buttons[0][1]['text'] == "x" and buttons[0][2]['text'] == "x":
        print("X won")
        heading['text'] = "X Won"
        gameComplete = True
    elif buttons[1][0]['text'] == "x" and buttons[1][1]['text'] == "x" and buttons[1][2]['text'] == "x":
        print("X won")
        heading['text'] = "X Won"
        gameComplete = True
    elif buttons[2][0]['text'] == "x" and buttons[2][1]['text'] == "x" and buttons[2][2]['text'] == "x":
        print("X won")
        heading['text'] = "X Won"
        gameComplete = True
    elif buttons[0][0]['text'] == "x" and buttons[1][0]['text'] == "x" and buttons[2][0]['text'] == "x":
        print("X won")
        heading['text'] = "X Won"
        gameComplete = True
    elif buttons[0][1]['text'] == "x" and buttons[1][1]['text'] == "x" and buttons[2][1]['text'] == "x":
        print("X won")
        heading['text'] = "X Won"
        gameComplete = True
    elif buttons[0][2]['text'] == "x" and buttons[1][2]['text'] == "x" and buttons[2][2]['text'] == "x":
        print("X won")
        heading['text'] = "X Won"
        gameComplete = True
    elif buttons[0][0]['text'] == "x" and buttons[1][1]['text'] == "x" and buttons[2][2]['text'] == "x":
        print("X won")
        heading['text'] = "X Won"
        gameComplete = True
    elif buttons[0][2]['text'] == "x" and buttons[1][1]['text'] == "x" and buttons[2][0]['text'] == "x":
        print("X won")
        heading['text'] = "X Won"
        gameComplete = True
    elif buttons[0][0]['text'] == "o" and buttons[0][1]['text'] == "o" and buttons[0][2]['text'] == "o":
        print("o won")
        heading['text'] = "o Won"
        gameComplete = True
    elif buttons[1][0]['text'] == "o" and buttons[1][1]['text'] == "o" and buttons[1][2]['text'] == "o":
        print("o won")
        heading['text'] = "o Won"
        gameComplete = True
    elif buttons[2][0]['text'] == "o" and buttons[2][1]['text'] == "o" and buttons[2][2]['text'] == "o":
        print("o won")
        heading['text'] = "o Won"
        gameComplete = True
    elif buttons[0][0]['text'] == "o" and buttons[1][0]['text'] == "o" and buttons[2][0]['text'] == "o":
        print("o won")
        heading['text'] = "o Won"
        gameComplete = True
    elif buttons[0][1]['text'] == "o" and buttons[1][1]['text'] == "o" and buttons[2][1]['text'] == "o":
        print("o won")
        heading['text'] = "o Won"
        gameComplete = True
    elif buttons[0][2]['text'] == "o" and buttons[1][2]['text'] == "o" and buttons[2][2]['text'] == "o":
        print("o won")
        heading['text'] = "o Won"
        gameComplete = True
    elif buttons[0][0]['text'] == "o" and buttons[1][1]['text'] == "o" and buttons[2][2]['text'] == "o":
        print("o won")
        heading['text'] = "o Won"
        gameComplete = True
    elif buttons[0][2]['text'] == "o" and buttons[1][1]['text'] == "o" and buttons[2][0]['text'] == "o":
        print("o won")
        heading['text'] = "o Won"
        gameComplete = True
   










def disableButtons():
    pass







def gameOver():
    pass

def resetGame():
    global gameComplete
    gameComplete = False
    for row in range(3):
        for column in range(3):
            buttons[row][column] = Button(frame, height =5, width = 5, text="", command= lambda row=row, column=column: nextTurn(row, column))
            buttons[row][column].grid(row=row,column=column)
            heading['text'] = "New Game  X's Turn"


#-----------

heading = Label(text = "Player X Turn")
heading.pack()

frame = Frame(root)
frame.pack()

restartGame = Button(root, width=5, height=5, text="restart game", command=lambda:resetGame())
restartGame.pack()


for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, height =5, width = 5, text="", command= lambda row=row, column=column: nextTurn(row, column))
        buttons[row][column].grid(row=row,column=column)
        heading['text'] = "New Game  X's Turn"




root.mainloop()
