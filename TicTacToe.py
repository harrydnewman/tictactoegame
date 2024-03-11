#Harry Newman, TicTacToe Game, IMA Application, 12/27/22;


import random
def Board():
    print()
    print("_____________")
    print("|",sp1,"|",sp2,"|",sp3,"|", sep=" ")
    print("|",sp4,"|",sp5,"|",sp6,"|", sep=" ")
    print("|",sp7,"|",sp8,"|",sp9,"|", sep=" ")
    print("_____________")
    print()
TL = []
PL = []
CC = []
sp1 = 1
sp2 = 2
sp3 = 3
sp4 = 4
sp5 = 5
sp6 = 6
sp7 = 7
sp8 = 8
sp9 = 9

d = {1: ['1', '2', '3'],
     2: ['4', '5', '6'],
     3: ['7', '8', '9'],
     4: ['1', '4', '7'],
     5: ['2', '5', '8'],
     6: ['3', '6', '9'],
     7: ['1', '5', '9'],
     8: ['3', '5', '7'],}



def StartGame():
    Board()
    while True:
        print("Hi I'm TicTac")
        playyn = input("do you wanna play tic-tac-toe with me? (y/n) ")
        if playyn == "y":
            print()
            print("Yay!")
            print("Lets go")
            print()
            break
        elif playyn == "n":
            print()
            print("Mmmm...TicTac doesn't think so")
            print("I think you're gonna play with me")
            print()
            break
        else:
            print()
            print("WHAT?! I DIDNT QUITE GET THAT!")
            print("I ASKED YOU, YES OR NO!")
            print()
    return

def TicTacWins():
    ttwl = {
            0: "HORRAY! TICTAC DOES IT AGAIN",
            1: "I AM THE CHAMPION!, TICTAC NEVER LOSES!",
            2: "SUCK IT BITCH"
            }
    ttwlg = random.randint(0,2)
    print(ttwl[ttwlg])


    
def TicTacLoses():
    ttll = {
            0: "NOOOOOOOOOOOOOOO",
            1: "YOU SUCK",
            2: "I CANT BELIEVE THIS, YOU CHEATED I NEVER LOSE!",
            3: "I CANT BELIEVE THIS. SCREW. YOU."
            }
    ttlln = random.randint(0,2)
    print(ttll[ttlln])


def WinTester(d, PL, CC):
    global endgame
    global restart
    endgame = False
    restart = False
    list0 = []
    list1 = []
    for x in range(1,9):
        for z in range(len(PL)):
            if PL[z] in d[x]:
                list0.append(PL[z])
                if len(list0) == 3:
                    TicTacLoses()
                    print()
                    print()
                    while True:
                        restart = input("Anyways...Do you wanna play again? (y/n) ")
                        if restart == "y":
                            print()
                            print()
                            restart = True
                            return restart      
                        elif restart == "n":
                            quit()
                            return
        list0 = []
        for y in range(len(CC)):
            if CC[y] in d[x]:
                list1.append(CC[y])  
                if len(list1) == 3:
                    TicTacWins()
                    print()
                    print()
                    while True:
                        restart = input("Do you wanna try again?\nI don't think you'll win but you can give it a shot! (y/n) ")
                        if restart == "y":
                            print()
                            print()
                            restart = True
                            return restart      
                        elif restart == "n":
                            quit()
                            return
        list1 = []
            

def PlayerTurn(PL):
    end = False
    while True:
        if end == True:
            break
        while True:
            pp = input("Please Select an Open Space (1-9): ")
            if pp == "1":
                if pp in TL:
                    break
                elif pp not in TL:
                    sp1 = "X"
                    TL.append(pp)
                    PL.append(pp)
                    PLtoBoard(PL)
                    end = True
                    break
            if pp == "2":
                if pp in TL:
                    break
                elif pp not in TL:
                    sp2 = "X"
                    TL.append(pp)
                    PL.append(pp)
                    PLtoBoard(PL)
                    end = True
                    break
            if pp == "3":
                if pp in TL:
                    break
                elif pp not in TL:
                    sp3 = "X"
                    PL.append(pp)
                    TL.append(pp)
                    PLtoBoard(PL)
                    end = True
                    break
            if pp == "4":
                if pp in TL:
                    break
                elif pp not in TL:
                    sp4 = "X"
                    TL.append(pp)
                    PL.append(pp)
                    PLtoBoard(PL)
                    end = True
                    break
            if pp == "5":
                if pp in TL:
                    break
                elif pp not in TL:
                    sp5 = "X"
                    TL.append(pp)
                    PL.append(pp)
                    PLtoBoard(PL)
                    end = True
                    break
            if pp == "6":
                if pp in TL:
                    break
                elif pp not in TL:
                    sp6 = "X"
                    TL.append(pp)
                    PL.append(pp)
                    PLtoBoard(PL)
                    end = True
                    break
            if pp == "7":
                if pp in TL:
                    break
                elif pp not in TL:
                    sp7 = "X"
                    TL.append(pp)
                    PL.append(pp)
                    PLtoBoard(PL)
                    end = True
                    break
            if pp == "8":
                if pp in TL:
                    break
                elif pp not in TL:
                    sp8 = "X"
                    TL.append(pp)
                    PL.append(pp)
                    PLtoBoard(PL)
                    end = True
                    break
            if pp == "9":
                if pp in TL:
                    break
                elif pp not in TL:
                    sp9 = "X"
                    TL.append(pp)
                    PL.append(pp)
                    PLtoBoard(PL)
                    end = True
                    break


