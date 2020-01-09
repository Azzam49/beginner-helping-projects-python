theBoard = {'TL': 'b', 'TM': 'b', 'TR': 'b',
            'ML': 'b', 'MM': 'b', 'MR': 'b',
            'BL': 'b', 'BM': 'b', 'BR': 'b'}

def printBoard(brd):
    print(brd['TL'] + "|" + brd['TM'] + "|" + brd['TR'])
    
    print("-----")
    
    print(brd['ML'] + "|" + brd['MM'] + "|" + brd['MR'])

    print("-----")

    print(brd['BL'] + "|" + brd['BM'] + "|" + brd['BR'])

# Logic to check a winner
def getWinStatus(brd):
    result = False
    if (brd ['TL'] == brd['TM'] == brd['TR'] != 'b'):
        result = True
    elif (brd ['ML'] == brd['MM'] == brd['MR'] != 'b'):
        result = True  
    elif (brd ['BL'] == brd['BM'] == brd['BR'] != 'b'):
        result = True  
    elif (brd['TL'] == brd['MM'] == brd['BR'] != 'b'):
        result = True
    elif (brd['TR'] == brd['MM'] == brd['BL'] != 'b'):
        result = True
    elif (brd['TL'] == brd['ML'] == brd['BL'] != 'b'):
        result = True
    elif (brd['TM'] == brd['MM'] == brd['BM'] != 'b'):
        result = True
    elif (brd['TR'] == brd['MR'] == brd['BR'] != 'b'):
        result = True
    return result



printBoard(theBoard)


Q = False
turn = 'x'
isWin = getWinStatus(theBoard)
moves = ["TL","TM","TR","ML","MM","MR","BL","BM","BR"]
print("Moves : TL,TM,TR,ML,MM,MR,BL,BM,BR.")

# i Integer used to count the moves , each loop it gets +1 , at 9 our loop gets break as board gets full.
i = 0

# while we didnt Quit(Q) or a winner found, our game will continue until the board gets a Tie.
while not Q and not isWin:
    print("Turn for " + turn + ".")
    move = input("Enter Your Move : ")
    if move == 'Q':
        isWin = True

    # if our move not a valid one from the moves list, our loop will ignore
    # the below coding after printing"Incorrect move" and continue.
    if move.upper() not in moves:
        print("Incorrect move")
        continue

    # update the value of our dictonary key.
    theBoard[move.upper()] = turn
     
    if turn == 'x':
        turn = 'o'
    else:
        turn = 'x'

    
    isWin = getWinStatus(theBoard)
    printBoard(theBoard)
    
    i += 1
    if i == 9:
        break


# if a winner , will print it.
# else we call our board and a tie.
if isWin == True:
    printBoard(theBoard)
    if turn == "o":
        print("x" + " Win")
    else:
        print("o" + " Win")
else:
    printBoard(theBoard)
    print("Its a Tie!")

