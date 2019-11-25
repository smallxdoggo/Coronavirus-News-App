# project4.py

import mechanics


gamestate: mechanics.GameState
colors = ['A', 'B', 'C']
faller = mechanics.Faller()

def init_gamestate():
    rows = int(input('Rows: '))
    columns = int(input('Columns: '))
    gamestate = mechanics.GameState(rows, columns)

    begin = input('Empty or w/ contents: ').upper()
    if begin == 'EMPTY':
        print('is EMPTY')
        gamestate.empty_gameboard()
        
    elif begin == 'CONTENTS':
        print('is CONTENTS')
        gameboard = []
        for x in range(rows):
            contents = list(input())
            
            gameboard.append(contents)
        gamestate.set_gameboard(gameboard)

    return gamestate   


def commands(gamestate: mechanics.GameState):
    command = input()
    if command[0] == ' ':
        gamestate.pass_time()
    elif command[0] == 'F':
        command = command.split()
        faller = mechanics.Faller()
        faller.new_faller(int(command[1]), command[2:])
        gamestate.set_faller(faller)
        gamestate.update_faller()
        
    return gamestate

def display(gamestate):
    print(gamestate.get_gameboard())
    gameboard = gamestate.get_gameboard()

    output = ''

    for r in range(2, gamestate.get_rows()):
        output += '|'
        for c in range(gamestate.get_columns()):
            if gameboard[r][c][0] == '[' or gameboard[r][c][0] == '*':
                output += gameboard[r][c]
            else:
                output += f' {gameboard[r][c]} '
        output += '|'
        output += '\n' 

    output += ' '     
    for c in range(gamestate.get_columns()):
        output += f'---'
    output += ' '

    print(output)     

if __name__ == "__main__":
    gamestate = init_gamestate()
    display(gamestate)
    gamestate = commands(gamestate)
    display(gamestate)
    

    

