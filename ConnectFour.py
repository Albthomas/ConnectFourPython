# Project: Connect Four Game
# Filename: ConnectFour.py
# Author: Albert Thomas
# Date Created: 1/10/2022
# Date Modified: 1/11/2022
# Description: Basic Connect Four game using the terminal as the game board
def startup_screen():
    print("Welcome to Connect Four!")
    print("Type Instructions to see the rules")
    print("Type Start to begin the game")
    print("Type esc to close the game")
def print_instructions():
    print("---------------")
    print("Instructions")
    print("This is a two player game")
    print("Get 4 of a kind to win")
    print("During your turn select a column for your piece")
    print("The two colors are red and yellow")
    input("Press Enter to continue...")
    print("---------------")
def complete_check(gameboard):
    #this method verifies if there is a winner and returns the winner's name
    #check for 4 horizontal

    for i in range(0, 6): #for each row
        if(gameboard[i][3] != ' '):
            if((gameboard[i][3] == gameboard[i][0] and gameboard[i][3] == gameboard[i][1] and gameboard[i][3] == gameboard[i][2])
            or (gameboard[i][3] == gameboard[i][4] and gameboard[i][3] == gameboard[i][1] and gameboard[i][3] == gameboard[i][2])
            or (gameboard[i][3] == gameboard[i][4] and gameboard[i][3] == gameboard[i][5] and gameboard[i][3] == gameboard[i][2])
            or (gameboard[i][3] == gameboard[i][4] and gameboard[i][3] == gameboard[i][5] and gameboard[i][3] == gameboard[i][6])):
                return True, gameboard[i][3]

    #check for 4 vertical
    for j in range(0, 7): #for each column
        if(gameboard[2][j] != ' ' or gameboard[3][j] != ' '):
            if((gameboard[0][j] == gameboard[1][j] and gameboard[0][j] == gameboard[2][j] and gameboard[0][j] == gameboard[3][j])
            or (gameboard[1][j] == gameboard[4][j] and gameboard[1][j] == gameboard[2][j] and gameboard[1][j] == gameboard[3][j])
            or (gameboard[2][j] == gameboard[4][j] and gameboard[2][j] == gameboard[5][j] and gameboard[2][j] == gameboard[3][j])):
                return True, gameboard[2][j]
    #check for 4 horizontal top left to bottom right
    if(gameboard[2][0] == gameboard[3][1] and gameboard[2][0] == gameboard[4][2] and gameboard[2][0] == gameboard[5][3]
            and gameboard[2][0] != ' '):
        return True, gameboard[2][0]
    if(gameboard[0][3] == gameboard[1][4] and gameboard[0][3] == gameboard[2][5] and gameboard[0][3] == gameboard[3][6]
            and gameboard[0][3] != ' '):
        return True, gameboard[0][3]
    if ((gameboard[1][3] == gameboard[0][2] or gameboard[1][3] == gameboard[4][6]) and gameboard[1][3] == gameboard[2][4] and gameboard[1][3] == gameboard[3][5]
            and gameboard[1][3] != ' '):
        return True, gameboard[1][3]
    if (gameboard[2][3] == gameboard[3][4] and ((gameboard[2][3] == gameboard[1][2] and gameboard[2][3] == gameboard[4][5]
        ) or (gameboard[2][3] == gameboard[1][2] and gameboard[2][3] == gameboard[0][1])
        or (gameboard[2][3] == gameboard[5][6] and gameboard[2][3] == gameboard[4][5])) and gameboard[2][3] != ' '):
        return True, gameboard[2][3]
    if (gameboard[2][2] == gameboard[3][3] and ((gameboard[2][2] == gameboard[1][1] and gameboard[2][2] == gameboard[4][4]
        ) or (gameboard[2][2] == gameboard[1][1] and gameboard[2][2] == gameboard[0][0])
        or (gameboard[2][2] == gameboard[5][5] and gameboard[2][2] == gameboard[4][4])) and gameboard[2][2] != ' '):
        return True, gameboard[2][2]
    if ((gameboard[3][2] == gameboard[1][0] or gameboard[3][2] == gameboard[5][4]) and gameboard[3][2] == gameboard[2][1]
            and gameboard[3][2] == gameboard[4][3]
            and gameboard[3][2] != ' '):
        return True, gameboard[3][2]
    #check for 4 horizontal bottom left to top right
    if(gameboard[3][0] == gameboard[2][1] and gameboard[3][0] == gameboard[1][2] and gameboard[3][0] == gameboard[0][3]
            and gameboard[3][0] != ' '):
        return True, gameboard[3][0]
    if (gameboard[5][3] == gameboard[4][4] and gameboard[5][3] == gameboard[3][5] and gameboard[5][3] == gameboard[2][6]
            and gameboard[5][3] != ' '):
        return True, gameboard[5][3]
    if((gameboard[3][1] == gameboard[4][0] or gameboard[3][1] == gameboard[0][4]) and gameboard[3][1] == gameboard[2][2]
            and gameboard[3][1] == gameboard[1][3] and gameboard[3][1] != ' '):
        return True, gameboard[3][1]
    if ((gameboard[4][3] == gameboard[5][2] or gameboard[4][3] == gameboard[1][6]) and gameboard[4][3] == gameboard[3][4]
            and gameboard[4][3] == gameboard[2][5] and gameboard[4][3] != ' '):
        return True, gameboard[4][3]
    if(gameboard[3][3] == gameboard[2][4] and ((gameboard[3][3] == gameboard[4][2] and gameboard[3][3] == gameboard[5][1])
            or (gameboard[3][3] == gameboard[1][5] and gameboard[3][3] == gameboard[0][6])
            or (gameboard[3][3] == gameboard[1][5] and gameboard[3][3] == gameboard[4][2])) and gameboard[3][3] != ' '):
        return True, gameboard[3][3]
    if (gameboard[3][2] == gameboard[2][3] and ((gameboard[3][2] == gameboard[4][1] and gameboard[3][2] == gameboard[5][0])
            or (gameboard[3][2] == gameboard[1][4] and gameboard[3][2] == gameboard[0][5])
            or (gameboard[3][2] == gameboard[1][4] and gameboard[3][2] == gameboard[4][1])) and gameboard[3][2] != ' '):
        return True, gameboard[3][2]
    return False, ''
