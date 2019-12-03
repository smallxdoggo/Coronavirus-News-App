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
        gamestate.update_gameboard()

    return gamestate   


def commands(gamestate: mechanics.GameState):
    faller = mechanics.Faller()
    faller.set_max_columns(gamestate.get_columns())
    while True:
        matched = gamestate.check_matches()
        display(gamestate)
        if matched:
            #display(gamestate)
            gamestate.update_gameboard()
            #display(gamestate)
            continue

        command = input()
        
        #try:
        if command[0] == ' ':
            faller.get_colors()
            gamestate.pass_time()
            gamestate.update_faller(faller)
            
        elif command[0] == 'F':
            command = command.split()
            faller = mechanics.Faller()
            faller.new_faller(int(command[1]), command[2:])
            gamestate.update_faller(faller)
        elif command[0] == 'R':
            faller.rotate()
            gamestate.update_faller(faller)
        elif command[0] == '<':
            faller.move_left()
            gamestate.move_faller(faller)
            gamestate.update_faller(faller)
        elif command[0] == '>':
            faller.move_right()
            gamestate.move_faller(faller)
            gamestate.update_faller(faller)
        elif command[0] == 'Q':
            break 
        else:
            print("OOP, SOMETHING AIN'T RIGHT")
        #except IndexError:
         #   pass
        
        


def display(gamestate):
    #print(gamestate.get_gameboard())
    gameboard = gamestate.get_gameboard()

    output = ''

    for r in range(2, gamestate.get_rows()):
        output += '|'
        for c in range(gamestate.get_columns()):
            if gameboard[r][c][0] == '[' or gameboard[r][c][0] == '*' or gameboard[r][c][0] == '|':
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
    commands(gamestate)
    
    

    