def ComputerTurn(CC):
    goodplacement = False
    while True:
        if goodplacement == True:
            return
        elif goodplacement == False:
            number = random.randint(1,9)
            snum = str(number)
            while True:
                if snum in TL: 
                    goodplacement = False
                    break
                elif snum not in TL:
                    CC.append(snum)
                    TL.append(snum)
                    CCtoBoard(CC)
                    goodplacement = True
                    ttl = {
                            0: f'Hmmm...This is a hard one...\nI choose...{snum}!',
                            1: f'Ohh, my brain hurts!\nYou know what...{snum}',
                            2: f'I think {snum} will do the trick!',
                            3: f'I choose {snum}!'
                        }            
                    linepicker = random.randint(0,3)
                    print(ttl[linepicker])
                    return


def PLtoBoard(PL):
    global sp1
    global sp2
    global sp3
    global sp4
    global sp5
    global sp6
    global sp7
    global sp8
    global sp9
    for x in range(len(PL)):
        if "1" in PL:
            sp1 = "X"
        if "2" in PL:
            sp2 = "X"     
        if "3" in PL:
            sp3 = "X"    
        if "4" in PL:
            sp4 = "X"    
        if "5" in PL:
            sp5 = "X"  
        if "6" in PL:
            sp6 = "X"    
        if "7" in PL:
            sp7 = "X"    
        if "8" in PL:
            sp8 = "X" 
        if "9" in PL:
            sp9 = "X"
    

def CCtoBoard(CC):
    global sp1
    global sp2
    global sp3
    global sp4
    global sp5
    global sp6
    global sp7
    global sp8
    global sp9
    for x in range(len(CC)):
        if "1" in CC:
            sp1 = "O"      
        if "2" in CC:
            sp2 = "O"    
        if "3" in CC:
            sp3 = "O"     
        if "4" in CC:
            sp4 = "O"
        if "5" in CC:
            sp5 = "O" 
        if "6" in CC:
            sp6 = "O"    
        if "7" in CC:
            sp7 = "O"
        if "8" in CC:
            sp8 = "O"   
        if "9" in CC:
            sp9 = "O"



def TieGame():
    global endgame
    global restart
    endgame = False
    restart = False
    tttgl = {
            0: "BARNACLES!, HOW DID THAT HAPPEN?",
            1: "WHAT! I ALWAYS WIN!",
            2: "To me a tie is just as bad as a loss..."
            }
    tglp = random.randint(0,2)
    print(tttgl[tglp])
    print()
    print()
    while True:
        restart = input("Do you wanna try again so I can beat your ass? (y/n) ")
        if restart == "y":
            print()
            print()
            restart = True
            return restart      
        elif restart == "n":
            return endgame 
    



def ResetBoard():
    global sp1, sp2, sp3, sp4, sp5, sp6, sp7, sp8, sp9, PL, TL, CC
    sp1 = 1
    sp2 = 2
    sp3 = 3
    sp4 = 4
    sp5 = 5
    sp6 = 6
    sp7 = 7
    sp8 = 8
    sp9 = 9
    PL = []
    TL = []
    CC = []
    return sp1, sp2, sp3, sp4, sp5, sp6, sp7, sp8, sp9, PL, TL, CC

restart = False
def PlayGame():
    StartGame()
    Board()
    while True:
        PlayerTurn(PL)
        PLtoBoard(PL)
        Board()
        WinTester(d, PL, CC)
        if restart == True:
            ResetBoard()
            PlayGame()
        if endgame == True:
            return
        ComputerTurn(CC)
        Board()
        WinTester(d, PL, CC)
        if restart == True:
            ResetBoard()
            PlayGame()
        if endgame == True:
            return
        if len(TL) == 9:
            print("Tie")
            TieGame()
            if restart == True:
                ResetBoard()
                PlayGame()
            if endgame == True:
                return
            

PlayGame()
