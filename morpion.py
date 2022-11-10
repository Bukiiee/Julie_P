import subprocess as subpcs
from operator import xor
from colorama import Fore, Back

grid = [[0,0,0],
        [0,0,0],        
        [0,0,0]]



def GetA (liste):
    return liste[0]

def GetB (liste):
    return liste[1]



#Function to choose la case (jsp comment on le dit en anglais et j'ai la turbo flemme de chercher)
def Currentplay (val):
    
    result = (0,0)
    if val == "a1":
        result = (0,0)
    elif val == "a2":
        result = (0,1)
    elif val == "a3":
        result = (0,2)
    elif val == "b1":
        result = (1,0)
    elif val == "b2":
        result = (1,1)
    elif val == "b3":
        result = (1,2)
    elif val == "c1":
        result = (2,0)
    elif val == "c2":
        result = (2,1)
    elif val == "c3":
        result = (2,2)
    else:
        result = (10,10)
    return result     



#Check if a box is empty or not
def Check (liste, currentp):
    if liste[GetA(currentp)][GetB(currentp)] != int(0):
            res = False
    else:
            res = True
    return res


#Check for a winner in collumns, rows or diagonals

#Horizontal Movment
def HorizontalCheck (liste):
    HC = ""
    win = False
    if liste[0][0] == liste[0][1] == liste[0][2] != int(0):
        win = True
        HC = "H1"
    elif liste[1][0] == liste[1][1] == liste[1][2] != int(0):
         win = True
         HC = "H2"
    elif liste[2][0] == liste[2][1] == liste[2][2] != int(0):
        win = True
        HC = "H3"
    return (win, HC)

#Vertical Movement
def VerticalCheck (liste):
    VC = ""
    win = False
    if liste[0][0] == liste[1][0] == liste[2][0] != 0:
        win = True
        VC = "V1"
    elif liste[0][1] == liste[1][1] == liste[2][1] != 0:
        win = True
        VC = "V2"
    elif liste[0][2] == liste[1][2] == liste[2][2] != 0:
        win = True
        VC = "V3"
    return (win,VC)


#Diagonal Movment
def DiagonalCheck (liste):
    DC = ""
    win = False
    if liste[0][0] == liste[1][1] == liste[2][2] != 0:
        DC = "D1"
        win = True
    elif liste[2][0] == liste[1][1] == liste[0][2] != 0:
        DC = "D2"
        win = True
    return (win, DC)





#Determine what player played last turn based on the current turn 
def WhichPlayer (nb):
    if nb % 2 == 0:
        player = 2
    else:
        player = 1
    return player


#Replace Player number with its symbol
def Symbol (liste, case):
    if liste[GetA(case)][GetB(case)] == 0:
        symb = " "
    elif liste[GetA(case)][GetB(case)] == 1:
        symb = "O"
    else:
        symb = "X"
    return symb

#Draw PlayGround
def DrawPlayground (liste, col):
    D1 = ""
    D2 = ""
    V1 = ""
    V2 = ""
    V3 = ""
    H1 = ""
    H2 = ""
    H3 = ""

    if col == "H1":
        H1 = Back.RED
    if col == "H2":
        H2 = Back.RED
    if col == "H3":
        H3 = Back.RED
    if col == "V1":
        V1 = Back.RED
    if col == "V2":
        V2 = Back.RED
    if col == "V3":
        V3 = Back.RED
    if col == "D1":
        D1 = Back.RED
    if col == "D2":
        D2 = Back.RED


    print("  | 1  |  2 | 3") 
    print(Fore.WHITE + "a |", end = "")
    print(D1, H1, V1, end = "") 
    print(Fore.GREEN + Symbol(liste, (0,0)) + Back.BLACK, end = "")
    print(Fore.WHITE + " | ", end = "") 
    print(H1, V2, end = "")
    print("" + Fore.GREEN + Symbol(liste, (0,1)) + Back.BLACK, end = "")
    print(Fore.WHITE + " | ", end = "")
    print(H1, V3, D2, end = "")
    print(Fore.GREEN + Symbol(liste, (0,2)) + Back.BLACK)
    print(Fore.WHITE + "b | ", end = "")
    print(V1, H2, end = "")
    print(Fore.GREEN + Symbol(liste, (1,0)) + Back.BLACK, end = "") 
    print(Fore.WHITE + " |", end = "") 
    print(D1, D2, H2, D2, end = "")
    print(Fore.GREEN + Symbol(liste, (1,1)) + Back.BLACK, end = "") 
    print(Fore.WHITE + "|", end = "")
    print(V3, H2, end = "")
    print(Fore.GREEN + Symbol(liste, (1,2)) + Back.BLACK)
    print(Fore.WHITE + "c | ", end = "")
    print(V1, H3, D2, end = "")
    print(Fore.GREEN + Symbol(liste, (2,0)) + Back.BLACK, end = "")
    print(Fore.WHITE + "| ", end = "")
    print(H3, V2, end = "")
    print(Fore.GREEN + Symbol(liste, (2,1)) + Back.BLACK, end = "")
    print(Fore.WHITE + " | ", end = "")
    print(H3, V3, D1, end = "")
    print(Fore.GREEN + Symbol(liste, (2,2)) + Fore.WHITE + Back.BLACK)
          



def CheckAll(liste):
    what = ""
    what = HorizontalCheck(liste)[1] + VerticalCheck(liste)[1] + DiagonalCheck(liste)[1]
    return what






#Main function
def TicTacToe (liste):
    end = False
    turn = 0
    while xor(end, turn < 9):
        subpcs.run("clear")
        DrawPlayground(liste, None)
        inp = input('\n' '\n'"What will you play ? "'\n')
        uinput = Currentplay(inp)

        if uinput[0] != 10:
            if turn % 2 != 0:
                if not Check(grid, uinput):
                    print("You can't play here"'\n''\n')
                    input("Press any key to continue")
                else:
                    liste[GetA(uinput)][GetB(uinput)] = 2
                    turn += 1
                    end = HorizontalCheck(liste)[0] or VerticalCheck(liste)[0] or DiagonalCheck(liste)[0]
            else:
                if not Check(grid, uinput):
                    print("You can't play here"'\n''\n')
                    input("Press any key to continue")
                else:
                    liste[GetA(uinput)][GetB(uinput)] = 1
                    turn += 1
                    end = HorizontalCheck(liste)[0] or VerticalCheck(liste)[0] or DiagonalCheck(liste)[0]
        else:
            input("This is not a valid play, please play again :" '\n' '\n' "Press any key to continue")
    if end:
        subpcs.run("clear")
        DrawPlayground(liste, CheckAll(liste))
        print('\n''\n'"Player "+  str(WhichPlayer(turn)) + " won")
    else:
        subpcs.run("clear")
        DrawPlayground(liste, CheckAll(liste))
        print('\n''\n'"Nobody wins, it's a draw")
    


TicTacToe(grid)