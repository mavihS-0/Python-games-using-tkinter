import tkinter  
import tkinter.messagebox

def TicTacToe():
    import tictactoe

def RockPaperScissors():
    import rps
    
tk=tkinter.Tk()
tk.geometry('200x120')
tk.title("Games")
var=tkinter.StringVar()
label=tkinter.Label(tk,textvariable=var)
var.set("GAMES")
label.pack(pady=10)
ttt=tkinter.Button(tk,text="TIC TAC TOE",command=TicTacToe)
ttt.pack(pady=3)
rps=tkinter.Button(tk,text="Rock Paper Scissors", command=RockPaperScissors)
rps.pack()
tk.mainloop()