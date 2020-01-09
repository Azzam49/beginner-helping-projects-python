from tkinter import Tk,Button,Frame,Label
from Game import Start
import threading
root = Tk()

def Root():
    # Root Window For Game
    
    root.title("TIC TAC TOE")
    Frames = Frames1(root)
    Label1(root,[Frames])
    Menu1(root, [Frames])
    
    root.resizable(width=False,height=False)
    root.geometry("300x250+50+50")
    root.mainloop()
    

def Frames1(root):
    Frame1 = Frame(root,width="300",height="300", bg="lightblue")
    Frame1.pack()
    Frames = [Frame1]
    return Frames

def Label1(root, values: list):
    Labels1 = Label(values[0][0], text="Tic Tac Toe", width=45, height=2, bg="white", font=("Serif", 16))
    Labels1.place(x=-200/2-16,y=2)


def Menu1(root, values: list):
    
    newGame = Button(values[0][0],text="New Game",width=30,height=2,bg="lightgreen")
    newGame.bind("<Button-1>",lambda e: Start(e,root,[]) ,root.update)
    newGame.place(x=200 / 5, y=200 - 80)
    
    




def caller():
    Root()
    
    


caller()
