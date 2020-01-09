from tkinter import Tk, Button, Label, Menu, Frame



Turn = "X"
buttons = None
Output = None


def Start(e, root, values: list):
    root.destroy()
    root1 = Tk()
    root1.title("Tic Tac Toe")
    Frames = Frames1(root1)
    Label1(root1, [Frames])
    Buttons1(root1, [Frames])

    root1.resizable(width=False, height=False)
    root1.geometry("300x300+25+25")
    root1.mainloop()


def Frames1(root):
    Frame1 = Frame(root, width="300", height="230", bg="lightblue")
    Frame1.pack()
    Frame2 = Frame(root, width="300", height="70", bg="lightgreen")
    Frame2.pack()
    Frames = [Frame1,Frame2]
    return Frames


def Label1(root, values: list):
    Labels1 = Label(values[0][0], text="Tic Tac Toe",
                    width=45, height=2, bg="white", font=("Serif", 16))
    Labels1.place(x=-200 / 2 - 16, y=2)
    Labels2 = Label(values[0][1], width="300", height="70",bg="lightgreen")
    Labels2.pack()
    global Output
    Output = Labels2

def Buttons1(root, values: list):
    global Turn
    global buttons
    # (
    #
    # Row 1
    #
    # )
    b1 = Button(values[0][0], width=5, height=2,
                bg="white", font=("Serif", 12))
    b1.bind("<Button-1>", lambda e: [setT(b1), root.update(),
                                     Switch(), b1.configure(state="disabled")])
    b1.place(x=200 / 5 + 22, y=200 / 3)

    b5 = Button(values[0][0], width=5, height=2,
                bg="white", font=("Serif", 12))
    b5.bind("<Button-1>", lambda e: [setT(b5), root.update(),
                                     Switch(), b5.configure(state="disabled")])
    b5.place(x=200 / 5 + 56 + 56+22, y=200 / 3)

    b3 = Button(values[0][0], width=5, height=2,
                bg="white", font=("Serif", 12))
    b3.bind("<Button-1>", lambda e: [setT(b3), root.update(),
                                     Switch(), b3.configure(state="disabled")])
    b3.place(x=200 / 5 + 56+22, y=200 / 3)
    # (
    #
    # Row 2
    #
    # )

    b2 = Button(values[0][0], width=5, height=2,
                bg="white", font=("Serif", 12))
    b2.bind("<Button-1>", lambda e: [setT(b2), root.update(),
                                     Switch(), b2.configure(state="disabled")])
    b2.place(x=200 / 5+22, y=118)

    b4 = Button(values[0][0], width=5, height=2,
                bg="white", font=("Serif", 12))
    b4.bind("<Button-1>", lambda e: [setT(b4), root.update(),
                                     Switch(), b4.configure(state="disabled")])
    b4.place(x=200 / 5 + 56 + 56+22, y=118)

    b6 = Button(values[0][0], width=5, height=2,
                bg="white", font=("Serif", 12))
    b6.bind("<Button-1>", lambda e: [setT(b6), root.update(),
                                     Switch(), b6.configure(state="disabled")])
    b6.place(x=200 / 5 + 56 + 22, y=118)
    # (
    #
    # Row 3
    #
    # )

    b7 = Button(values[0][0], width=5, height=2,
                bg="white", font=("Serif", 12))
    b7.bind("<Button-1>", lambda e: [setT(b7), root.update(),
                                     Switch(), b7.configure(state="disabled")])
    b7.place(x=200 / 5 + 22, y=200 / 3 + 56 + 46)

    b8 = Button(values[0][0], width=5, height=2,
                bg="white", font=("Serif", 12))
    b8.bind("<Button-1>", lambda e: [setT(b8), root.update(),
                                     Switch(), b8.configure(state="disabled")])
    b8.place(x=200 / 5 + 56 + 22, y=118 + 51)

    b9 = Button(values[0][0], width=5, height=2,
                bg="white", font=("Serif", 12))
    b9.bind("<Button-1>", lambda e: [setT(b9), root.update(),
                                     Switch(), b9.configure(state="disabled")])
    b9.place(x=200 / 5+56+56+22, y=200 / 3 + 56+46)

    buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]


def Switch():
    global Turn
    if Turn is "X":
        Turn = "O"
    else:
        Turn = "X"


def setT(button1):
    global Turn
    if button1["text"] is "X":
        Turn1 = "X"
        button1.config(text=Turn1)
    elif button1["text"] is "O":
        Turn1 = "O"
        button1.config(text=Turn1)
    else:
        button1.config(text=Turn)
        win()


def win():
    winX = [[buttons[0]["text"] == "X", buttons[2]["text"] == "X", buttons[4]["text"] == "X"],
            [buttons[1]["text"] == "X", buttons[5]["text"]
                == "X", buttons[3]["text"] == "X"],
            [buttons[6]["text"] == "X", buttons[7]["text"]
                == "X", buttons[8]["text"] == "X"]
            ]
    winO = [[buttons[0]["text"] == "O", buttons[2]["text"] == "O", buttons[4]["text"] == "O"],
            [buttons[1]["text"] == "O", buttons[5]["text"]
                == "O", buttons[3]["text"] == "O"],
            [buttons[6]["text"] == "O", buttons[7]["text"]
             == "O", buttons[8]["text"] == "O"]
            ]
    global Output
    if winX[0][0] and winX[1][1] and winX[2][2]:
        Output["text"] = "X Wins"
    elif winX[0][2] and winX[1][1] and winX[2][0]:
        Output["text"] = "X Wins"
    elif winX[0][0] and winX[1][0] and winX[2][0]:
        Output["text"] = "X Wins"
    elif winX[0][1] and winX[1][1] and winX[2][1]:
        Output["text"] = "X Wins"
    elif winX[0][2] and winX[1][2] and winX[2][2]:
        Output["text"] = "X Wins"
    elif winX[0][0] and winX[0][1] and winX[0][2]:
        Output["text"] = "X Wins"
    elif winX[1][0] and winX[1][1] and winX[1][2]:
        Output["text"] = "X Wins"
    elif winX[2][0] and winX[2][1] and winX[2][2]:
        Output["text"] = "X Wins"
    # O wins
    elif winO[0][2] and winO[1][1] and winO[2][0]:
        Output["text"] = "O Wins"
    elif winO[0][0] and winO[1][0] and winO[2][0]:
        Output["text"] = "O Wins"
    elif winO[0][1] and winO[1][1] and winO[2][1]:
        Output["text"] = "O Wins"
    elif winO[0][2] and winO[1][2] and winO[2][2]:
        Output["text"] = "O Wins"
    elif winO[0][0] and winO[0][1] and winO[0][2]:
        Output["text"] = "O Wins"
    elif winO[1][0] and winO[1][1] and winO[1][2]:
        Output["text"] = "O Wins"
    elif winO[2][0] and winO[2][1] and winO[2][2]:
        Output["text"] = "O Wins"
    else:
        Output["text"] = "Noone Wins Draw"