def start_game():
    complete = False
    gameboard = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ']] #empty board
    color = ''
    #initial board printout
    print("| | | | | | | |")
    print("| | | | | | | |")
    print("| | | | | | | |")
    print("| | | | | | | |")
    print("| | | | | | | |")
    print("| | | | | | | |")
    while complete == False:
        if (color == 'r'):  # change the color selection
            color = 'y'
            print("yellow's turn")
        else:
            color = 'r'
            print("red's turn")
        #row = int(input("row selection: "))
        column = int(input("column selection: "))
        while(column >6 or column <0 or gameboard[0][column] != ' '):
            print("invalid location. Try again")
            column = int(input("column selection: "))

        for i in range(0, 6):
            if gameboard[5 - i][column] == ' ':
                gameboard[5 - i][column] = color
                break
        for i in range(0,6):
            print("|", end = '')
            for j in range(0,7):
                print(gameboard[i][j], end = '')
                print("|", end = '')
            print("")#begin the new line


        complete, win = complete_check(gameboard)
        if complete == True:
            print('winner is: ', win)
            print('Thanks for playing!')

if __name__ == '__main__':
    print("---------------");
    while(1):#This loop will run until the user wants to close the program
        startup_screen()#prints the startup messages
        button = input()
        if (str.lower(button) == 'start'):
            #begin the game
            start_game()
            continue
        if (str.lower(button) == 'instructions'):
            #print the instructions
            print_instructions()
            continue
        if(str.lower(button) == 'esc'):
            print("closing program. Thanks for playing!")
            break
        print("Invalid Input")
        print("---------------");

